from shapely.geometry import Point
from functools import partial
import pyproj
from shapely.ops import transform
 
point1 = Point(31, 30)

print (point1)

project = partial(
    pyproj.transform,
    pyproj.Proj(init='epsg:4229'),
    pyproj.Proj(init='epsg:4326'))

point2 = transform(project, point1)

# pyproj.transform(isn2004, UTM27N, x, y)

print (point2)