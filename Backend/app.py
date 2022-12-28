'''
Author: Qing Shi
LastEditTime: 2022-04-27 08:21:48
Knowledge: 
Description: 
Attention: 
'''
# from crypt import methods
# from crypt import methods
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import render_template
import os
import zipfile
import csv
import shutil
import json
import numpy as np
import io
import PIL
import PIL.Image
import pandas as pd
import tensorflow as tf
from PIL import Image

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin') or 'http://127.0.0.1:5000'  or 'http://localhost:8082/'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Origin, Referer, User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response
    
# app = Flask(__name__)


FILE_ABS_PATH = os.path.dirname(__file__)
app = Flask(__name__)
# app.after_request(after_request)

CORS(app)


base_model = tf.keras.applications.ResNet50(input_shape=(128, 256, 3),
                                            include_top=False,
                                            weights=None)
base_model.trainable = True
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer1 = tf.keras.layers.Dense(11)
inputs = tf.keras.Input(shape=(128, 256, 3))
rescale = tf.keras.layers.Rescaling(1. / 127.5, offset=-1)
x = rescale(inputs)
x = base_model(x)
x = global_average_layer(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = prediction_layer1(x)
model = tf.keras.Model(inputs, outputs)
op = tf.keras.optimizers.Adam(learning_rate=0.00005)
model.compile(optimizer=op,
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
base_model1 = tf.keras.applications.ResNet50(input_shape=(128, 256, 3),
                                             include_top=False,
                                             weights=None)
base_model1.trainable = True
global_average_layer1 = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer11 = tf.keras.layers.Dense(11)
inputs1 = tf.keras.Input(shape=(128, 256, 3))
rescale1 = tf.keras.layers.Rescaling(1. / 127.5, offset=-1)
x1 = rescale1(inputs1)
x1 = base_model1(x1)
x1 = global_average_layer1(x1)
x1 = tf.keras.layers.Dropout(0.2)(x1)
outputs1 = prediction_layer11(x1)
model1 = tf.keras.Model(inputs1, outputs1)
op1 = tf.keras.optimizers.Adam(learning_rate=0.00005)
model1.compile(optimizer=op1,
               loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
               metrics=['accuracy'])
model.load_weights(r"C:\Users\Yilin\Downloads\VisAtlas-main\Backend\11250.h5")
model1.load_weights(r"C:\Users\Yilin\Downloads\VisAtlas-main\Backend\forvis2.h5")


#model1.load_weights("forvis3.h5")
def softmax(x):
    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x


import gc
from tensorflow.keras import backend as k
va = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# allType = [
#     "area", "bar", "circle", "diagram", "line", "map", "matrix", "net",
#     "point", "table", "word"
# ]


@app.route('/')
def hello():
    return "hello"


@app.route('/api/getfile')
def return_file():
    # params = request.json;
    # print(request.json['filePath'])
    # print(FILE_ABS_PATH)
    # csvData = pd.read_csv(FILE_ABS_PATH + '/data/' + request.json['filePath'])
    # # print(csvData)

    # his_data = {}
    # for index, row in csvData.iterrows():
    #     # print(row['class'] not in his_data.keys())
    #     # print(type(row.to_dict()))
    #     for typeName in allType:
    #         if (row['class'] not in his_data.keys()):
    #             his_data[row['class']] = {}
    #         indexNum = math.floor(float(row[typeName]) * 10)
    #         if (indexNum == 10):
    #             indexNum -= 1
    #         if (indexNum == 0):
    #             continue
    #         # print(indexNum)
    #         if (indexNum not in his_data[row['class']].keys()):
    #             his_data[row['class']][indexNum] = {'cnt': 0, 'item': []}
    #         his_data[row['class']][indexNum]['cnt'] += 1
    #         his_data[row['class']][indexNum]['item'].append(row.to_dict())
    #         # print(row)
        #     break
        # break
    return "123"


@app.route('/api/getImg/', methods=['GET', 'POST'])
def getImg():
    # # 通过表单中name值获取图片
    # f = request.files["image"]
    # imgData = f.read()
    # print(f)
    # byte_stream = io.BytesIO(imgData)
    # print(request.json)
    # return "1";
    byte_stream = FILE_ABS_PATH + "\\uploadImage\\" + request.json['img_path']
    # print(byte_stream)
    # return "1"
    im = Image.open(byte_stream)
    width, height = im.size
    if width >= 2 * height:
        left = 0
        top = (int)((width / 2 - height) / 2)
        right = width
        bottom = width / 2 - top
        color = (255, 255, 255)
        im1 = Image.new(im.mode, (width, (int)(width / 2)), color)
        im1.paste(im, (left, top))
    else:
        left = (int)((2 * height - width) / 2)
        top = 0
        right = 2 * height - left
        bottom = height

        color = (255, 255, 255)
        im1 = Image.new(im.mode, (2 * height, height), color)
        im1.paste(im, (left, top))
    newsize = (256, 128)

    ref = im1.resize(newsize, PIL.Image.BILINEAR)
    try:
        img = tf.keras.preprocessing.image.img_to_array(ref)
        print("success: " + str(img.shape))
    except:
        print("error")
        print(type(imgData))
    if img.shape[2] == 4:
        png = ref.convert('RGBA')
        background = Image.new('RGBA', png.size, (255, 255, 255))

        alpha_composite = Image.alpha_composite(background, png)
        img0 = alpha_composite.convert("RGB")
        img = tf.keras.preprocessing.image.img_to_array(img0)

    imgs = [img]
    pre0 = model.predict(x=np.array(imgs))
    pre = softmax(pre0[0])
    pre1 = softmax(model1.predict(x=np.array(imgs))[0])
    for i in range(11):
        va[i] = str((2 * pre[i] + pre1[i]) / 3)

    return jsonify({
        "circle": va[0],
        "point": va[1],
        "net": va[2],
        "line": va[3],
        "area": va[4],
        "bar": va[5],
        "map": va[6],
        "matrix": va[7],
        "table": va[8],
        "word": va[9],
        "diagram": va[10]
    })


if __name__ == '__main__':
    app.run()

# # from crypt import methods
# # from crypt import methods
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import json
# import csv
# import os
# import numpy as np
# import pandas as pd
# import math
# FILE_ABS_PATH = os.path.dirname(__file__)

# app = Flask(__name__)
# CORS(app)

# allType = ["area", "bar", "circle", "diagram", "line", "map", "matrix", "net", "point", "table", "word"]

# @app.route('/')
# def hello():
#     return "hello"


# @app.route('/api/getfile', methods=['POST'])
# def return_file():
#     # params = request.json;
#     # print(request.json['filePath'])
#     # print(FILE_ABS_PATH)
#     csvData = pd.read_csv(FILE_ABS_PATH + '/data/' + request.json['filePath'])
#     # print(csvData)
        
#     his_data = {}
#     for index, row in csvData.iterrows():
#         # print(row['class'] not in his_data.keys())
#         # print(type(row.to_dict()))
#         for typeName in allType:
#             if (row['class'] not in his_data.keys()):
#                 his_data[row['class']] = {}
#             indexNum = math.floor(float(row[typeName]) * 10)
#             if (indexNum == 10): 
#                 indexNum -= 1
#             if (indexNum == 0):
#                 continue
#             # print(indexNum)
#             if (indexNum not in his_data[row['class']].keys()):
#                 his_data[row['class']][indexNum] = {
#                     'cnt': 0,
#                     'item': []
#                 }
#             his_data[row['class']][indexNum]['cnt'] += 1
#             his_data[row['class']][indexNum]['item'].append(row.to_dict())
#             # print(row)
#         #     break
#         # break
#     return jsonify({'data': his_data})

# if __name__ == '__main__':
#     app.run()

