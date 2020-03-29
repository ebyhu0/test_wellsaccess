from osgeo.osr import SpatialReference, CoordinateTransformation
# Define the Rijksdriehoek projection system (EPSG 28992)

# EPSG:4326 WGS 84
# EPSG:4229 Egypt 1907
# EPSG:22992 Egypt 1907 / Red Belt
# EPSG:22993 Egypt 1907 / Purple Belt 
# epsgRedBelt.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)

epsgPurpleBelt = SpatialReference()
epsgPurpleBelt.ImportFromEPSG(22993)
epsgPurpleBelt.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)

epsgRedBelt = SpatialReference()
epsgRedBelt.ImportFromEPSG(22992)
epsgRedBelt.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)

# correct the towgs84
# Egy 1907 7-par
# Define the wgs84 system (EPSG 4326)
epsgEgypt1907 = SpatialReference()
epsgEgypt1907.ImportFromEPSG(4229)
epsgEgypt1907.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)

epsgWgs84 = SpatialReference()
epsgWgs84.ImportFromEPSG(4326)


Red_WGS_latlon = CoordinateTransformation(epsgRedBelt, epsgWgs84)
WGS_Red_latlon2rd = CoordinateTransformation(epsgWgs84, epsgRedBelt)
pur_to_red = CoordinateTransformation(epsgPurpleBelt, epsgRedBelt)  
pur_to_wgs = CoordinateTransformation(epsgPurpleBelt, epsgWgs84)  

# Check the transformation for a point close to the centre of the projected grid
# Red_WGS_latz = Red_WGS_latlon.TransformPoint(615000.0, 810000.0)
# print(Red_WGS_latz) # (5.387203018813555, 52.002375635973344, 43.614926571026444)
# WGS_longLat_Red = WGS_Red_latlon2rd.TransformPoint(31, 30)
# print(WGS_longLat_Red) # (5.387203018813555, 52.002375635973344, 43.614926571026444)

Red_xy = pur_to_wgs.TransformPoint(670934.110, 305758.950)
print(Red_xy) # (5.387203018813555, 52.002375635973344, 43.614926571026444)
