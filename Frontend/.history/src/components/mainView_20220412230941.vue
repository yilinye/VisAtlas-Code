<template>
  <!-- <div id="titleBar">
    {{ viewName }}
  </div> -->
  <div id="mainViewPic">

  </div>
</template>

<script>
import * as d3 from 'd3';
export default {
  data () {
    return {
        viewName: "Model"
    }
  },
  methods: {
    createSVG () {
      d3.select("#mainViewPicSvg").remove();
      
    }
  }
}
</script>

<style>
</style>