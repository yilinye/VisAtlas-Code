<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 11:27:51
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
      uniID: '0'
    }
  },
  methods: {
    createSVG: function () {

      //   d3.select(this.uniID).append('svg')
      //   .attr('width', )
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