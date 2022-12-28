<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 11:44:04
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
      console.log('#' + this.uniID)
      d3.select('#' + this.uniID).append('svg')
        .attr('width', document.getElementById(this.uniID).offsetWidth)
        .attr('height', document.getElementById(this.uniID).offsetHeight)
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