<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 22:14:49
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div id="titleBar">
    {{ viewName }}
  </div>
  <div id="panel">
    <span style="font-weight: bold;">Embedding model:</span>&nbsp;&nbsp;&nbsp;&nbsp;ResNet50
    <br>
    <span style="font-weight: bold;">Choose a dataset:</span>
    <br>
    <form>
					<div style="display:inline-block">
						<input type="radio" id="cbox1" name="dataset" value="Beagle" @click="chooseFile('../visData/Beagle reorder.csv')" checked
							source="../visData/Beagle reorder.csv">
						Beagle
          </div>

					<div style="margin-left:10px;display:inline-block">
						<input type="radio" id="cbox2" name="dataset" value="Vis30k" @click="chooseFile('../visData//vis30k reorder.csv')" source="../visData/vis30k reorder.csv">
						VIS30K
          </div>

					<div style="margin-left:10px;display:inline-block">
						<input type="radio" id="cbox3" name="dataset" value="Data2Vis" @click="chooseFile('../visData/data2vis reorder.csv')" source="../visData/data2vis reorder.csv">
						Data2Vis
          </div>

					<input type="submit" value="Submit" style="display:none" id="dataset submit">
				</form>
    <!-- <br> -->
    <span style="font-weight: bold;">Upload an image:</span> &nbsp;
    <button>Select Image</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      viewName: "Model",
      fileName: "../visData/Beagle reorder.csv"
    }
  },
  methods: {
    chooseFile: function(e) {
      this.fileName = e;
      this.$emit(getFilePath, this.fileName);
    }
  }
}
</script>

<style>
#panel {
  /* text-align: center; */
  font-size: 15px;
  line-height: 2rem;
  margin-top: 10px;
  margin-left: 15px;
}
</style>