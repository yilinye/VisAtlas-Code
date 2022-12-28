<template>
  <div style="height:100%;width:100%;">
    <!-- System Logo -->
    <div id="logoView">
      <img
        src="../assets/logo.png"
        alt=""
        style="width: 100%; height=auto;"
      >
    </div>
    <!-- Model -->
    <div id="modelView">
      <ModelView
        @getFilePath="getFilePath"
        @queryNode="updateQuery"
      />
    </div>
    <div id="settingView">
      <SettingView />
    </div>
    <!-- Selection -->
    <div id="selectView">
      <SelectView />
    </div>
    <!-- Main View -->
    <div id="mainView">
      <MainView
        ref="mainV"
        @updateTree="updateTree"
        @updateGallery="updateGallery"
      />
    </div>
    <!-- Embedding Dendrogram -->
    <!-- <div id="dendrogramView">
      <DendrogramView ref="dendrogram" @updateTree="updateTree"/>
    </div> -->
    <!-- Embedding Histogram -->
    <div id="histogramView">
      <HistogramView @updateTree="updateTree" />
    </div>
    <!-- Visualization Gallery -->
    <div id="galleryView">
      <GalleryView
        ref="gallery"
        @updateGType="updateType"
        @updateSelectNode="updateSelectNode"
      />
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import SelectView from "../components/selectView.vue";
import MainView from "../components/mainView.vue";
// import DendrogramView from "../components/dendrogramView.vue";
import HistogramView from "../components/histogramView.vue";
import GalleryView from "../components/galleryView.vue";
import ModelView from "../components/modelView.vue";
// import SettingView from "../components/settingView.vue";
import {zoom} from "https://cdn.skypack.dev/d3-zoom@3";
export default {
  components: { SelectView, MainView, HistogramView, GalleryView, ModelView },
  data () {
    return {
      //! init file path
      // pth: { filePath: "/src/visData/Beagle reorder.csv" },

      pth: { filePath: "/src/visData/data2vis reorder.csv" },
    }
  },
  provide () {
    //! we need provide an object, which can watch by other components
    return {
      fileP: this.pth,
    }
  },
  methods: {
    /**
     * @description: change file path from model view's <input>
     * @param {String} val file path from model
     * @return {*} none
     */
    getFilePath: function (val) {
      this.pth.filePath = val;
      this.fileP = this.pth;
    },
    /**
     * @description: change dendrogram view's tree
     * @param {Array} treeData data of the tree
     * @param {Int} sumTree Number of all selected elements
     * @return {*}
     */    
    updateTree (treeData, sumTree) {
      this.$refs.dendrogram.drawTree(treeData, sumTree);
    },
    /**
     * @description: change the gallery using new selected element data
     * @param {Array} data
     * @return {*}
     */    
    updateGallery (data) {
      this.$refs.gallery.setCloseNode(data);
    },
    /**
     * @description: change gallery type (Cosine or Projection) 
     * @param {*} data Calculation method of distance (Cosine or Projection) 
     * @return {*}
     */    
    updateType (data) {
      this.$refs.mainV.setGalleryType(data);
    },
    /**
     * @description: set a new selected node to refresh the system
     * @param {*} data selected element (node) data
     * @return {*}
     */    
    updateSelectNode (data) {
      this.$refs.mainV.setSelectNode(data);
    },
    /**
     * @description: query a new Picture
     * @param {*} data new picture information which from model view
     * @return {*}
     */    
    updateQuery (data) {
      this.$refs.mainV.setQuery(data);
    }
  }
}
</script>

<style>
#logoView {
  position: absolute;
  left: 5px;
  top: 5px;
  /* height: 17%; */
  width: 17%;
  margin-left: 5px;
  /* border: solid 1px rgb(163, 163, 163); */
}

#modelView {
  /* margin-left: 5px; */
  position: absolute;
  left: 5px;
  top: calc(15% + 5px + 5px);
  /* height: 25%; */
  height: 20%;
  width: 17%;
  /* border: solid 1px rgb(163, 163, 163); */
  border: solid 2px #A5C6C6;
  /* font-size:50px; */
  /* border-radius: 5px; */
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}

/* #settingView {
  position: absolute;
  left: 5px;
  top: calc(38% + 10px + 4px);

  height: calc(15% + 7px);
  width: 17%;

  border: solid 2px #A5C6C6;

  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
} */

#selectView {
  position: absolute;
  left: 5px;
  top: calc(35.5% + 15px + 1px);
  /* height: calc(58% - 30px); */
  height: calc(59.7% + 9px);
  width: 17%;
  /* border: solid 1px rgb(163, 163, 163); */
  border: solid 2px #A5C6C6;
  /* border-radius: 5px; */
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}

/* #mainView {
  position: absolute;
  left: calc(15px + 17%);
  top: calc(5px);
  height: calc(75%);
  width: calc(58%);

} */
#mainView {
  position: absolute;
  left: calc(15px + 17%);
  top: calc(5px);
  height: calc(100% - 25px);
  width: calc(43%);
  border: solid 2px #A5C6C6;
  /* border-radius: 5px; */
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}

/* #dendrogramView {
  position: absolute;
  left: calc(25px + 55%);
  top: calc(5px);
  height: calc(75%);
  width: calc(20% - 10px);
  border: solid 1px rgb(163, 163, 163);
  border-radius: 5px;
} */

/* #galleryView {
  position: absolute;
  left: calc(15px + 17%);
  top: calc(15px + 75%);
  height: calc(25% - 25px);
  width: calc(58%);
  border: solid 1px rgb(163, 163, 163);
  border-radius: 5px;
} */
#galleryView {
  position: absolute;
  left: calc(25px + 60%);
  top: calc(25px + 47%);
  height: calc(53% - 45px);
  width: calc(38%);
  /* border: solid 1px rgb(163, 163, 163); */
  border: solid 2px #A5C6C6;
  /* border-radius: 5px; */
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}

/* #histogramView {
  position: absolute;
  left: calc(25px + 75%);
  top: calc(5px);
  height: calc(100% - 15px);
  width: calc(25% - 30px);
  border: solid 1px rgb(163, 163, 163);
  border-radius: 5px;
} */
#histogramView {
  position: absolute;
  left: calc(25px + 60%);
  top: calc(5px);
  height: calc(82% - 318px);
  width: calc(38%);
  /* border: solid 1px rgb(163, 163, 163); */
  border: solid 2px #A5C6C6;
  /* border-radius: 5px; */
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}
</style>