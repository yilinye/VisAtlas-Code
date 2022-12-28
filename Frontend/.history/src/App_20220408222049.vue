
<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main> -->
  <div id="logoView">
    <img src="./assets/logo.png" alt="" style="width: 100%; height=auto;">
  </div>
  <div id="modelView">
    <ModelView/>
  </div>
  <div id="selectView">
    <SelectView/>
  </div>
  <div id="mainView">
    <MainView/>
  </div>
  <div id="dendrogramView">
    <DendrogramView/>
  </div>
  <div id="histogramView">
    <HistogramView/>
  </div>
  <div id="galleryView">
    <GalleryView/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import ModelView from './components/modelView.vue';
import SelectView from './components/selectView.vue';
import DendrogramView from './components/dendrogramView.vue';
import HistogramView from './components/histogramView.vue';
import GalleryView from './components/galleryView.vue';
import MainView from './components/mainView.vue';

// var Event = new Vue();
export default {
  components: {
    HelloWorld,
    TheWelcome,
    ModelView,
    SelectView,
    DendrogramView,
    HistogramView,
    GalleryView,
    MainView
  },
  methods: {
    getFilePath(val) {
      console.log(1)
      console.log(val);
    }
  }
}
</script>

<style>
@import "./assets/base.css";

#app {
  height: calc(100%);
  font-weight: normal;
}

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
