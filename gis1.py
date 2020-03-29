import arcpy
import pandas

# connect to GIS
from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
# from arcgis.features import features
import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
from IPython.display import display


# try:
#     import archook #The module which locates arcgis
#     archook.get_arcpy()
#     import arcpy
# except ImportError:
# print('do whatever you do if arcpy isnt there.')


# gis = GIS("https://bap-s-bxlm.bapetco.com/portal/    ", 'geomatics_publisher', 'qwerty@12',verify_cert=False)
# # gis = GIS() # anonymous connection to www.arcgis.com

# item = gis.content.get('fe25c45ae23742ffa700fbbd0c89096c')
# flayer = item.layers[0]
# sdf = pd.DataFrame.spatial.from_layer(flayer)
# sdf.head()

# search_result= gis.content.search("wells11", "Feature Layer")

# ports_item = search_result[0]
# ports_item

# freeways.layers
# earch_results = gis.content.search('title: edit_wells_geo','Feature Layer')

# --------

# Access the first Item that's returned
# major_cities_item = search_results[0]


# search for the feature layer named Ports along west coast
# search_result = gis.content.search('title:edit_wells_geo')
# search_result2 = gis.content.search('title:wells_geo_test_edit')


# search_result[0]
# search_result2[0]

# access the item's feature layers
# ports_item = search_result[0]

# print(search_result)
# ports_layers = ports_item.layers
# ports_layers

print("End of Script")

arcpy.env.workspace = r"D:\Bapetco_Jobs\test\test11.gdb"
fc = "Point11"
fields = ["SHAPE@XY"]
pnt = arcpy.Point()
print("Test11")

with arcpy.da.SearchCursor("Point11", ["SHAPE@X"]) as cursor:
    for row in cursor:
        print("{0}" .format(row[0]))


pnt = arcpy.Point()
pnt.X = 615000
pnt.Y = 810000

print("X: {0}, Y: {1}".format(pnt.X, pnt.Y))
