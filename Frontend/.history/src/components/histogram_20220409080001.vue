<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-09 07:59:30
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
    // console.log(this.fileP);
    this.drawHistogram(this.fileP.filePath, this.uniID);
  },
  props: {
    uniID: String
  },
  inject: ['fileP'],
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
    drawHistogram: function (filePath, hisType) {
      d3.csv(filePath).then((hisData) => {
        console.log(hisData[0]);
        console.log(Math.floor(parseFloat(hisData[0].line) * 10));
        // for (let i =0; i < hisData.length; ++i) {

        //   // console.log(hisData[i], i);
        // }
      })
    }
  },
  watch: {
    fileP: {
      handler (newValue, oldValue) {
        console.log(newValue)
      },
      deep: true
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