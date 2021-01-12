import os
 
path_dir = '/Volumes/data_usb/FLIR_ADAS_1_3/train/Annotated_thermal_8_bit'
file_list = os.listdir(path_dir)

f = open('train.txt', mode='wt', encoding='utf-8')
f.write("\nx64/Release/data/img/".join(file_list))
f.close()

