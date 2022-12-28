<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-09 08:39:23
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
    /**
     * @description: data processing and use function
     * @param {String} filePath: which file will be use, selected in modelView.vue
     * @param {String} hisType: which feature will be draw
     * @return {*}
     */
    drawHistogram: function (filePath, hisType) {
      d3.csv(filePath).then((fileData) => {
        // index name need small letters
        hisType = hisType.toLowerCase();
        const hisData = new Object();
        for (let i = 0; i < fileData.length; ++i) {
          console.log(Math.floor(parseFloat(fileData[i][hisType])));
        }
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