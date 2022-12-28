<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 10:51:43
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div id="titleBar">
    {{ viewName }}
  </div>
  <div id="mainHistogram">
    <div
      v-for="(ty, index) in typeName"
      :key="ty"
      v-bind:style="{background:'red', width: 'calc(49%)',height:ls }"
    >
      {{index}}
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      viewName: "Embedding Histogram",
      typeName: ["Area", "Bar", "Circle", "Diagram", "Line", "Map", "Matrix", "Net", "Point", "Table", "Word"],
      ls: 'calc(60% + 100px)'
    }
  }
}
</script>

<style>
#mainHistogram {
  height: calc(100% - 30px);
  width: calc(100%);
  /* background-color: #000; */
}
</style>