<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 11:49:56
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
  created () {
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
      d3.selectAll('#' + this.uniID).append('svg')
        .attr('width', document.getElementById(this.uniID).offsetWidth)
        .attr('height', document.getElementById(this.uniID).offsetHeight)
      d3.append('text').text(this.uniID).attr('x', 10).attr('font-size', 15)
        .attr('font-weight', 'bold')
        .attr('font-family', 'STHeiti')
        .attr('y', 10);
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