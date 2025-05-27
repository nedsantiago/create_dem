# Create Watershed DEM

`qgis_create_dem.py` aims to simplify the raster mosaic process
by creating a watershed's Digital Elevation Model (DEM) 
using only the following inputs:

1. The path to the location (folder) of the DEM files
2. A vector geometry that indicates the estimated extent
of the watershed

`qgis_create_dem.py` assumes that the user will use:
WGS 84 / UTM Zone 51N (ESRI: 32651)
raw DEM files that are rectangular

`dem_from_list.py` aims to simplify the raster mosaic process
by creating a watershed's Digital Elevation Model (DEM) 
using only the following inputs:

1) A csv file with a list of all the dem tile names one
   wishes to merge
2) The folder location of all the relevant dem tiles

## Documentation
1) allow the user to search multiple DEM folders
2) provide a Graphical User Interface (GUI) to the user
3) add user input for buffer distance
4) provide support for more coordinate systems
5) GitHub integration
6) Use Design Patterns to increase modularity and readability

## Milestones
- Started `qgis_create_dem.py` on January 03, 2023.
- Started `dem_from_list.py` on August 09, 2023
- Completed `dem_from_list.py` version 1.0.0 on August 09, 2023
