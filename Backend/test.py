'''
Author: Qing Shi
LastEditTime: 2022-04-17 21:41:28
Knowledge: 
Description: 
Attention: 
'''
import pandas as pd
import os
import numpy as np
import pandas as pd
import math
FILE_ABS_PATH = os.path.dirname(__file__)

csvData = pd.read_csv(FILE_ABS_PATH + '/data/' + 'Beagle reorder.csv')

allType = ["area", "bar", "circle", "diagram", "line", "map", "matrix", "net", "point", "table", "word"]

his_data = {}
for index, row in csvData.iterrows():
        # print(row['class'] not in his_data.keys())
        # print(type(row.to_dict()))
    for typeName in allType:
        if (row['class'] not in his_data.keys()):
            his_data[row['class']] = {}
        indexNum = math.floor(float(row[typeName]) * 10)
        if (indexNum == 10): 
            indexNum -= 1
        if (indexNum == 0):
            continue
        print(indexNum)
        if (indexNum not in his_data[row['class']].keys()):
            his_data[row['class']][indexNum] = {
                'cnt': 0,
                'item': []
            }
        his_data[row['class']][indexNum]['cnt'] += 1
        his_data[row['class']][indexNum]['item'].append(row.to_dict())
        # print(row)
        break
    break

print(his_data)