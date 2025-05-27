###################################################################
#
#
# PROJECT: Create Watershed DEM
# PURPOSE:
# This script aims to simplify the raster mosaic process
# by creating a watershed's Digital Elevation Model (DEM) 
# using only the following inputs:
# 1) The path to the location (folder) of the DEM files
# 2) A vector geometry that indicates the estimated 
#    extent of the watershed
# AUTHOR: Ned Santiago, started on January 03, 2023.
#
# Notes:
# This script assumes that the user will use:
# WGS 84 / UTM Zone 51N (ESRI: 32651)
# raw DEM files that are rectangular
#
# Future planned updates: 
# 1) allow the user to search multiple DEM folders
# 2) provide a Graphical User Interface (GUI) to the user
# 3) add user input for buffer distance
# 4) provide support for more coordinate systems
# 5) GitHub integration
# 6) Use Design Patterns to increase modularity and readability
###################################################################


import os
from osgeo import gdal
from osgeo import ogr

# get vector
raster_folder_path = r"C:/02Python/create_dem/shp"
raster_file_name = r"shape.shp"
raster_file_path = os.path.join(raster_folder_path,raster_file_name)
layer = vector.GetLayer()
feature = layer.GetFeature(0)
v_Geometry = feature.GetGeometryRef()

# get vector's extents


# create a rectangle with buffer


# get raster folder
raster_folder_path = r"C:\02Python\create_dem\dem_metromanila"
raster_file_name = r"3130-II-9dtm.bil"
raster_file_path = os.path.join(raster_folder_path,raster_file_name)
print(f"Loading {raster_file_name}...")

# loop checking whether the DEM in the folder
# intersects with the vector


#   checking for extents
gtif = gdal.Open(raster_file_path)
geo_transform = gtif.GetGeoTransform()
print(f"Getting geotransform of {raster_file_name}...\n{geo_transform}")

minx = geo_transform[0]
maxy = geo_transform[3]
maxx = minx + geo_transform[1] * gtif.RasterXSize
miny = maxy + geo_transform[5] * gtif.RasterYSize
print(f"Results: \nminx = {minx} maxy = {maxy}")
print(f"maxx = minx + {geo_transform[1]} * {gtif.RasterXSize} = {maxx}")
print(f"miny = maxy + {geo_transform[5]} * {gtif.RasterYSize} = {miny}")

#   make a temporary rectangular vector using extents
r_vect = ogr.Geometry(ogr.wkbLinearRing)
r_vect.AddPoint(minx, maxy)
r_vect.AddPoint(minx, miny)
r_vect.AddPoint(maxx, maxy)
r_vect.AddPoint(maxx, miny)

r_geometry = ogr.Geometry(ogr.wkbPolygon)
r_geometry.AddGeometry(r_vect)
print(f"r_geometry: {r_geometry}")

#   check if vector intersects with a raster in folder
wkt1 = "POLYGON ((1208064.271243039 624154.6783778917, 1208064.271243039 601260.9785661874, 1231345.9998651114 601260.9785661874, 1231345.9998651114 624154.6783778917, 1208064.271243039 624154.6783778917))"
wkt2 = "POLYGON ((1199915.6662253144 633079.3410163528, 1199915.6662253144 614453.958118695, 1219317.1067437078 614453.958118695, 1219317.1067437078 633079.3410163528, 1199915.6662253144 633079.3410163528)))"

poly1 = ogr.CreateGeometryFromWkt(wkt1)
poly2 = ogr.CreateGeometryFromWkt(wkt2)

intersection = poly1.Intersection(poly2)

#print(intersection.ExportToWkt())

#   if intersects, add raster file to a list


# after all relevant rasters have been added to the list,
# merge all rasters in the list
