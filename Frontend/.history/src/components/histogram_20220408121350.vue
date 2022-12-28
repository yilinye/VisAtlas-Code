<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 12:13:00
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
  },
  props: {
    uniID: String
  },
  data () {
    return {

    }
  },
  methods: {
    createSVG: function () {
      const hisHeight = document.getElementById('His' + this.uniID).offsetHeight;
      const hisWidth = document.getElementById('His' + this.uniID).offsetWidth;
      console.log(hisHeight)
      d3.select('#His' + this.uniID)
        .append('svg')
        .attr('id', this.uniID + 'Svg')
        .attr('width', hisWidth)
        .attr('height', hisHeight)
    //   d3.select('#' + this.uniID + 'Svg')
    //     .append('text')
    //     .text(this.uniID)
    //     .attr('font-size', 15)
    //     // .attr('font-weight', 'bold')
    //     // .attr('font-family', 'STHeiti')
    //     .attr('text-align', 'center')
    //     .attr('y', 15)
    //     .attr('x', hisWidth / 2)
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