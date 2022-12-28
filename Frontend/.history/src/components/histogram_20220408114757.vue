<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 11:47:31
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
      d3.selectAll('#' + this.uniID).append('svg')
        .attr('width', document.getElementById(this.uniID).offsetWidth)
        .attr('height', document.getElementById(this.uniID).offsetHeight)
      d3.append('text').attr('text', this.uniID).attr('x', i * nowStep + 10)
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