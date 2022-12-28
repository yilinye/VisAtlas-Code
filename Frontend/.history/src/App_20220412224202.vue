<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-12 22:41:44
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->

<template>
  <!-- <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
  </main> -->
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
