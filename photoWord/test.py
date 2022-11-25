import numpy as np
import os

myImage = []
dir_path = "./Photo/"
dirFiles = os.listdir ( "./Photo/" )
dirFiles.sort ( )
# print ( dirFiles )

dir_full_paths = []
for i in dirFiles :
    full_paths = os.path.join ( dir_path, i )
    dir_full_paths.append (full_paths)

image = os.listdir ( dir_full_paths[0] )
image.sort ( )
dir_path_0 = os.path.join (dir_full_paths[0], image[0] )
print ( dir_path_0 )

# print ( dir_full_paths )

all_images_list = []

# for k in dir_full_paths :
#     each_image_path = os.path.join ( dir_full_paths[k], os.listdir( dir_full_paths[k] ) )
#     all_images_list.append ( each_image_path )

# print ( all_images_list )