<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-12 22:41:44
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->

<template>
  <VisView/>
</template>

<script>
import VisView from "./views/visView.vue";

// var Event = new Vue();
export default {
    components: { VisView }
}
</script>

<style>
@import "./assets/base.css";

#app {
  height: calc(100%);
  font-weight: normal;
}

</style>
