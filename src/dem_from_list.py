import os
from csv import reader

def main():
    dem_folder_path = r"P:\IFS\WEC_DATABASE\NAMRIA_IFSAR 2013\IFSARVisayas\4811_Panay_Negros_Cebu\DTM"
    csv_path = r"C:\01Project\99-000_Non-project_works\PresidentialBridge_Negros\CSV\ifsar_tiles\list_tiles.csv"
    output_path = r"C:\01Project\99-000_Non-project_works\PresidentialBridge_Negros\TIF\output.tif"
    dem_list = read_csv(csv_path=csv_path, folder_path=dem_folder_path)
    print(dem_list)
    dict_input = {
        'INPUT':dem_list,
        'PCT':False,
        'SEPARATE':False,
        'NODATA_INPUT':None,
        'NODATA_OUTPUT':-9999,
        'OPTIONS':'',
        'EXTRA':'',
        'DATA_TYPE':5,
        'OUTPUT':output_path
        }
    processing.run("gdal:merge", dict_input)
    print("Processing Complete!")

# read csv file function
def read_csv(csv_path, folder_path):
    # initialize list object to none
    list_dem = []

    # reader object
    # read csv
    with open(csv_path, "r",  encoding='utf-8-sig') as csv_file:
        readlines = reader(csv_file, delimiter=",")
        for line in readlines:
            file_name = line[0]+"dtm.bil"
            print(f"Appending: {file_name}")
            list_dem.append(os.path.join(folder_path, file_name))
    # return resulting list
    return list_dem

# base code
#processing.run("gdal:merge", {'INPUT':['P:/IFS/WEC_DATABASE/NAMRIA_IFSAR 2013/IFSARVisayas/4811_Panay_Negros_Cebu/DTM/3321-I-5dtm.bil','P:/IFS/WEC_DATABASE/NAMRIA_IFSAR 2013/IFSARVisayas/4811_Panay_Negros_Cebu/DTM/3321-I-10dtm.bil'],'PCT':False,'SEPARATE':False,'NODATA_INPUT':None,'NODATA_OUTPUT':-9999,'OPTIONS':'','EXTRA':'','DATA_TYPE':5,'OUTPUT':'TEMPORARY_OUTPUT'})

main()
