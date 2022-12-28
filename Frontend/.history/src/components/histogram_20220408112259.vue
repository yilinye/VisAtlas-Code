<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 11:22:59
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
      // d3.select
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