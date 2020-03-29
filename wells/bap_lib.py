
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
import math 
from .models import Concession, WellGeoinfo,Approved,Staked,Provisional,Psd

from osgeo.osr import SpatialReference, CoordinateTransformation

def egpc_Calc(ChLat,ChLong):

    if ChLat != '' and ChLong != '':
    
        capital_char= chr(int(ChLat) + 43)
        point1_lat=int((ChLat - int(ChLat))*60) # (ChLat - int(ChLat))*10 # to nearest 0.1 degree
        small_char= chr(int((point1_lat / 6) + 97)) #chr(int(point1_lat)+97)

        well_tens= (int(ChLong) - 25) * 10 # + 1 # * 10 
        point1_long=int((ChLong - int(ChLong))*60)
        well_unit= int(point1_long/6) + 1

        # egpc_block= capital_char + small_char + " " + str(well_tens) + str(well_unit)
        egpc_block= capital_char + small_char + " " + str(well_tens + well_unit)
        return egpc_block

        # WELL_CAP = Chr(eft(ChLat, 2) + 43) 'Chr(Int(ChLat / 10000) + 43)
        # WELL_SMALL = Chr(Int(Mid(ChLat, 3, 2) / 6) + 97) ' Chr(Int((ChLat - Int(ChLat / 10000) * 10000) / 100 / 6) + 97)
        
        # WELL_TEN = (Left(ChLong, 2) - 25) * 10 '(Int(ChLong / 10000) - 25) * 10
        # WELL_UNIT = Int(Mid(ChLong, 3, 2) / 6) + 1 'Int((ChLong - Int(ChLong / 10000) * 10000) / 100 / 6) + 1
        # EGPCName = WELL_CAP & WELL_SMALL & " " & Trim(Str(WELL_TEN + WELL_UNIT))
#        EGPCName = WELL_CAP & WELL_SMALL & " " & Trim(Str(WELL_TEN + WELL_UNIT)) & "-"
#        EGPC_Required = EGPCName & "%"
#        Well_Type = Wells_IN_Concession!Well_Type
#        i = WLS.get_Wells_In_EGPC_Block(EGPC_Required, Well_Type, Wells_In_EGPC_Block_RS)
        
#        If Wells_In_EGPC_Block_RS.RecordCount > 0 Then
#            Wells_In_EGPC_Block_RS.MoveLast
#
#            Select Case Well_Type
#            Case 1, 2, 5, 7, 9, 10 'If Well_Type <= 2 Then
#                dash_pos = InStr(1, Wells_In_EGPC_Block_RS!EGPC_NAME, "-", vbTextCompare)
#
#                EGPCNameComplete = EGPCName & _
#                    Format(Val(Mid(Wells_In_EGPC_Block_RS!EGPC_NAME, dash_pos + 1, _
#                    Len(Wells_In_EGPC_Block_RS!EGPC_NAME) - dash_pos)) + 1, "0000")
#
#
#                    EGPC_cbo.Text = Mid(EGPCName, 1, Len(EGPCName) - 1)
#            Case 3, 4 'Else
#                dash_pos = InStr(1, Wells_In_EGPC_Block_RS!EGPC_NAME, "-", vbTextCompare)
#                EGPC_cbo.Text = EGPCName & Format(Val(Mid(Wells_In_EGPC_Block_RS!EGPC_NAME, dash_pos + 1, Len(Wells_In_EGPC_Block_RS!EGPC_NAME) - dash_pos)) + 1, "00")
#            End Select
#
#        ElseIf Wells_In_EGPC_Block_RS.RecordCount = 0 Then
#            Select Case Well_Type
#            Case 1, 2, 5, 7, 9, 10 'If Well_Type <= 2 Then
#                'dash_pos = InStr(1, Wells_In_EGPC_Block_RS!EGPC_NAME, "-", vbTextCompare)
#                EGPCNameComplete = EGPCName & "1001"
#                EGPC_cbo.Text = Mid(EGPCName, 1, Len(EGPCName) - 1)
#            Case 3, 4 'Else
#                'dash_pos = InStr(1, Wells_In_EGPC_Block_RS!EGPC_NAME, "-", vbTextCompare)
#                EGPC_cbo.Text = EGPCName & "01"
#            End Select
#
#        End If
         
        # EGPC_cbo.Text = EGPCName

def Set_final_stake(request,st_id):
    pass
def Set_final_check(request,chk_id):
    pass    
def SetFinal(request,app_id):
     
    finalapp=Approved.objects.filter(app_id=app_id).first()
    wellInApp=finalapp.well_info
    provid=finalapp.prop.pk

    finalprov=Provisional.objects.filter(pk=provid).first()
    allapp=Approved.objects.filter(well_info=wellInApp.pk)
    allprov=Provisional.objects.filter(well_info=wellInApp.pk)
    wellinfoRow=WellGeoinfo.objects.filter(pk=wellInApp.pk).first()

    allapp.update(app_type='Option')
    allprov.update(prov_type='Option')

    finalapp.app_type='Final'
    finalprov.prov_type='Final'
    # finalapp.save()
    finalprov.prov_east=finalapp.app_east
    finalprov.prov_north=finalapp.app_north
    

    bingrid_points= finalprov.prov_seismic_survey.bindata_set.all().order_by('point')
    ## print("bg_id:" + str(bingrid_points.bg_id))
    # print("Vintage:" + finalprov.prov_seismic_survey.seismicvintage)
    
    if bingrid_points.count() == 3:
        # for n in bingrid_points:
            
        #     # article_group.append(n.article_set.all())
        #     # for field in n._meta.get_all_field_names():
        #     #     # print getattr(n, field, None)
        #     #     print (field)
        #     print("bg_id:" + str(n.bg_id))
        #     print("point:" + str(n.point))
        #     print("east:" + str(n.east))
        #     print("north:" + str(n.north))
        # BoxCornersList = bingrid_points.values_list('east','north')
        # BoxCornersList = list(BoxCornersList)
        # #otherlist=list(bingrid_points)
        # print(BoxCornersList[0][0],BoxCornersList[0][1])
        #print(otherlist)

        inline,xline= N_E_2_IN_X(bingrid_points,finalapp.app_east,finalapp.app_north)
        # print("Inline, Xline: " +  inline  + "," + xline)
    

    wellinfoRow.app_id=finalapp

    epsg_From=finalapp.projection.epsg
    epsg_To=22992 # RedBelt

    xlong_to,ylat_to,zcart_to,long_to,lat_to,zcart2_to  = coord_conv(epsg_From,epsg_To,finalapp.app_east,finalapp.app_north)

    # epsg_To=4229 # Egy1907
    # Longitude,Latitude,zcart2=coord_conv(epsg_From,epsg_To,finalapp.app_east,finalapp.app_north)
    # print("lat_to",lat_to)
    lat_ddmmss = float(dms_to_ddmmss(lat_to)) #Latitude
    long_ddmmss = float(dms_to_ddmmss(long_to))#Longitude
    lat_dd=ddmmss_to_dd(lat_ddmmss)
    long_dd=ddmmss_to_dd(long_ddmmss)

    # print("YYYYYY",lat_ddmmss,long_ddmmss)

    wellinfoRow.lat_red=lat_ddmmss
    wellinfoRow.long_red=long_ddmmss
    wellinfoRow.lat_EG_dd=lat_dd
    wellinfoRow.long_EG_dd=long_dd
    wellinfoRow.east_red=xlong_to
    wellinfoRow.north_red=ylat_to
    wellinfoRow.elevation=finalapp.app_elev
    wellinfoRow.egpc_name=egpc_Calc(lat_dd,long_dd)#(lat_to,long_to)
    


    finalapp.app_lat=lat_ddmmss
    finalapp.app_long=long_ddmmss
    
    if bingrid_points.count() == 3:
        finalapp.app_inline=inline
        finalapp.app_xline=xline

    finalapp.save()
    finalprov.save()
    wellinfoRow.save()

    return HttpResponseRedirect(reverse('update-well-view', kwargs={'pk':str(wellInApp.pk)}))


# def CoordTrans_ProjToGeo(epsg_From,epsg_To,east,north):
#     # epsg_From=finalapp.projection.epsg
#     # epsg_To=22992 # RedBelt

#     # East,North,zcart1=coord_conv(epsg_From,epsg_To,finalapp.app_east,finalapp.app_north)

#     # epsg_To=4229 # Egy1907
#     Longitude,Latitude,zcart2=coord_conv(epsg_From,epsg_To,east,north)

#     return Longitude,Latitude,zcart2

# def CoordTrans_GeoToProj(epsg_From,epsg_To,latitude,longitude):
#     # epsg_From=finalapp.projection.epsg
#     # epsg_To=22992 # RedBelt

#     East,North,zcart1=coord_conv(epsg_From,epsg_To,longitude,latitude)

#     # epsg_To=4229 # Egy1907
#     # Longitude,Latitude,zcart2=coord_conv(epsg_From,epsg_To,finalapp.app_east,finalapp.app_north)
#     return East,North,zcart1

def coord_conv(epsg_from,epsg_to,cord_xlong,cord_ylat):
    # 
    if epsg_from and epsg_to :

        epsgfrom = SpatialReference()
        epsgfrom.ImportFromEPSG(epsg_from)

        epsgto = SpatialReference()
        epsgto.ImportFromEPSG(epsg_to)

        #  Check for Projection exists
        if not epsgfrom.GetAttrValue("PROJCS|AUTHORITY", 1):
            cord_xlong=ddmmss_to_dd(cord_xlong)
            cord_ylat=ddmmss_to_dd(cord_ylat)

        psd2_IsProjected=False
        if epsgto.GetAttrValue("PROJCS|AUTHORITY", 1):
            psd2_IsProjected=True

        # Datum_epsg_from = epsgfrom.GetAttrValue("PROJCS|GEOGCS|AUTHORITY", 1)
        Datum_epsg_from = epsgfrom.GetAttrValue("GEOGCS|AUTHORITY", 1)
        Datum_epsg_to = epsgto.GetAttrValue("GEOGCS|AUTHORITY", 1)

        if int(Datum_epsg_from) == 4229:
            epsgfrom.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)

        if int(Datum_epsg_to) == 4229:
            epsgto.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)
        # ----------------------------
        if psd2_IsProjected:
            FromTo_psd = CoordinateTransformation(epsgfrom, epsgto)
            x_to,y_to,zcart_to = FromTo_psd.TransformPoint(cord_xlong, cord_ylat)
            x_to = format(round(x_to,2),'.2f')
            y_to = format(round(y_to,2),'.2f')
 
        else:
            x_to,y_to,zcart_to=None,None,None
    # -------- Case Projected To Get the datum from info of epsg2 and calculate lat/long------------------------
        epsgto.ImportFromEPSG(int(Datum_epsg_to))
        if int(Datum_epsg_to) == 4229:
            epsgto.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)
        FromTo_psd = CoordinateTransformation(epsgfrom, epsgto)
        long_to,lat_to,zcart2_to = FromTo_psd.TransformPoint(cord_xlong, cord_ylat)
        
        lat_to = ddmmss_to_dms(dd_to_ddmmss(lat_to)) + " N"
        long_to = ddmmss_to_dms(dd_to_ddmmss(long_to)) + " E"
        
    return (x_to,y_to,zcart_to,long_to,lat_to,zcart2_to)

def N_E_2_IN_X(BoxCorners,pointEast,pointNorth):
    # Dim Brg_1P, Brg_InLine, Brg_XLine, CompBearing, Alpha_P As Double
    # Dim Length_InLine, Length_XLine As Double
    # Dim D_L, D_T, Interval_Inline, Interval_XLine As Double
    # Dim East_D_L, North_D_T As Double
    # Dim Length_1P As Double
 
    BoxCornersList = BoxCorners.values_list('inline','xline','east','north')
    BoxCornersList = list(BoxCornersList)

    # # print(BoxCornersList[0][0],BoxCornersList[0][1])

    CompBearing= Bearing_Calc( BoxCornersList[0][2], BoxCornersList[0][3], BoxCornersList[1][2], BoxCornersList[1][3])
    Brg_XLine = CompBearing

    CompBearing= Bearing_Calc( BoxCornersList[0][2], BoxCornersList[0][3], pointEast, pointNorth)
    Brg_1P = CompBearing

    Length_InLine = math.sqrt((BoxCornersList[1][2] - BoxCornersList[0][2]) ** 2 + (BoxCornersList[1][3] - BoxCornersList[0][3]) ** 2)
    Length_XLine = math.sqrt((BoxCornersList[2][2] - BoxCornersList[1][2]) ** 2 + (BoxCornersList[2][3] - BoxCornersList[1][3]) ** 2)

    Interval_Inline = Length_InLine / (BoxCornersList[1][0] - BoxCornersList[0][0])
    Interval_XLine = Length_XLine / (BoxCornersList[2][1] - BoxCornersList[1][1])

    Length_1P = math.sqrt(((pointEast - BoxCornersList[0][2])) ** 2 + ((pointNorth - BoxCornersList[0][3])) ** 2)
    Alpha_P = (Brg_XLine - Brg_1P) # Abs(Brg_XLine - Brg_1P)

    D_T = Length_1P * math.sin(Alpha_P) / Interval_XLine
    D_L = Length_1P * math.cos(Alpha_P) / Interval_Inline

# str(format(inline, '.2f')) 
    # new_Point_InLine =format(BoxCornersList[0][0] + D_L,"#.00") # Round 2
    # new_Point_XLine = format(BoxCornersList[0][1] + D_T, "#.00")# Round 2
    new_Point_InLine =format(BoxCornersList[0][0] + D_L,".2f") # Round 2
    new_Point_XLine = format(BoxCornersList[0][1] + D_T, ".2f")# Round 2

    return new_Point_InLine,new_Point_XLine

def Bearing_Calc(east_fst_point, north_fst_point, east_snd_point, north_snd_point):


 
    D_east = east_snd_point - east_fst_point
    D_north = north_snd_point - north_fst_point

    Bearing_atan2=math.atan2(D_east,D_north)

#    pi_value = 4 * math.atan(1)

#     if D_east >= 0 and D_north > 0:
#         CompBearing = math.atan((D_east) / (D_north))

#     elif D_east >= 0 and D_north < 0:
#         CompBearing = pi_value - abs(math.atan((D_east) / (D_north)))

#     elif D_east >= 0 and D_north == 0:
#         CompBearing = pi_value / 2

#     elif D_east < 0 and D_north < 0:
#         CompBearing = abs(math.atan((D_east) / (D_north))) + pi_value

#     elif D_east < 0 and D_north > 0:
#         CompBearing = 2 * pi_value - abs(math.atan((D_east) / (D_north)))

#     elif D_east < 0 and D_north == 0:
#         CompBearing = 3 / 2 * pi_value

#     if CompBearing >= 2 * pi_value:
#         CompBearing = CompBearing - (2 * pi_value)
    # return CompBearing
    return Bearing_atan2

def decimal_places(value,decimalplaces):
    return format(value , '.' + str(decimalplaces) + 'f')


def zero_Pad_left(value,numberOfDigits):
    return str(value.zfill(numberOfDigits)) 

def dd_to_ddmmss(dd):
    dd1 = round(abs(float(dd)) ,10)

    cdeg = int(dd1)  
    minsec = dd1 - cdeg  
    # print(minsec)
    cmin = int(minsec * 60)
    # print(cmin)
    #csec = (minsec % 60) / float(3600)
    csec = ((minsec*60)-cmin)*60

    if dd < 0: cdeg = cdeg * -1
    degree_sign= u'\N{DEGREE SIGN}'
    # return str(cdeg) + degree_sign + str(cmin).zfill(2) + "'" + str(format(csec, '.3f')).zfill(6) + '\"'  #:.2f
    return str(cdeg) + str(cmin).zfill(2)  + str(format(csec, '.3f')).zfill(6)


def ddmmss_to_dms(ddmmss):
    return (ddmmss[:2] + "°" + ddmmss[2:4] + "\'" + ddmmss[4:] +  "\"")


def ddmmss_to_dd(ddmmss):
    deg=str(ddmmss)[:2]    
    # print(deg)
    min=str(ddmmss)[2:4]    
    # print(min)
    sec=str(ddmmss)[4:]    
    # print(sec)
    ddmmss_to_dd=float(sec)/3600+float(min)/60+float(deg)
    # print(ddmmss_to_dd)
    return float(sec)/3600+float(min)/60+float(deg)

def dms_to_ddmmss(dms):
    dd_delimeter = dms.find('°')
    mm_delimeter = dms.find("'")
    ss_delimeter = dms.find('"')
    if ss_delimeter <=0:
        ss_delimeter = dms.find("''")

    dd1=dms[:dd_delimeter] 
    mm1=dms[dd_delimeter+1:mm_delimeter] 
    ss1=dms[mm_delimeter+1:ss_delimeter] 

    # print("FFFF" + dd1,mm1,ss1)

    if len(mm1) <2:
        # print("RRRRR" + mm1)
        mm1=mm1.zfill(2)
    
    if len(ss1) <2:
        # print("TTTT" + ss1)
        ss1=str(format(ss1, '.3f')).zfill(6)
    
    ddmmss=str(dd1)+str(mm1)+str(ss1)
    # print("GGGGGGGG" + ddmmss)

    return ddmmss




