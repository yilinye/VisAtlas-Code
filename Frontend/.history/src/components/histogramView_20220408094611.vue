<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 09:45:28
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div id="titleBar">
    {{ viewName }}
  </div>
  <div id="mainHistogram">
    <div v-for="ty in typeName" :key="ty" style="width: calc(50% - 10px); height: calc(20% - 10px); background-color: #22345;">

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