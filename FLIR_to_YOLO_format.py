import os
import json

json_files = "/home/OD/FLIR_ADAS_1_3/train/thermal_annotations.json"

with open(json_files, 'r') as f:
    data = json.load(f) 
    annotations = data['annotations']
    image = data['images']
    
    width = 640
    height = 512

    # image_id는 object의 갯수만큼
    # print(len(image))   # 8862
    for i in range(0, len(image)):  
        result = []     # init; for next file
        for j in annotations:
            if j['image_id'] == i:
                category_id = int(j['category_id'])

                if category_id == 17: category_id = 3
                else: category_id -= 1

                x_loc, y_loc, w_loc, h_loc = map(float, j['bbox'])
                x_center, y_center = w_loc/2 + x_loc, h_loc/2 + y_loc

                # relative location
                x, y = x_center/width, y_center/height
                w, h = w_loc/width, h_loc/height
    
                result.append((category_id, x, y, w, h))

        img_name = image[i]['file_name']
        img_name = img_name[14:-5]
        print(img_name) 

        file = open('/home/OD/x64/Release/data/img/' + str(img_name) + '.txt', 'w')
        #file.write('\n'.join('%d %.4f %.4f %.4f %.4f' % res for res in result))
        file.write('\n'.join('%d %.6f %.6f %.6f %.6f' % res for res in result))
        file.close()
    