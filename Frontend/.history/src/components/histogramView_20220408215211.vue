<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 21:52:02
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
      v-bind:style="{ border: 'solid 1px', width: wd, height:hs, position: 'absolute', left: '2px', transform: 'translate(' + (index == 10 ? 'calc(50% + 5px)' : index % 2 ? 'calc(100% + 5px)' : '0') + ',' + 'calc(' + ((Math.floor(index / 2)) * 100) + '% + ' + ((Math.floor(index / 2)) * 2) + 'px' + ' + 5px)' + ')' }"
    >
      <Histogram :uniID="ty" :id="'His' + ty"/>
    </div>
  </div>
</template>

<script>
import Histogram from "./histogram.vue"
export default {
    data() {
        return {
            viewName: "Embedding Histogram",
            typeName: ["Area", "Bar", "Circle", "Diagram", "Line", "Map", "Matrix", "Net", "Point", "Table", "Word"],
            hs: "calc(17% - 14px)",
            wd: "calc(50% - 7px)"
        };
    },
    components: { Histogram }
}
</script>

<style>
#mainHistogram {
  height: calc(100% - 30px);
  width: calc(100%);
  /* background-color: #000; */
}
</style>