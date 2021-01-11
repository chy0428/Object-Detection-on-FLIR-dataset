import os
import glob 
import json
from collections import Counter

# TO DO: thermal_annotations.json 에서
# annotations 전부 읽은 후 각 category id의 빈도수 파악

json_files = "/home/OD/FLIR_ADAS_1_3/train/thermal_annotations.json"

with open(json_files, 'r') as f:
    data = json.load(f) 
    annotations = data['annotations']

    print(len(annotations)) #image num * object num
    
    arr = []
    for category in annotations:
        arr.append(category['category_id'])
    count = Counter(arr)    
    print(count)
  