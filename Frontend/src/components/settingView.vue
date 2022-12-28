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
    <div id="panel">
  <div id="Sampling" style="height: 30px; width: 260px; margin-right:15px">
  <button style="font-size: 14px;margin-top: 8px;display: none;" @click="resample($event)" ref="sample">Resample</button>
   
  <span style="margin-left:0px;font-weight: bold">Sample Radius: </span><span style="margin-left:25px">0</span>
  <input style="width: 43px" type="range" min="0" max="15" value="0"
                 class="trigger" id="sampleRange" @change="$refs.sample.click()">
  <span>15</span>
  </div>
  <div id="Ordering" style="height: 30px; width: 260px; margin-right:15px">
  <span style="font-weight: bold">Optimal Ordering: </span>
  <button style="margin-top: 0px; font-size: 14px;display: none;" @click="switchOrder($event)" ref="order">Shuffle Order</button>
  <button style="margin-left:3px; font-size: 14px;display: none;" @click="optimalOrder($event)">Optimal Order</button>
  <span style="margin-left:5px">Single</span>
  <input style="width: 30px" type="range" min="0" max="1" value="0"
                 class="trigger" id="optimalOption" @change="$refs.order.click()">
  <span>All</span>
  </div> 
  <!-- <br> -->
  <!-- <button style="font-size: 14px;margin-top: 8px" @click="clearBrush($event)">Clear Brush</button>
  <input style="width: 30px" type="range" min="0" max="1" value="0"
                 class="trigger" id="optimalOption" @change="$refs.order.click()"> -->
  <span style="margin-left:0px;font-weight: bold">Overview Mode: </span><input type="radio" id="Selection" name="drone" value="huey"
             checked>
      <label for="huey">Selection</label>
  <input type="radio" id="Zoom" name="drone" value="dewey">
      <label for="dewey">Zoom</label>
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
      viewName: "Settings",
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
        if (ph * 2 > pw)
          d3.select("#nodePic").attr("style", 'width: 95%; border: solid 1px; transform: translate(0,0)');
        else
          d3.select("#nodePic").attr("style", 'height: 95%; border: solid 1px; transform: translate(0,0)');
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