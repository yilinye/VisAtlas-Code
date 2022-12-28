<template>
  <div style="width: 100%; height: 100%;">
    <div id="titleBar" style="transform:translate(0,-1px)">
      <span style="position: absolute; left: 40%;">{{ viewName }}</span>
      <span style="float: right">
        <form
          id="select-distance"
          style="margin-top:0;margin-right:18px;"
        >

          <input
            type="radio"
            id="metricChoice1"
            name="contact"
            value="cosine"
            checked="checked"
            @click="updateType('Cosine')"
          >
          <label for="metricChoice1" style="font-weight:normal">Cosine</label>

          <input
            type="radio"
            id="metricChoice2"
            name="contact"
            value="radviz"
            style="margin-left:13px;padding-top:50%;"
            @click="updateType('Projection')"
          >
          <label for="metricChoice2" style="font-weight:normal">Projection</label>

        </form>
      </span>

    </div>
    <div id="nodeGallery">
      <div style="height: 100%; white-space: nowrap; padding-left: 5px;padding-top: 5px">
        
        <div
          v-for="(item, index) in closeNode.slice(0,3)"
          :key="index"
          class="closeNode"
        >
          <img
            :src="'/src/assets' + item.path.slice(1)"
            alt=""
            :pid="item.pid"
            style="height:100%;"
            class="gal_img"
            @click="updateSelectNode(item)"
          >
        </div>
        <br>
        <!-- <div
          v-for="(item, index) in closeNode.slice(5,10)"
          :key="index"
          class="closeNode"
        >
          <img
            :src="'/src/assets' + item.path.slice(1)"
            alt=""
            :pid="item.pid"
            style="height:100%;"
            @click="updateSelectNode(item)"
          >
        </div> -->
        <div
          v-for="(item, index) in closeNode.slice(3,6)"
          :key="index"
          class="closeNode"
        >
          <img
            :src="'/src/assets' + item.path.slice(1)"
            alt=""
            :pid="item.pid"
            style="height:100%;"
            class="gal_img"
            @click="updateSelectNode(item)"
          >
        </div>
        <br>
        <div
          v-for="(item, index) in closeNode.slice(6,9)"
          :key="index"
          class="closeNode"
        >
          <img
            :src="'/src/assets' + item.path.slice(1)"
            alt=""
            :pid="item.pid"
            style="height:100%;"
            class="gal_img"
            @click="updateSelectNode(item)"
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      viewName: "Visualization Gallery",
      closeNode: []
    }
  },
  methods: {
    /**
     * @description: set the closeNode
     * @param {Array} data picture information from visView.vue
     * @return {*}
     */    
    setCloseNode (data) {
      // console.log(data);
      this.closeNode = data;
    },
    /**
     * @description: change the gallery type 
     * @param {String} data Cosine / Projection
     * @return {*}
     */    
    updateType (data) {
      // console.log(data)
      this.$emit('updateGType', data);
    },
    /**
     * @description: select a picture and upload information
     * @param {*} data data bound to the picture
     * @return {*}
     */    
    updateSelectNode (data) {
      this.$emit("updateSelectNode", data);
    }
  }
}
</script>

<style>
#nodeGallery {
  overflow-x: scroll;
  overflow-y: hidden;
  width: 100%;
  height: calc(100% - 30px);
}
.closeNode {
  /* position: absolute; */
  /* width: 20%; */
  /* height: calc(100% - 20px); */
  /* height: calc(45% - 10px); */
  height: calc(30% - 10px);
  /* padding-bottom: 50%; */
  /* position: fixed; */
  margin-top: 10px;
  margin-bottom: 10px;
  border: solid 1px rgba(0, 0, 0, 0.5);
  margin-left: 5px;
  margin-right: 5px;
  /* float: left; */
  white-space: normal;
  display: inline-block;
  /* display: flex; */
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>