<template>
  <div id="logoView">
    <img
      src="../assets/logo.png"
      alt=""
      style="width: 100%; height=auto;"
    >
  </div>
  <div id="modelView">
    <ModelView @getFilePath="getFilePath" />
  </div>
  <div id="selectView">
    <SelectView />
  </div>
  <div id="mainView">
    <MainView />
  </div>
  <div id="dendrogramView">
    <DendrogramView />
  </div>
  <div id="histogramView">
    <HistogramView />
  </div>
  <div id="galleryView">
    <GalleryView />
  </div>
</template>

<script>

import * as d3 from 'd3';
import SelectView from "../components/selectView.vue";
import MainView from "../components/mainView.vue";
import DendrogramView from "../components/dendrogramView.vue";
import HistogramView from "../components/histogramView.vue";
import GalleryView from "../components/galleryView.vue";
import ModelView from "../components/modelView.vue";
export default {
  components: { SelectView, MainView, DendrogramView, HistogramView, GalleryView, ModelView },
  data () {
    return {
      pth: { filePath: "/src/visData/Beagle reorder.csv" }
    }
  },
  provide () {
    return {
      fileP: this.pth,
    }
  },
  methods: {
    getFilePath: function (val) {
      this.pth.filePath = val;
      this.fileP = this.pth;
    }
  }
}
</script>

<style>

#logoView {
  position: absolute;
  left: 5px;
  top: 5px;
  height: 17%;
  width: 17%;
  /* border: solid 1px; */
}

#modelView {
  position: absolute;
  left: 5px;
  top: calc(17% + 5px + 5px);
  height: 25%;
  width: 17%;
  border: solid 1px;
  border-radius: 5px;
}

#selectView {
  position: absolute;
  left: 5px;
  top: calc(42% + 15px + 5px);
  height: calc(58% - 30px);
  width: 17%;
  border: solid 1px;
  border-radius: 5px;
}

#mainView {
  position: absolute;
  left: calc(15px + 17%);
  top: calc(5px);
  height: calc(70%);
  width: calc(38%);
  /* border: solid 1px;
  border-radius: 5px; */
}

#dendrogramView {
  position: absolute;
  left: calc(25px + 55%);
  top: calc(5px);
  height: calc(70%);
  width: calc(20% - 10px);
  border: solid 1px;
  border-radius: 5px;
}

#galleryView {
  position: absolute;
  left: calc(15px + 17%);
  top: calc(15px + 70%);
  height: calc(30% - 25px);
  width: calc(58%);
  border: solid 1px;
  border-radius: 5px;
}

#histogramView {
  position: absolute;
  left: calc(25px + 75%);
  top: calc(5px);
  height: calc(100% - 15px);
  width: calc(25% - 30px);
  border: solid 1px;
  border-radius: 5px;
}
</style>