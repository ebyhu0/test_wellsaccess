from pyproj import Proj, transform
  
# copy the SR-ORG:6781 definition in Proj4 format from http://spatialreference.org/ref/sr-org/6781/
p1 = Proj("+proj=sterea +lat_0=52.15616055555555 +lon_0=5.38763888888889 +k=0.9999079 +x_0=155000 +y_0=463000 +ellps=bessel +towgs84=565.237,50.0087,465.658,-0.406857,0.350733,-1.87035,4.0812 +units=m +no_defs")

p2 = Proj(proj='latlong',datum='WGS84')
 
# Transform point (155000.0, 446000.0) with SR-ORG:6781
lon, lat, z = transform(p1, p2, 155000.0, 446000.0, 0.0)
print(lon, lat, z) # 5.38720301881 52.002375636 43.614926571