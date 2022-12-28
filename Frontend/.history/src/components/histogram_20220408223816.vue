<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 22:37:26
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div
    id=""
    class="hisType"
  >

  </div>
</template>

<script>
import * as d3 from 'd3';
export default {
  mounted () {
    this.createSVG();
    console.log(this.fileAll.filePath);
  },
  props: {
    uniID: String
  },
  inject: ['fileAll'],
  data () {
    return {

    }
  },
  methods: {
    createSVG: function () {
      const hisHeight = document.getElementById(('His' + this.uniID)).offsetHeight;
      const hisWidth = document.getElementById(('His' + this.uniID)).offsetWidth;
      d3.select('#His' + this.uniID)
        .append('svg')
        .attr('id', this.uniID + 'Svg')
        .attr('width', hisWidth)
        .attr('height', hisHeight)
      d3.select('#' + this.uniID + 'Svg')
        .append('text')
        .text(this.uniID)
        .attr('font-size', 15)
        .attr('text-anchor', 'middle')
        .attr('y', 15)
        .attr('x', hisWidth / 2)
    },
    drawHistogram: function () {
        
    }
  }
}
</script>

<style>
.hisType {
  /* border: 1px solid; */
  width: 100%;
  height: 100%;
}
</style>