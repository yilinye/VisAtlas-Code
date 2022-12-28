<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-09 10:24:23
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
        let hisTag = hisType.toLowerCase();
        const hisData = new Object();
        for (let i = 0; i < fileData.length; ++i) {
          let indexNum = Math.floor(parseFloat(fileData[i][hisTag]) * 10);
          if (indexNum == 10) indexNum--; // let 1 to 0.9 ~ 1
          if (indexNum == 0) continue;
          if (isNaN(hisData[indexNum])) {
            hisData[indexNum] = 0;
          }
          hisData[indexNum]++;
        }
        const hisArray = new Array();
        for (let i in hisData) {
          hisArray.push(hisData[i]);
        }
        this.drawRectAndAxis(hisArray, hisType);
      })
    },
    drawRectAndAxis: function (hisArray, hisType) {
      const hisHeight = document.getElementById(('His' + this.uniID)).offsetHeight;
      const hisWidth = document.getElementById(('His' + this.uniID)).offsetWidth;
      // remove old View
      d3.select("#his_g_" + hisType).remove();
      // define new View
      const his_g = d3.select("#" + hisType + "Svg")
        .append('g')
        .attr("id", "his_g_" + hisType);
      const xAxis = d3.scaleLinear()
        .domain([0.1, 1.0])
        .range([0, 0.7 * hisWidth])
      const yAxis = d3.scaleLinear()
        .domain([0, d3.max(hisArray)])
        .range([0.7 * hisHeight, 0])
        .attr("transform", `translate(${0.2 * hisWidth}, ${0.8 * hisHeight})`);
      console.log(1);
      his_g.append('g')
        .call(d3.axisBottom(xAxis).ticks(5))
        .attr("transform", `translate(${0.2 * hisWidth}, ${0.8 * hisHeight})`);

      his_g.append('g')
        .call(d3.axisLeft(yAxis).ticks(5))

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