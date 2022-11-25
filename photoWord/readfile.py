import os
import numpy as np

set_photo_path = "./Photo/"

get_folders = os.listdir ( set_photo_path )
get_folders.sort ( )
each_folder_path = [ set_photo_path + folder for folder in get_folders ]

images_path = [ ]

for path in each_folder_path :
    folder_images = os.listdir ( path )
    folder_images.sort ( )
    each_image_path = [ path + "/" + image for image in folder_images ]
    images_path.append ( each_image_path )

path_array = np.array ( images_path )