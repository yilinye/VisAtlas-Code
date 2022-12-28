<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-05-01 00:16:20
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div>
    <div id="titleBar" style="transform:translate(0,-1px);">
      {{ viewName }}
    </div>
    <div id="panel" style="font-size:13px;">
      <span style="font-weight: bold;font-size:16px;">Embedding model:</span>&nbsp;&nbsp;&nbsp;&nbsp;ResNet50
      <br>
      <span style="font-weight: bold;font-size:16px;">Choose a dataset:</span>
      <br>
      <form>
        <div style="display:inline-block">
          <input
            type="radio"
            id="cbox1"
            name="dataset"
            value="Beagle"
            @click="chooseFile('/src/visData/Beagle reorder.csv')"
            source="/src/visData/Beagle reorder.csv"
          >
          Beagle
        </div>

        <div style="margin-left:10px;display:inline-block">
          <input
            type="radio"
            id="cbox2"
            name="dataset"
            value="Vis30k"
            @click="chooseFile('/src/visData/vis30k reorder.csv')"
            source="/src/visData/vis30k reorder.csv"
          >
          VIS30K
        </div>

        <div style="margin-left:10px;display:inline-block">
          <input
            type="radio"
            id="cbox3"
            name="dataset"
            value="Data2Vis"
            @click="chooseFile('/src/visData/data2vis reorder.csv')"
            source="/src/visData/data2vis reorder.csv"
            checked
          >
          Data2Vis
        </div>

        <input
          type="submit"
          value="Submit"
          style="display:none"
          id="dataset submit"
        >
      </form>
      <!-- <br> -->
      <span style="font-weight: bold;font-size:16px">Upload an image:</span> &nbsp;
      <button onclick="upload.click()">Select Image</button>
      <div style="display:none;">
        <form
          action=""
          method="post"
          enctype='multipart/form-data'
        >
          <input
            type="file"
            name="image"
            id="upload"
            style="display:none;width:200px;height:200px"
            @change="chooseImage($event)"
          />
        </form>
        <!-- <form id="uploadForm" :onsubmit="PostData(event)" style="display:inline;margin-left:8px;">


					<input type="file" name="image" id="pic_img" style="display:none" @change="chooseFile($event)">
					<input type="submit" value="upload" id="img_submit" style="display:none">

					<label for="datasets" style="margin-left:11px;margin-top:11px">Upload an image:</label> <input
						type="button" value="Select image" id="button" style="margin-top:0;margin-left:23px">

				</form> -->
      </div>

    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import { dataService } from '../service';
export default {
  // created() {
  //   this.chooseFile(this.fileName);
  // },
  data () {
    return {
      viewName: "Model",
      fileName: "/src/visData/Beagle reorder.csv",
      imageUrl: '',
      typeName: ["Area", "Bar", "Circle", "Diagram", "Line", "Map", "Matrix", "Net", "Point", "Table", "Word"]
    }
  },
  methods: {
    chooseFile: function (e) {
      this.fileName = e;
      this.$emit('getFilePath', e);
    },

    /**
     * @description: clear brush 
     * @param {*} e event
     * @return {*}
     */    
    clearBrush: function (e) {
      d3.selectAll('.brush_rect').remove();
      // if (d3.select("#cir"+d.pid).attr("")
      d3.selectAll('.rad_cir').attr('r', d=>{ return d.show == 'true' ? 2 : 0;});
      d3.selectAll('.selrect').attr('height',0)
      d3.select("#drawn").attr("d",null);
      d3.select("#loop_close").attr("d",null);
    },

    /**
     * @description: query and show picture
     * @param {*} e event
     * @return {*}
     */    
    chooseImage: function (e) {
      // console.log(e);
      // d3.select("#img_submit").click();
      var file = e.target.files[0]
      var reader = new FileReader()
      var that = this
      reader.readAsDataURL(file)
      reader.onload = function (e) {
        // console.log("file name", file.name);
        // console.log("file type", file.type);
        // console.log("this.result", this.result)
        // that.imageUrl = '/src/assets/static/uploadImage/' + file.name;
        that.imageUrl = this.result;
        let pw = document.getElementById("isChoose").offsetWidth;
        let ph = document.getElementById("isChoose").offsetHeight;
        // console.log(ph, pw);
        
        // if (ph * 2 > pw)
        //   d3.select("#nodePic").attr("style", 'width: 95%; border: solid 1px; transform: translate(0,0)');
        // else
        //   d3.select("#nodePic").attr("style", 'height: 95%; border: solid 1px; transform: translate(0,0)');
        d3.select("#nodePic").attr("style", 'height: 150px; border: solid 1px; transform: translate(0,0)');
        d3.select("#nodePic").attr("src", that.imageUrl);

      }
      dataService.queryImg({ "img_path": file.name }, data => {
        let d = data.data;
        for (let i in that.typeName) {
          document.getElementById(that.typeName[i] + 'Table').innerHTML = Math.round((d[that.typeName[i].toLowerCase()] * 100000)) / 100000;
        }
        d.pid = -1;
        // console.log(d);
        this.$emit("queryNode", d);
      })
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
  margin-bottom: 10px;
}
</style>