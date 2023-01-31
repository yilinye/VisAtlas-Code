<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-05-01 00:28:31
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
# VisAtlas

![image](https://github.com/sqsssq/VisAtlas/blob/main/others/sys220501.png)
This is the code for our paper **VISAtlas: An Image-based Exploration and Query System for Large Visualization Collections via Neural Image Embedding** https://ieeexplore.ieee.org/abstract/document/9984953
VISAtlas is an image-based approach empowered by neural image embedding, which can facilitate exploration and query for visualization collections. 
This system based on 3 different sources, Beagle(real-world visualization collection), VIS30K(real-world visualization collection) and Data2Vis(synthetic collection).
And we train a CNN model for taxonomical classification of visualizations.
## Installation
You need install [Node.js](http://nodejs.cn/download/) and [Python](https://www.python.org/).
### Python dependency Library
They're all in the requirement.txt.
```sh
tensorflow==2.8.0
numpy==1.21.6
Flask_Cors==3.0.6
pandas==0.23.4
Flask==2.1.1
Pillow==9.1.0
```
### Install all dependency
```sh
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

## Data
### Source Data
```
imdb_vis30k.zip
imdb_Beagle.zip
data2vis_imdb.zip
download link https://drive.google.com/drive/folders/1jBBQm_Yi8ri9NFGW33Wyp9eazc_ZMjhr?usp=sharing
```
### File Path
You need to put `imdb_vis30k`, `imdb_Beagle` and `data2vis_imdb` in `/Frontend/src/assets/static/`.

### Picture to Query
You should put the pictures in `/Frontend/src/assets/static/uploadImage/` and `/Backend/uploadImage/`.


## How To Run this Project

### Frontend -- Vue

#### Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.vscode-typescript-vue-plugin).

#### Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

#### Enter the Folder

```sh
cd Frontend
```

#### Project Setup

```sh
npm install
```

#### Compile and Hot-Reload for Development

```sh
npm run dev
```

#### Compile and Minify for Production

```sh
npm run build
```
---

### Backend -- Flask

#### Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) or [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) 

#### Enter the Folder

```sh
cd Backend
```

#### Compile and Run for Development
```sh
set FLASK_APP=app.py
flask run
```

#### Change .h5 Path
In the app.py, I use absolute address in two places. You need to change them into yours.
```py
model.load_weights(r"<PROJECT_ROOT>\Backend\11250.h5")
model1.load_weights(r"<PROJECT_ROOT>\Backend\forvis2.h5")
```
