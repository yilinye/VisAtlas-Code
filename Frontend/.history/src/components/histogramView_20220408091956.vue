<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 09:19:51
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div id="titleBar">
    {{ viewName }}
  </div>
  <div id="mainHistogram"></div>
</template>

<script>
export default {
  data () {
    return {
        viewName: "Embedding Histogram"
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