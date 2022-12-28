<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 10:37:29
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
      v-bind:style="'background-color:red;width:calc(49%);position:absolute;transform:translate(' + (index % 2 ? '100%' : '0%') + ', '+ index*100 +'px)'"
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
      typeName: ["Area", "Bar", "Circle", "Diagram", "Line", "Map", "Matrix", "Net", "Point", "Table", "Word"]
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