<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-05-01 00:24:11
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div id="titleBar">
    {{ viewName }}
  </div>
  <div
    style="height: 27%; width: 8%; background-color: #F2F7F7; position: absolute; bottom: 49%; left:3px; border-radius:10px">
    <span style="margin-left:19%; color: #739998;font-weight: bold ;text-decoration: underline">View</span>
    <div id="lassoback"
      onclick="document.getElementById('lassoback').style.backgroundColor='#3C6865'; document.getElementById('zoomback').style.backgroundColor='#8CAFAE'"
      style="width:47px; height: 47px; margin-top:3px;margin-left:13%; background-color: #3C6865;border-radius:10px">
      <img src="../assets/Logo/lasso.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.selection.click()">
    </div>
    <span style="margin-left:15%; color: #8CAFAE; font-size:14px">Select</span>
    <div id="zoomback"
      onclick="if (document.getElementById('zoomback').style.backgroundColor!='#3C6865') document.getElementById('zoomback').style.backgroundColor='#3C6865'; document.getElementById('lassoback').style.backgroundColor='#8CAFAE'"
      style="width:47px; height: 47px; margin-top:2px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/zoom.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.zoom.click()">
    </div>
    <span style="margin-left:17%; color: #8CAFAE; font-size:14px">Zoom</span>
    <div style="width:47px; height: 47px; margin-top:2px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/clear.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.clear.click()">
    </div>
    <span style="margin-left:22%; color: #8CAFAE; font-size:14px">Clear</span>
  </div>

  <div
    style="height: 27%; width: 8%; background-color: #F2F7F7; position: absolute; bottom: 21%; left:3px; border-radius:10px">
    <span style="margin-left:6%; color: #739998;font-weight: bold ;text-decoration: underline">Sample</span>
    <div id="gridback"
      style="width:47px; height: 47px; margin-top:3px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/grid1.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.grid.click()">
    </div>
    <span style="margin-left:27%; color: #8CAFAE; font-size:14px">Grid</span>
    <div id="poissonback"
      style="width:47px; height: 47px;  margin-top:2px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/disk.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.poisson.click()">
    </div>
    <span style="margin-left:30%; color: #8CAFAE; font-size:14px">Disk</span>
    <div id="fpsback"
      style="width:47px; height: 47px;  margin-top:2px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/chart-scatter.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.FPS.click()">
    </div>
    <span style="margin-left:8%; color: #8CAFAE; font-size:14px">Random</span>
  </div>

  <div
    style="height: 19%; width: 8%; background-color: #F2F7F7; position: absolute; bottom: 1%; left:3px; border-radius:10px">
    <span style="margin-left:17%; color: #739998;font-weight: bold ;text-decoration: underline">Order</span>
    <div id="singleback"
      onclick="document.getElementById('singleback').style.backgroundColor='#3C6865'; document.getElementById('allback').style.backgroundColor='#8CAFAE'"
      style="width:47px; height: 47px; margin-top:1px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/ordering-single.svg" alt=""
        style="width: 70%; height=auto;margin-left:15%;margin-top:15%" @click="$refs.single.click()">
    </div>
    <span style="margin-left:20%; color: #8CAFAE; font-size:14px">Single</span>
    <div id="allback"
      onclick="document.getElementById('allback').style.backgroundColor='#3C6865'; document.getElementById('singleback').style.backgroundColor='#8CAFAE'"
      style="width:47px; height: 47px; margin-top:2px;margin-left:13%; background-color: #8CAFAE;border-radius:10px">
      <img src="../assets/Logo/ordering-all.svg" alt="" style="width: 70%; height=auto;margin-left:15%;margin-top:15%"
        @click="$refs.all.click()">
    </div>
    <span style="margin-left:33%; color: #8CAFAE; font-size:14px">All</span>
  </div>

  <div id="mainViewPic" style="height: 80%; width: 90%;margin-left:11%">
    <div style="display:none">
      <span style="margin-left:0px;font-weight: bold">Sampling</span><input type="radio" id="Grid" name="drone"
        value="huey" checked ref="grid" @change="$refs.sample.click()">
      <label for="huey">Grid</label>
      <input type="radio" id="Poisson" name="drone" value="dewey" ref="poisson" @change="$refs.sample.click()">
      <label for="dewey">Poisson</label>
      <input type="radio" id="FPS" name="drone" value="d" ref="FPS" @change="$refs.sample.click()">
      <label for="dewey">FPS</label>
      <span style="margin-left:8px;font-weight: bold">Overview: </span><input type="radio" ref="selection"
        id="Selection" name="drone1" value="huey" checked>
      <label for="huey">Selection</label>
      <input type="radio" id="Zoom" ref="zoom" name="drone1" value="dewey">
      <label for="dewey">Zoom</label>
      <span style="margin-left:8px;font-weight: bold">Overview: </span><input type="radio" id="Selection" name="drone3"
        value="huey" checked>
      <label for="huey">Clear</label>
      <!-- <button id="single_order" style="margin-top: 0px; font-size: 14px;" @click="switchOrder($event)" ref="Single">Shuffle Order</button>
  <button id="all_order" style="margin-left:3px; font-size: 14px;" @click="optimalOrder($event)" ref="All">Optimal Order</button> -->
      <!-- <span style="margin-left:8px;font-weight: bold">Optimal Ordering: </span><input type="radio" @change="switchOrder($event)" ref="Single" id="Single" name="drone2" value="huey"
             checked>
      <label for="huey">Single</label>
  <input type="radio" ref="All" id="All" @change="optimalOrder($event)" name="drone2" value="dewey">
      <label for="dewey">All</label> -->

    </div>
    <!-- <button style="font-size: 14px;margin-top: 8px;" @click="resample($event)" ref="sample">Resample</button> -->




  </div>
  <!-- <span style="margin-left:8px;font-weight: bold">Optimal Ordering: </span><input type="radio" @click="$refs.single.click()" ref="Single" id="Single" name="drone2" value="huey"
             checked>
      <label for="huey">Single</label>
  <input type="radio" ref="All" id="All" @click="$refs.all.click()" name="drone2" value="dewey">
      <label for="dewey">All</label> -->
  <div id="mainViewBottom" style="height: 20%; width: 100%;">
    <div id="mainViewWidget" style="display: inline-block;"></div>
    <button style="font-size: 14px;margin-top: 8px;display: none;" @click="resample($event)"
      ref="sample">Resample</button>
    <button style="margin-top: 0px; font-size: 14px;display: none;" @click="switchOrder($event)" ref="single">Shuffle
      Order</button>
    <button style="margin-left:3px; font-size: 14px;display: none;" @click="optimalOrder($event)" ref="all">Optimal
      Order</button>

   
    <button style="font-size: 14px;margin-top: 8px;display:none" ref="clear" @click="clearBrush($event)">Clear
      Brush</button>
  </div>

</template>

<script>
import * as d3 from 'd3';
import classifyPoint from 'robust-point-in-polygon';
import { zoom } from "https://cdn.skypack.dev/d3-zoom@3";
// this is not a usual lasso. npm install skokenes/d3-lasso
// import * as d3Lasso from 'd3-lasso';
var lasso = 0
var positionfixed = -1
var isRedraw = false;
var DAorder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let sample_radius = 0;
var mousepreX = 0;
var mousepreY = 0;
var nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
var switchState=0;
var countData=[];
for (let i=0;i<11;i++)
{
  countData.push({"class":nameorder1[i],"count":0})
}
function shuffleArray(array) {
  let curId = array.length;
  // There remain elements to shuffle
  while (0 !== curId) {
    // Pick a remaining element
    let randId = Math.floor(Math.random() * curId);
    curId -= 1;
    // Swap it with the current element.
    let tmp = array[curId];
    array[curId] = array[randId];
    array[randId] = tmp;
  }
  return array;
}
// DAorder=shuffleArray(DAorder);
export default {
  name: 'mainView',
  mounted() {
    this.createSVG();
    this.drawMain(this.fileP.filePath, this.dimensions, DAorder);
    // this.setupLasso();
  },
  inject: ['fileP'],
  data() {
    return {
      viewName: "Embedding Overview",
      typeName: ["Matrix", "Table", "Word", "Circle", "Map", "Line", "Area", "Bar", "Net", "Point", "Diagram"],
      colormap: { "circle": "#4A80CE", "point": "#FF931D", "net": "#42B287", "line": "#E5CD3C", "area": "#FF6224", "bar": "#A9DB63", "map": "#C192EA", "matrix": "#1C9AB7", "table": "#FF9896", "word": "#FFB839", "diagram": "#0ED88F" },
      dimensions: ['circle', 'map', 'line', 'area', 'bar', 'net', 'point', 'diagram', 'matrix', 'table', 'word'],
      levelCluster: {
        "Beagle": ['Circle', 'Map', 'Line', 'Area', 'Bar', 'Net', 'Point', 'Diagram', 'Matrix', 'Table', 'Word'],
        "VIS": ["Map", "Circle", "Bar", "Point", "Line", "Diagram", "Matrix", "Net", "Area", "Table", "Word"],
        "Data": ["Area", "Line", "Bar", "Point", "Circle", "Map", "Matrix", "Net", "Table", "Word", "Diagram"],
      },
      wordDis: [41, 15, 26, 18, 25, 16, 29, 24, 24, 50, 88],
      chartRadius: 0,
      mainHeight: 0,
      mainWidth: 0,
      distanceType: "Cosine", //! init computing method
      selectNode: 0, //! the selected node data
      processedData: null //! the processed data
    }
  },
  methods: {
    /**
     * @description: create a svg
     * @param {*}
     * @return {*}
     */
    createSVG() {
      const mainHeight = document.getElementById('mainViewPic').offsetHeight;
      const mainWidth = document.getElementById('mainViewPic').offsetWidth;
      this.mainHeight = mainHeight;
      this.mainWidth = mainWidth;
      this.chartRadius = Math.min(this.mainWidth - 100, this.mainHeight) / 2 - 70;
      d3.select("#mainViewPicSvg").remove();
      d3.select("#mainViewPic")
        .append('svg')
        .attr('id', 'mainViewPicSvg')
        .attr('height', mainHeight)
        .attr('width', mainWidth);
    },

    /**
     * @description: draw side widget
     * @param {Array} allType: Feature Group
     * @return {*}
     */
    drawSideWidget(allData1, DAorder) {
      d3.select("#sideWidget").remove();
      let nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
      let widget = d3.select("#mainViewWidget")
        .append('svg')
        .attr('id', 'sideWidget')
        .style('overflow', 'visible')
        .attr('transform', 'translate(100,0)')

      let _this = this;
      let switchOrder2=this.switchOrder2;
      let counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      let total = 0
      if (allData1.length>11)
      {
        for (let i = 0; i < allData1.length; i++) {
          let idx = nameorder1.indexOf(allData1[i]['class'].toLowerCase());
          counts[idx] = counts[idx] + 1;
          total = total + 1;
        }
        for (let i = 0; i < countData.length; i++) {
          let idx = nameorder1.indexOf(countData[i]['class'].toLowerCase());
          countData[i]['count'] = counts[idx];
        }
      }
      else {
        for (let i = 0; i < allData1.length; i++) {
          let idx = nameorder1.indexOf(allData1[i]['class'].toLowerCase());
          counts[idx] = allData1[i]['count'];
          total = total + counts[idx];
        }
      }
      let colorMap = this.colormap;
      let group = widget.append('g');
      let lines = [0, 0.25, 0.5, 0.75]

      // let Wdrag = d3.drag()
      //   .on('start', WdragStarted)
      //   .on('drag', Wdragged)
      //   .on('end', WdragEnded);
    var startx=0
    var starty=0
    var rectx=0
    var recty=0
    var drag_handler = d3.drag()
    .on("start", Wdragstarted)
    .on("drag", Wdragged)
    .on("end", Wdragended);

    function Wdragstarted (event, d){
          rectx=d3.select(this).attr("x")
          recty=d3.select(this).attr("y")
          startx=event.x;
          starty=event.y;
    }
    function Wdragged (event, d){
      // d.x=event.x;
      // d.y=event.y;
      d3.select(this).attr("x", event.x).attr("y", event.y);
      let num=d3.select(this).attr("num");
      let i=Number(d3.select(this).attr("i"));
      d3.select("#"+"Widgettext"+num).attr("x", event.x-165).attr("y", event.y+38+ 200 * counts[DAorder[i]] / total );
      d3.select("#"+"widgetCount"+num).attr("x", event.x-165).attr("y", event.y-20 );
    } 
    function Wdragended (event, d){
      if (Math.pow(event.x-startx,2)>64){
      // d.x=event.x;
      // d.y=event.y;
      // d3.select(this).attr("x", event.x).attr("y", event.y);
      let name=d3.select(this).attr("num");
      // let i=Number(d3.select(this).attr("i"));
      // d3.select("#"+"Widgettext"+num).attr("x", event.x-165).attr("y", event.y+38+ 200 * counts[DAorder[i]] / total );
      // d3.select("#"+"widgetCount"+num).attr("x", event.x-165).attr("y", event.y-20 );
      let close_name=-1
      let min_dis;
      let insert_direction="none"
      if (name!=nameorder1[DAorder[10]])
      {
         min_dis=Math.pow(Number(d3.select(this).attr("x"))-Number(d3.select("#widget"+nameorder1[DAorder[10]]).attr("x")),2)
      }
      else{
         min_dis=Math.pow(Number(d3.select(this).attr("x"))-Number(d3.select("#widget"+nameorder1[DAorder[0]]).attr("x")),2)
      }
      
      for (let i=0;i<11;i++)
      {
         
        let dis=Math.pow(Number(d3.select(this).attr("x"))-Number(d3.select("#widget"+nameorder1[DAorder[i]]).attr("x")),2)
        if(nameorder1[DAorder[i]]!=name && dis<min_dis)
         {
           min_dis=dis
           close_name=nameorder1[DAorder[i]]
           if(Number(d3.select(this).attr("x"))-Number(d3.select("#widget"+nameorder1[DAorder[i]]).attr("x"))<0)
           {
            insert_direction="left"
           }
           else{
            insert_direction="right"
           }
         }
      }
      let tempOrder=[]
      let source_pos;
      let target_pos;
      for (let i=0;i<11;i++){
          if (nameorder1[DAorder[i]]==name)
          {
            source_pos=DAorder[i]
          }
          if (nameorder1[DAorder[i]]==close_name)
          {
            target_pos=DAorder[i]
          }
      }
      console.log("preorder")
      console.log(name)
      console.log(DAorder)
      for (let i=0;i<11;i++)
      {
        if (nameorder1[DAorder[i]]!=name && nameorder1[DAorder[i]]!=close_name)
        {
          tempOrder.push(DAorder[i])
        }
        else if (nameorder1[DAorder[i]]==close_name)
        {
           if (insert_direction=="left")
           {
            tempOrder.push(source_pos)
            tempOrder.push(DAorder[i])
           }
           else
           {
            tempOrder.push(DAorder[i])
            tempOrder.push(source_pos)
           }
        }
      }
      DAorder=tempOrder;
      console.log("postorder")
      console.log(DAorder)
      switchState=1
      switchOrder2(DAorder);
      document.getElementById('allback').style.backgroundColor='#8CAFAE'; document.getElementById('singleback').style.backgroundColor='#8CAFAE'
      // _this.drawMain(_this.fileP.filePath, _this.dimensions, DAorder);
      // isRedraw = true;
      }
      else{
        let name=d3.select(this).attr("num");
        d3.selectAll('.rad_cir')
            .attr('r', (d,i) => {
              // if(i%100==0)
              // {console.log(d)}
              return d.class == name ? 2 : 0;
            })
        d3.select(this).attr("x", rectx)
        d3.select(this).attr("y", recty)
        d3.selectAll(".widgetRect").attr("stroke","none")
        d3.select(this).attr("stroke","black")
        d3.select("#"+"Widgettext"+name).attr("x", rectx-165).attr("y", recty+38+ 200 * counts[DAorder[i]] / total );
        d3.select("#"+"widgetCount"+name).attr("x", rectx-165).attr("y", recty-20 );
      }
    } 
    group.selectAll(".widgetRect")
        .data(DAorder)
        .enter()
        .append('rect')
        .attr('class', 'widgetRect')
        .attr('global_ratio', function (d, i) { return counts[DAorder[i]] / total })
        .attr('id', function (d, i) { return "widget" + nameorder1[DAorder[i]] })
        .attr('num',(d,i)=>{return nameorder1[DAorder[i]]})
        .attr('i',(d,i)=>{return i})
        .attr("height", function (d, i) { return 200 * counts[DAorder[i]] / total })
        .attr("width", 30)
        .attr("x", function (d, i) { return 75 + 20 - 30 + 55 * i })
        .attr("y", function (d, i) { return 130 - 200 * counts[DAorder[i]] / total })
        .style("fill", function (d, i) { return colorMap[nameorder1[DAorder[i]]] })
        .call(drag_handler)
        
        
      // drag_handler(Widgets);


      group.selectAll(".widgetText")
        .data(DAorder)
        .enter()
        .append('text')
        .attr('class', 'widgetText')
        .attr('id', (d,i)=>{return 'Widgettext'+nameorder1[DAorder[i]]})
        .attr("x", function (d, i) { return 55 * i - 80 + 10 - 30 })
        .attr("y", function (d, i) { return 168 })
        .text(function (d, i) { return nameorder1[DAorder[i]][0].toUpperCase() + nameorder1[DAorder[i]].slice(1) })
        .style("text-anchor", "middle")
        .style("font-size", "14px")
        .attr("transform", (d, i) => { return 'translate(180,-22)' })

      group.selectAll(".widgetCount")
        .data(DAorder)
        .enter()
        .append('text')
        .attr('class', 'widgetCount')
        .attr('id', function (d, i) { return "widgetCount" + nameorder1[DAorder[i]] })
        .attr('global_num', function (d, i) { return counts[DAorder[i]] })
        .attr("x", function (d, i) { return 55 * i - 80 + 10 - 30 })
        .attr("y", function (d, i) { return 110 - 200 * counts[DAorder[i]] / total })
        .text(function (d, i) { return counts[DAorder[i]] })
        .style("text-anchor", "middle")
        .style("font-size", "14px")
        .attr("transform", (d, i) => { return 'translate(180,14)' })


    },
    /**
     * @description: draw pie chart and text
     * @param {Array} allType: Feature Group
     * @return {*}
     */
    drawLegend(allType, DAorder) {
      d3.select("#mainLegend").remove();
      let legend_g = d3.select("#mainViewPicSvg")
        .append('g')
        .attr('id', 'mainLegend')
        .attr('transform', `translate(${this.mainWidth / 2}, ${this.mainHeight / 2})`);
      
      let legData = new Array();
      let allType1 = new Array();
      let _this = this;
      let switchOrder2=this.switchOrder2;
      let counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      let total = 0
      //let DAorder2=[DAorder[8],DAorder[9],DAorder[10],DAorder[0], DAorder[1], DAorder[2],DAorder[3],DAorder[4],DAorder[5],DAorder[6],DAorder[7]];
      let nameorder2 = new Array();
      var nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
      for (let i = 0; i < allType.length; ++i) {
        nameorder2.push(nameorder1[DAorder[i]])
      }
      for (let i = 8; i < allType.length + 8; ++i) {
        legData.push(20);
        allType1.push(nameorder2[i % 11])
      }
      // drag fubctions
      var Ldrag_handler = d3.drag()
      .on("start", Ldragstarted)
      .on("drag", Ldragged)
      .on("end", Ldragended);
      var Lstartx=0
      var Lstarty=0
      var Lx=0
      var Ly=0
      function Ldragstarted (event, d){
            Lx=d3.select(this).attr("x")
            Ly=d3.select(this).attr("y")
            let name=d3.select(this).attr("num");
            Lstartx=event.x;
            Lstarty=event.y;
            // d3.select(this).attr("transform",`rotate(-214.5)`)
            d3.select("#use").attr("xlink:href","#mid_pie"+name)
      }
      function Ldragged (event, d){

        // d3.select(this).attr("x", event.x).attr("y", event.y);
        // let num=d3.select(this).attr("num");
        // let i=Number(d3.select(this).attr("i"));
        // d3.select("#"+"Legendtext"+num).attr("x", event.x-165).attr("y", event.y);
        let cos=(event.x*Lstartx+event.y*Lstarty)/(Math.sqrt(event.x*event.x+event.y*event.y)*Math.sqrt(Lstartx*Lstartx+Lstarty*Lstarty))
        let angle=Math.acos(cos)
        let degree=180*angle/Math.PI
        if (event.x*(-Lstarty)+event.y*(Lstartx)>0)
        {
          degree=degree
        }
        else
        {
          degree=360-degree
        }
        d3.select(this).attr("transform","rotate("+(degree-114.5)+")").attr('fill-opacity', 1)

      } 
      function Ldragended (event, d){
        if (Math.pow(event.x-Lstartx,2)+Math.pow(event.y-Lstarty,2)>128){

        let name=d3.select(this).attr("num");
        let cos=(event.x*Lstartx+event.y*Lstarty)/(Math.sqrt(event.x*event.x+event.y*event.y)*Math.sqrt(Lstartx*Lstartx+Lstarty*Lstarty))
        let angle=Math.acos(cos)
        let degree=180*angle/Math.PI
        if (event.x*(-Lstarty)+event.y*(Lstartx)>0)
        {
          degree=degree
        }
        else
        {
          degree=360-degree
        }
        let degree_step=Math.floor(degree/(360/11))
        let current_pos;
        for (let i=0;i<DAorder.length;i++)
        {
          if (nameorder1[DAorder[i]]==name)
          {
             current_pos=i
          }
        }
        let new_pos=(degree_step+current_pos)%11


        let tempOrder=[]
        if (new_pos!=current_pos)
        {
            for (let i=0;i<11;i++)
            {
                tempOrder.push(DAorder[i])
            }
            let temp=tempOrder[current_pos]
            tempOrder[current_pos]=tempOrder[new_pos]
            tempOrder[new_pos]=temp
            DAorder=tempOrder;
            console.log("postorder")
            console.log(DAorder)
            switchState=1
            switchOrder2(DAorder);
            document.getElementById('allback').style.backgroundColor='#8CAFAE'; document.getElementById('singleback').style.backgroundColor='#8CAFAE'
        }
        else
        {
          switchState=1
          switchOrder2(DAorder);
        }
        // _this.drawMain(_this.fileP.filePath, _this.dimensions, DAorder);
        // isRedraw = true;
        }
        else{
          let name=d3.select(this).attr("num");
        }
      } 
      console.log(allType1);
      let pie = d3.pie();
      let inner = this.chartRadius;
      let outer = this.chartRadius + 25;
      let arc = d3.arc()
        .innerRadius(inner)
        .outerRadius(outer);

      let pieData = pie(legData);
      for (let i in pieData) {
        pieData[i]['type'] = allType1[i];
      }
      
      let Lgroup=legend_g.append('g')
        .attr('id', 'leg_pie')
        // .attr('transform', `translate(${this.mainWidth / 2}, ${this.mainHeight / 2})`)
      
      Lgroup.selectAll('#pie_g')
        .attr('id', 'pie_g')
        .data(pieData)
        .enter()
        .append('path')
        .attr('id', d => 'mid_pie' + d.type)
        .attr('num', d => d.type)
        // .attr("transform", `rotate(-24.5)`)
        .attr("transform", `rotate(-114.5)`)
        .attr("stroke", 'white')
        .attr("stroke-width", 1)
        .attr("stroke-linejoin", 'round')
        .attr('d', d => {
          console.log(d);
          return arc(d);
        })
        .attr('fill', d => {
          return this.colormap[d['type'].toLowerCase()];
        })
        .attr('fill-opacity', 0.7)
        .call(Ldrag_handler);

        Lgroup.append('use').attr("id","use").attr("xlink:href","#mid_pie"+pieData[10].type)

      // draw text and line
      let textMap = new Array(allType.length);
      let radius = 2 * Math.PI / allType.length;
      for (let i = 0; i < allType.length; ++i) {
        //var ID=DAorder2.indexOf(i);
        textMap[i] = {
          type: allType1[i],
          x1: (inner - 3) * Math.sin(radius * (-i + 6) - 24.5 * Math.PI / (180 * 3) + Math.PI / 2),
          y1: (inner - 3) * Math.cos(radius * (-i + 6) - 24.5 * Math.PI / (180 * 3) + Math.PI / 2),
          x2: (inner + 3) * Math.sin(radius * (-i + 6) - 24.5 * Math.PI / (180 * 3) + Math.PI / 2),
          y2: (inner + 3) * Math.cos(radius * (-i + 6) - 24.5 * Math.PI / (180 * 3) + Math.PI / 2),
          x: (outer + 11) * Math.sin(radius * (-i + 6) - 24.5 * Math.PI / (180 * 3) + Math.PI / 2),
          y: (outer + 11) * Math.cos(radius * (-i + 6) - 24.5 * Math.PI / (180 * 3) + Math.PI / 2),
          cnt: i
        }
      }

      let text_g = legend_g.append('g')
        .attr('id', 'leg_line')
        // .attr('transform', `translate(${this.mainWidth / 2}, ${this.mainHeight / 2})`)
        .selectAll('#mid_line')
        .data(textMap)
        .enter()
      text_g.append('line')
        .attr('id', d => 'mid_line' + d.type)
        .attr('x1', d => {
          return d.x1
        })
        .attr('y1', d => d.y1)
        .attr('x2', d => d.x2)
        .attr('y2', d => d.y2)
        .attr('stroke-width', 1)
        .attr('stroke', d3.rgb(120, 120, 120));

      // text_g.append('text')
      //   .attr('id', d => 'mid_text' + d.cnt)
      //   .attr('x', d => d.x)
      //   .attr('y', d => d.y)
      //   .attr('fill', d => {
      //     return this.colormap[d.type.toLowerCase()]
      //   })
      //   .attr('text-anchor', d => {
      //     if (d.cnt == 0 || d.cnt == 6)
      //       return 'middle'
      //     if (d.cnt > 0 && d.cnt < 6)
      //       return 'start';
      //     else
      //       return 'end'
      //   })
      //   .attr('font-size', '25px')
      //   .attr('font-weight', 'bold')
      //   .attr('dx', d => {
      //     if (d.cnt == 0 || d.cnt == 6)
      //       return -this.wordDis[d.cnt] + 'px';
      //     if (d.cnt > 0 && d.cnt < 6)
      //       return 0;
      //     else
      //       return -this.wordDis[d.cnt] + 'px'
      //   })
      //   .attr('dy', '0.2em')
      //   .text(d => d.type[0].toUpperCase())

      //uncolor
      text_g.append('text')
        .attr('id', d => 'mid_text' + d.cnt)
        .attr('x', d => d.x)
        .attr('y', d => d.y)
        .attr('fill', d => {
          return 'black'
        })
        //before change order
        // .attr('text-anchor', d => {
        //   if (d.cnt == 0 || d.cnt == 6)
        //     return 'middle'
        //   if (d.cnt > 0 && d.cnt < 6)
        //     return 'start';
        //   else
        //     return 'end'
        // })
        .attr('text-anchor', d => {
          if (d.cnt == 3)
            return 'middle'
          if (d.cnt > 3 && d.cnt < 9)
            return 'start';
          else
            return 'end'
        })
        .attr('font-size', '24px')
        .attr('font-weight', 'bold')
        // .attr('dx', d => {
        //   if (d.cnt > 0 && d.cnt < 6)
        //     return this.wordDis[d.cnt] + 'px';
        //   else
        //     return -this.wordDis[d.cnt] + 'px'; 
        // })
        .attr('dy', '0.2em')
        // .text(d => d.type)
        .text(d => d.type[0].toUpperCase() + d.type.slice(1))
      //   .text(d => d.type.slice(1))
      //uncolor

      // text_g.append('text')
      //   .attr('id', d => 'mid_text' + d.cnt)
      //   .attr('x', d => d.x)
      //   .attr('y', d => d.y)
      //   .attr('fill', d => {
      //     return this.colormap[d.type.toLowerCase()]
      //   })
      //   .attr('text-anchor', d => {
      //     if (d.cnt == 0 || d.cnt == 6)
      //       return 'middle'
      //     if (d.cnt > 0 && d.cnt < 6)
      //       return 'start';
      //     else
      //       return 'end'
      //   })
      //   .attr('font-size', '25px')
      //   .attr('font-weight', 'bold')
      //   .attr('dx', d => {
      //     if (d.cnt == 0 || d.cnt == 6)
      //       return -this.wordDis[d.cnt] + 'px';
      //     if (d.cnt > 0 && d.cnt < 6)
      //       return 0;
      //     else
      //       return -this.wordDis[d.cnt] + 'px'
      //   })
      //   .attr('dy', '0.2em')
      //   .text(d => d.type[0].toUpperCase())

      // text_g.append('text')
      //   .attr('id', d => 'mid_text' + d.cnt)
      //   .attr('x', d => d.x)
      //   .attr('y', d => d.y)
      //   .attr('fill', d => {
      //     return 'black'
      //   })
      //   .attr('text-anchor', d => {
      //     if (d.cnt == 0 || d.cnt == 6)
      //       return 'middle'
      //     if (d.cnt > 0 && d.cnt < 6)
      //       return 'start';
      //     else
      //       return 'end'
      //   })
      //   .attr('font-size', '25px')
      //   .attr('font-weight', 'bold')
      //   .attr('dx', d => {
      //     if (d.cnt > 0 && d.cnt < 6)
      //       return this.wordDis[d.cnt] + 'px';
      //   })
      //   .attr('dy', '0.2em')
      //   .text(d => d.type.slice(1))

    },
    /**
     * @description: RadViz process
     * @param {*} data
     * @param {*} dimensions
     * @param {*} dimensionNamesNormalized
     * @return {*}
     */
    addNormalizedValues(data, dimensions, dimensionNamesNormalized) {
      data.forEach(function (d) {
        dimensions.forEach(function (dimension) {
          d[dimension] = +d[dimension];
        });
      });
      var normalizationScales = {};
      dimensions.forEach(function (dimension) {
        normalizationScales[dimension] = d3.scaleLinear().domain(d3.extent(data.map(function (d, i) {
          return d[dimension];
        }))).range([0, 1]);
      });
      data.forEach(function (d) {
        dimensions.forEach(function (dimension) {
          d[dimension + '_normalized'] = normalizationScales[dimension](d[dimension]);
        });
      });
      data.forEach(function (d) {
        let dsum = 0;
        dimensionNamesNormalized.forEach(function (k) {
          dsum += d[k];
        }); // sum
        d.dsum = dsum;
      });
      return data;
    },
    /**
     * @description: RadViz process
     * @param {*} dataE
     * @param {*} dimensionNamesNormalized
     * @param {*} DA
     * @return {*}
     */
    calculateNodePosition(dataE, dimensionNamesNormalized, DA, DAorder) {
      dataE.forEach(function (d) {
        let dsum = d.dsum,
          dx = 0,
          dy = 0;

        dimensionNamesNormalized.forEach(function (k, i) {
          var ID = DAorder.indexOf(i);
          dx += Math.cos(DA[ID]) * d[k];
          dy += Math.sin(DA[ID]) * d[k];
        }); // dx & dy
        d.x0 = dx / dsum;
        d.y0 = dy / dsum;
        d.dist = Math.sqrt(Math.pow(dx / dsum, 2) + Math.pow(dy / dsum, 2)); // calculate r
        d.distH = Math.sqrt(Math.pow(dx / dsum, 2) + Math.pow(dy / dsum, 2)); // calculate r
        d.theta = Math.atan2(dy / dsum, dx / dsum) * 180 / Math.PI;
      });
      return dataE;
    },

    /**
     * @description: switch order 
     * @param {*} e event
     * @return {*}
     */
    switchOrder: function (e) {
      DAorder = shuffleArray(DAorder);
      this.drawMain(this.fileP.filePath, this.dimensions, DAorder);
      isRedraw = true;
    },
    switchOrder2: function (DAorder) {
      // DAorder = shuffleArray(DAorder);
      this.drawMain(this.fileP.filePath, this.dimensions, DAorder);
      isRedraw = true;
    },

    /**
     * @description: optimal order 
     * @param {*} e event
     * @return {*}
     */
    optimalOrder: function (e) {
      DAorder = [0, 2, 7, 5, 3, 1, 9, 10, 4, 6, 8];
      // DAorder=[3,5,10,8,6,4,1,2,7,9,0];
      // [Circle, Line, Diagram, Tree \& Network, Area, Map, Table, Word, Bar, Point, Grid \& Matrix];
      this.drawMain(this.fileP.filePath, this.dimensions, DAorder);
      isRedraw = true;
    },

    /**
     * @description: optimal order 
     * @param {*} e event
     * @return {*}
     */
    resample: function (e) {
      // sample_radius = document.getElementById('sampleRange').value ;
      this.drawMain(this.fileP.filePath, this.dimensions, DAorder);
      isRedraw = true;
    },

    /**
     * @description: clear brush 
     * @param {*} e event
     * @return {*}
     */
    clearBrush: function (e) {
      d3.selectAll('.brush_rect').remove();
      // if (d3.select("#cir"+d.pid).attr("")
      d3.selectAll(".widgetRect").attr("stroke","none")
      d3.selectAll('.rad_cir').attr('r', d => { return d.show == 'true' ? 2 : 0; }).attr("hisShow", "true").attr('state', 'bflasso');


      d3.selectAll('.selrect').attr('height', 0)
      // d3.select("#drawn").attr("d",null);
      // d3.select("#loop_close").attr("d",null);
      d3.selectAll('.lassoDraw').attr("d", null);
      d3.selectAll('.lassoClose').attr("d", null);
      d3.select("#mainScatter_g").attr("afterlasso", "false")
      // d3.select('#cir' + cd.pid).attr("hisShow")
      let nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
      for (let i = 0; i < DAorder.length; i++) {
        let ratio = Number(d3.select("#widget" + nameorder1[DAorder[i]]).attr("global_ratio"))
        d3.select("#widget" + nameorder1[DAorder[i]])
          .attr("height", 290 * ratio)
          .attr("y", 130 - 290 * ratio);
        let num = Number(d3.select("#widgetCount" + nameorder1[DAorder[i]]).attr("global_num"))
        d3.select("#widgetCount" + nameorder1[DAorder[i]])
          .attr("y", 110 - 290 * ratio)
          .text(num)
      }
      // isSecondFiltering=false;
      d3.select("#mainHistogram").attr("second", "false");
      this.removeSelect(this.typeName);
    },

    /**
     * @description: data process
     * @param {Array} fileData file data
     * @param {Array} dimensions Feature Group
     * @return {*}
     */
    getMainData(fileData, dimensions, DAorder) {
      let _this = this;
      let normalizeSuffix = '_normalized';
      let dimensionNamesNormalized = dimensions.map(function (d) {
        return d + normalizeSuffix;
      });
      let nodeAngle = dimensions.map((d, i) => {
        return (i * (Math.PI * 2) / dimensions.length) - Math.PI / 2;
      });
      let allData = fileData;
      allData.forEach((d, i) => {
        d.index = i;
        d.id = i;
        d.pid=i;
        // d.color = this.colormap[d.class.toLowerCase()];
      });
      allData = this.addNormalizedValues(allData, dimensions, dimensionNamesNormalized);
      allData = this.calculateNodePosition(allData, dimensionNamesNormalized, nodeAngle, DAorder);
      let matrixF = {};
      for (let w = 0; w < this.mainWidth / 30; w++) {
        matrixF[w] = {}
        for (let h = 0; h < this.mainHeight / 30; h++) {
          matrixF[w][h] = 0;
        }
      }
      var showpoints = [];
      var showpointX = [];
      var showpointY = [];
      var maxdis = 0;
      var distanceList = [];
      // let sample_radius=10;




      ////Start of farthest point sampling
      // if (document.getElementById("FPS").checked)
      // {
      // document.getElementById('gridback').style.backgroundColor='#8CAFAE';
      // document.getElementById('poissonback').style.backgroundColor='#8CAFAE';
      // document.getElementById('fpsback').style.backgroundColor='#3C6865';
      // let maxindex=0;
      // let upper=Math.min(allData.length*0.1,600)
      // for (let i=0;i<upper;i++)
      // {
      //   if (i==0)
      //   {
      //     let dt = allData[maxindex];
      //     let dt_x = dt.x0 * _this.chartRadius + _this.mainWidth / 2;
      //     let dt_y = dt.y0 * _this.chartRadius + _this.mainHeight / 2;
      //     allData[maxindex]["show"] = "true"
      //     showpointX.push(dt_x);
      //     showpointY.push(dt_y);
      //     showpoints.push(maxindex);
      //     maxdis=0;
      //     for (let k=0;k< allData.length;k++)
      //     {
      //       let dtk = allData[k];
      //       let dt_xk = dtk.x0 * _this.chartRadius + _this.mainWidth / 2;
      //       let dt_yk = dtk.y0 * _this.chartRadius + _this.mainHeight / 2;
      //       let dis=Math.sqrt(Math.pow(dt_xk-dt_x,2)+Math.pow(dt_yk-dt_y,2));
      //       distanceList.push(dis);
      //       if (dis>maxdis)
      //       {
      //         maxdis=dis;
      //         maxindex=k;
      //       }

      //     }
      //   }
      //   else
      //   {
      //     let dt = allData[maxindex];
      //     let dt_x = dt.x0 * _this.chartRadius + _this.mainWidth / 2;
      //     let dt_y = dt.y0 * _this.chartRadius + _this.mainHeight / 2;
      //     allData[maxindex]["show"] = "true"
      //     showpointX.push(dt_x);
      //     showpointY.push(dt_y);
      //     showpoints.push(maxindex);
      //     maxdis=0;
      //     for (let k=0;k< allData.length;k++)
      //     {
      //       let dtk = allData[k];
      //       let dt_xk = dtk.x0 * _this.chartRadius + _this.mainWidth / 2;
      //       let dt_yk = dtk.y0 * _this.chartRadius + _this.mainHeight / 2;
      //       let dis=Math.sqrt(Math.pow(dt_xk-dt_x,2)+Math.pow(dt_yk-dt_y,2));
      //       // distanceList.push(dis);
      //       if (dis<distanceList[k])
      //       {
      //         distanceList[k]=dis
      //       }      
      //       if (distanceList[k]>maxdis)
      //       {
      //         maxdis=distanceList[k];
      //         maxindex=k;
      //       }                
      //     }


      //   }
      // }
      // }
      ////End of FPS

      if (document.getElementById("FPS").checked) {
        document.getElementById('gridback').style.backgroundColor = '#8CAFAE';
        document.getElementById('poissonback').style.backgroundColor = '#8CAFAE';
        document.getElementById('fpsback').style.backgroundColor = '#3C6865';
        let sam_count = 0;
        let idx_list = []
        for (let i = 0; i < allData.length; i++) {
          allData[i]["show"] = "false";
        }
        for (let i = 0; i < 0.01 * allData.length || i < 300; i++)
        //for (let i=0; i<20000;i++)
        {

          let idx = Math.floor(allData.length * Math.random())
          let dt = allData[idx];
          let show_point = true;
          for (let j = 0; j < idx_list.length; j++) {
            if (idx_list[j] == idx) {
              show_point = false;
            }
          }
          let dt_x = dt.x0 * _this.chartRadius + _this.mainWidth / 2;
          let dt_y = dt.y0 * _this.chartRadius + _this.mainHeight / 2;
          // let w = Math.floor((dt_x) / 30);
          // let h = Math.floor((dt_y) / 30);
          let w = Math.floor((dt_x) / 30);
          let h = Math.floor((dt_y) / 30);


          // if (w >= 0 && w < this.mainWidth / 30 && h >= 0 && h < this.mainHeight / 30) {
          let dice = Math.random()
          if (w >= 0 && w < this.mainWidth / 30 && h >= 0 && h < this.mainHeight / 30) {
            if (matrixF[w][h] < 30 && show_point == true) {


              matrixF[w][h] = matrixF[w][h] + 1;
              allData[i]["show"] = "true"
              showpointX.push(dt_x);
              showpointY.push(dt_y);
              showpoints.push(i);
              sam_count += 1;

            }
          }



        }
      }

      ////Start of Poisson Disk
      else {
        if (document.getElementById("Grid").checked) {
          sample_radius = 5.5;
          document.getElementById('gridback').style.backgroundColor = '#3C6865';
          document.getElementById('poissonback').style.backgroundColor = '#8CAFAE';
          document.getElementById('fpsback').style.backgroundColor = '#8CAFAE';
        }
        else {
          sample_radius = 10
          document.getElementById('poissonback').style.backgroundColor = '#3C6865';
          document.getElementById('gridback').style.backgroundColor = '#8CAFAE';
          document.getElementById('fpsback').style.backgroundColor = '#8CAFAE';
        }
        for (let i = 0; i < allData.length; i++)
        //for (let i=0; i<20000;i++)
        {
          let dt = allData[i];
          allData[i]["show"] = "false"
          let dt_x = dt.x0 * _this.chartRadius + _this.mainWidth / 2;
          let dt_y = dt.y0 * _this.chartRadius + _this.mainHeight / 2;
          // let w = Math.floor((dt_x) / 30);
          // let h = Math.floor((dt_y) / 30);
          let w = Math.floor((dt_x) / 30);
          let h = Math.floor((dt_y) / 30);


          // if (w >= 0 && w < this.mainWidth / 30 && h >= 0 && h < this.mainHeight / 30) {
          if (w >= 0 && w < this.mainWidth / 30 && h >= 0 && h < this.mainHeight / 30) {
            let flag;
            if (w > 0 && h > 0) {
              flag = (matrixF[w - 1][h - 1] < 2 && matrixF[w][h - 1] < 2 && matrixF[w - 1][h] < 2)
            }
            else if (w > 0) {
              flag = (matrixF[w - 1][h] < 2)
            }
            else {
              flag = (matrixF[w][h - 1] < 2)
            }
            if (matrixF[w][h] < 2) {
              var closepoint = true;
              for (let j = 0; j < showpoints.length; j++) {
                if (Math.sqrt(Math.pow(showpointX[j] - dt_x, 2) + Math.pow(showpointY[j] - dt_y, 2)) < sample_radius) {
                  closepoint = false;
                  break;
                }
              }
              if (closepoint == true) {
                matrixF[w][h] = matrixF[w][h] + 1;
                allData[i]["show"] = "true"
                showpointX.push(dt_x);
                showpointY.push(dt_y);
                showpoints.push(i)
              }
            }
          }



        }
      }
      ////End of Poisson Disk
      return allData;
    },
    /**
     * @description: call function to draw
     * @param {*} filePath selected file path
     * @param {*} dimensions Feature Group
     * @return {*}
     */
    drawMain(filePath, dimensions, DAorder) {
      let _this = this;
      this.drawLegend(this.typeName, DAorder);

      if (switchState>0)
      {
        this.drawSideWidget(countData, DAorder);        
      }
      d3.csv(filePath).then((fileData) => {
        // d3.select("#zoomWindow").remove();
        
        let allData = this.getMainData(fileData, dimensions, DAorder);
        this.processedData = allData;
        

        this.drawSideWidget(allData, DAorder);
        this.drawDensity(filePath, dimensions, allData);
        this.drawLegend(this.typeName, DAorder);
        // this.drawScatter(allData);
        this.setupLasso(allData);
        
        this.drawScatter(allData);
        switchState=0;

      });
    },


    /**
     * @description: draw density
     * @param {*} filePath selected file path
     * @param {*} dimensions Feature Group
     * @param {*} densityAllData density data
     * @return {*}
     */
    drawDensity(filePath, dimensions, densityAllData) {
      d3.select("#mainDensity_g").remove();
      let density_g = d3.select("#mainViewPicSvg").append('g')
        .attr('id', 'mainDensity_g')
      // .attr('transform', `translate(${this.mainWidth / 2}, ${this.mainHeight / 2})`)
      let per = 0;
      let bandw = 0;
      if (filePath[13] == 'B') {
        per = 0.5
        bandw = 25
        // per=0.05
        // bandw=10
      } else if (filePath[13] == 'v') {
        per = 0.6;
        bandw = 18;
      } else if (filePath[13] == 'd') {
        bandw = 18;
        per = 0.3;
      }
      let densityTypeData = {};
      dimensions.forEach(d => {
        densityTypeData[d] = [];
      });
      densityAllData.forEach(d => {
        densityTypeData[d.class.toLowerCase()].push(d);
      });
      for (let type in densityTypeData) {
        let densityData = densityTypeData[type];
        if (densityData.length > 0) {
          let colorScale = d3.scaleLinear()
            .domain([0, per])
            .range(['white', this.colormap[type]]);
          var densityProgress = d3.contourDensity()
            .x(d => {
              return parseFloat(d.x0) * this.chartRadius + this.mainWidth / 2;
            })
            .y(d => {
              return parseFloat(d.y0) * this.chartRadius + this.mainHeight / 2;
            })
            .size([this.mainWidth, this.mainHeight])
            .thresholds(25)
            .bandwidth(bandw)(densityData);
          // let line = d3.line()
          // .x(d => d[0])
          // .y(d => d[1])
          // console.log(line(densityProgress[0].coordinates[0][0]));
          // density_g.append("path").attr("d", line([[1, 1000], [1, 1], [1000, 1000]])).attr('fill', 'none').attr("stroke", 'black');
          // density_g.append("path").attr("d", line(densityProgress[0].coordinates[0][0])).attr('fill', 'none').attr("stroke", 'black');
          density_g.append('g').attr('class', 'contour').selectAll("#density_all")
            .attr("id", 'density_all')
            .data(densityProgress)
            .enter()
            .append('path')
            .attr('d', d3.geoPath())
            .attr('fill', d => colorScale(d.value));
        }
      }

      let arc = d3.arc()
        .innerRadius(this.chartRadius)
        .outerRadius(this.chartRadius + 70);
      // console
      density_g.append('g')
        .attr('transform', `translate(${this.mainWidth / 2}, ${this.mainHeight / 2})`)
        .append('path')
        .attr('d', arc(d3.pie()([1])[0]))
        .attr('fill', 'white')
    },
    /**
     * @description: draw scatter
     * @param {*} scatterData scatter data
     * @return {*}
     */
    drawScatter(scatterData) {
      d3.select("#mainScatter_g").remove();

      // document.getElementById("#mainScatter_g")
      let scatter_g = d3.select("#mainViewPicSvg").append('g')
        .attr('id', 'mainScatter_g')
        .attr('afterhis', 'false')
        .attr('afterlasso', 'false')
        .attr('transform', `translate(${this.mainWidth / 2}, ${this.mainHeight / 2})`);
      // d3.select("#mainViewPicSvg")
      // .on("mousedown", function() { 
      //      var pos = d3.mouse(this); 
      //      console.log("(" + pos[0] + ", " + pos[1] +   ")")}) 
      // document.getElementById("mainViewPicSvg").addEventListener("mousemove", function(e){console.log(e.offsetX)})
      // var zoom = d3.zoom().on('zoom', zoomed);
      // d3.select("#mainViewPicSvg").call(zoom);
      // var transform = d3.event.transform;
      // d3.select("#mainViewPicSvg").attr('transform', transform.toString());
      d3.select("#tooltip").remove();
      let circles = scatter_g
        .selectAll('#mainScatter')
        .attr('id', 'mainScatter')
        .data(scatterData)
        .enter()
        .append('circle')
        .attr('class', d => 'rad_cir')
        .attr('state', 'bflasso')
        .attr('id', d => 'cir' + d.pid)
        .attr('path', d => d.path)
        .attr('cx', d => d.x0 * this.chartRadius)
        .attr('cy', d => d.y0 * this.chartRadius)
        .attr('fill', d => this.colormap[d.class.toLowerCase()])
        .attr("x0", d => d.x0).attr("y0", d => d.y0)
        .attr("circle", d => d.circle).attr("map", d => d.map).attr("line", d => d.line).attr("area", d => d.area)
        .attr("bar", d => d.bar).attr("net", d => d.net).attr("point", d => d.point).attr("diagram", d => d.diagram)
        .attr("matrix", d => d.table).attr("table", d => d.table)
        .attr("word", d => d.word)
        .attr('type', d => d.class.toLowerCase())
        .attr('stroke', 'black')
        .attr('stroke-width', 0.5)
        .attr("show", d => d.show)
        .attr("hisShow", "true")
        .attr('r', d => {
          return d.show == 'true' ? 2 : 0;
        })
        .on('mouseover', d => {
          // if (d3.select("#nodePic").attr("sid") != 1) {
          // console.log(d);
          if (lasso == 0 && document.getElementById('Selection').checked) {
            let selData = d.srcElement.__data__;
            d3.select('#cir' + selData.pid).attr('r', 8).attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
            // d3.select(this).attr('r', 8).attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
            // this.setSelect(selData, this.typeName);
            let tx = selData.x0 * this.chartRadius + this.mainWidth / 2 - 30;
            let ty = selData.y0 * this.chartRadius + this.mainHeight / 2 - 93;
            // console.log("tx")
            // console.log(tx)
            // console.log("ty")
            // console.log(ty)
            // console.log(d3.select('#cir' + selData.pid).attr("cx"))
            // console.log(d3.select('#cir' + selData.pid).attr("cy"))
            console.log(selData.pid)

            let tooltip = d3.select("#mainViewPic").append("div")
              .attr("id", "tooltip") //用于css设置类样式
              .attr("display", 'none')//新建一个tooltip

            tooltip.html("<img style='height: 70px; width: 140px; border-radius: 10px; border: solid 2px rgb(99,99,99);' src='" + "/src/assets" + selData.path.slice(1) + "'>")
              .style("left", (tx) + "px")
              .style('top', ty + 'px')
              .style('position', 'absolute')
              .attr('display', null);
            //this.clickNode(selData);
            //this.selectNode = selData;
            // this.setSelect(this.selectNode, this.typeName);
          }

        })
        .on('mouseout', d => {
          let selData = d.srcElement.__data__;
          // console.log(selData);
          // let selData = d.srcElement.__data__;
          // d3.select('#cir' + selData.pid).attr('r', 8).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
          d3.select('#cir' + selData.pid).attr('r', 2).attr("fill", this.colormap[selData.class.toLowerCase()]).attr('stroke-width', 0.5);
          d3.select("#tooltip").remove();
          if (d3.select("#nodePic").attr("sid") != 1) {
            this.removeSelect(this.typeName);
          }
        })
        .on("click", d => {
          let selData = d.srcElement.__data__;
          this.selectNode = selData;
          this.clickNode(selData);
          let close_node = this.closeNode(scatterData, selData, this.distanceType);
          this.updateGallery(close_node);
        });
      var mainW = this.mainWidth;
      var mainH = this.mainHeight;
      var scrollSize = 1;
      var showpoints1 = [];
      var showpointX1 = [];
      var showpointY1 = [];
      var showpointclass = [];
      var mouseX = 0;
      var mouseY = 0;
      var colormap = this.colormap;
      let clickNode = this.clickNode;
      let closeNode = this.closeNode;
      let updateGallery = this.updateGallery;
      let removeSelect = this.removeSelect;
      let distanceType = this.distanceType;
      let chartRadius = this.chartRadius;
      let selectNode = this.selectNode;
      let setSelect = this.setSelect;
      let typeName = this.typeName;
      // let chartRadius=this.chartRadius;
      document.getElementById('mainViewPicSvg').onmousedown = function (e) {
        var middleclick;
        if (!e) var e = window.event;
        if (e.which) { middleclick = (e.which == 2); positionfixed = positionfixed * (-1) }
        else if (e.button) { middleclick = (e.button == 2); positionfixed = positionfixed * (-1) }

      }
      document.getElementById("mainViewPicSvg").addEventListener("mousemove", function (e) {

        // console.log(positionfixed);

        if (!document.getElementById('Zoom').checked) {
          d3.select("#zoomCanvas").remove();
          d3.select("#zoomLens").remove();
          positionfixed = positionfixed * (-1);
        }
        else if (positionfixed == 1) {
          console.log("middle")
          console.log(positionfixed)
        }
        else {
          if (d3.select("#nodePic").attr("sid") != 1) {
            removeSelect(typeName);
          }
          console.log(positionfixed);
          d3.select("#tooltip").remove();
          // let zoomLens=d3.select("#mainViewPicSvg").append('rect')
          // .attr("id","zoomLens")
          // .attr("x",mouseX-30)
          // .attr("y",mouseY-30)
          // .attr("height",60)
          // .attr("width",60)
          // .style("fill",'transparent').style("outline", "3px red solid")
          // .on("click",function(){
          //   positionfixed=1
          // })
          // let zoomLens=d3.select("#mainViewPicSvg").append('circle')
          // .attr("id","zoomLens")
          // .attr("cx",mouseX)
          // .attr("cy",mouseY)
          // .attr("r", 50)
          // .style("fill",'transparent').style("outline", "3px black solid")
          // .on("click",function(){
          //   positionfixed=1
          // })
          // let zoomCanvas=d3.select("#zoomWindow")
          // .append('g')
          // .attr("id","zoomCanvas")
          // .attr('transform', 'translate(0,0)')
          // zoomCanvas.append('rect')
          // .attr("x",1)
          // .attr("y",1)
          // .attr('height',153)
          // .attr('width',153)
          // .style("fill", "transparent")
          // .style("outline", "1px solid #A5C6C6")
          // let zoomCanvas=d3.select("#mainViewPicSvg").append('g')
          // .attr("id","zoomCanvas")
          // .attr('transform', `translate(${e.offsetX+5+50}, ${e.offsetY+5-70})`);
          let preX = mouseX
          let preY = mouseY
          // console.log("OffsetX:")
          // console.log(e.offsetX)

          mouseX = e.offsetX
          mouseY = e.offsetY

          // console.log(e.detail)

          scrollSize = 1

          let scaleFactor = scrollSize
          scrollSize = scrollSize
          d3.select("#zoomCanvas").remove();
          d3.select("#zoomLens").remove();
          let zoomCanvas = d3.select("#mainViewPicSvg").append('g')
            .attr("id", "zoomCanvas")
            .attr('transform', `translate(${e.offsetX}, ${e.offsetY})`);

          // zoomCanvas.append('rect').attr('x',-5).attr('y',-5).attr("width",210).attr("height",210)
          // .style("fill",'white').style("outline", "1px solid")
          zoomCanvas.append('circle').attr('x', 0).attr('y', 0).attr("r", 53)
            .style("fill", 'black')
          zoomCanvas.append('circle').attr('x', 0).attr('y', 0).attr("r", 50)
            .style("fill", 'white').style("stroke", "3px solid").attr("id", "lens")
        //  if (e.offsetX<94 || e.offsetX>636 || e.offsetY<104 || e.offsetY>646)
          if (Math.sqrt(Math.pow(365 - e.offsetX, 2) + Math.pow(365 - e.offsetY, 2))>chartRadius-10)
          {
              d3.select("#zoomCanvas").style("display","none")
          }
          // document.getElementById('lens').onmousedown =  function (e) {
          //   var middleclick;
          //   if (!e) var e = window.event;
          //   if (e.which) {middleclick = (e.which == 2);positionfixed=positionfixed*(-1)}
          //   else if (e.button) {middleclick = (e.button == 2);positionfixed=positionfixed*(-1)}

          // }

          d3.selectAll('.rad_cir')
            .each(function (d, i) {
              let x = Number(d3.select(this).attr("cx")) + mainW / 2;
              let y = Number(d3.select(this).attr("cy")) + mainH / 2;
              let show = d3.select(this).attr("show")
              let state = d3.select(this).attr("r")
              let pointFilter = (state != 0)
              // if (lasso==0)
              // {
              //   pointFilter=(show=="true")
              // }
              // else 
              // {
              //   pointFilter=(state!=0)
              // }
              let dis = Math.sqrt(Math.pow(x - e.offsetX, 2) + Math.pow(y - e.offsetY, 2));
              let disX = Math.sqrt(Math.pow(x - e.offsetX, 2))
              let disY = Math.sqrt(Math.pow(y - e.offsetY, 2))
              let scope = 30 / scaleFactor;
              let dis_thresh = 30 / scaleFactor;
              if (disX < scope && disY < scope && pointFilter) {
                var closepoint = true;
                // for (let j=0;j<showpoints1.length;j++)
                // {
                //   if (Math.sqrt(Math.pow(showpointX1[j]-x,2)+Math.pow(showpointY1[j]-y,2))< dis_thresh)
                //   {
                //     closepoint=false;
                //     break;
                //   }
                // }
                if (closepoint == true) {
                  showpointX1.push(x);
                  showpointY1.push(y);
                  let x0_t = d3.select(this).attr("x0");
                  let y0_t = d3.select(this).attr("y0");
                  let circle = d3.select(this).attr("circle");
                  let map = d3.select(this).attr("map");
                  let line = d3.select(this).attr("line");
                  let area = d3.select(this).attr("area");
                  let bar = d3.select(this).attr("bar");
                  let net = d3.select(this).attr("net");
                  let point = d3.select(this).attr("point");
                  let diagram = d3.select(this).attr("diagram");
                  let matrix = d3.select(this).attr("matrix");
                  let table = d3.select(this).attr("table");
                  let word = d3.select(this).attr("word");
                  showpoints1.push({
                    "id": d3.select(this).attr("id"), "pid": d3.select(this).attr("id").substring(3), "class": d3.select(this).attr("class"), "path": d3.select(this).attr("path"), "x": x, "y": y,
                    "x0": Number(x0_t), "y0": Number(y0_t), "circle": Number(circle), "map": Number(map), "line": Number(line), "area": Number(area),
                    "bar": Number(bar), "net": Number(net), "point": Number(point), "diagram": Number(diagram), "matrix": Number(matrix), "table": Number(table), "word": Number(word)
                  });
                  showpointclass.push(d3.select(this).attr("type"));
                  // d3.select(this).style("fill-opacity",1)
                }
              }
              // else
              // {
              //   d3.select(this).style("fill-opacity",0.2)
              // }
            }
            )
          let circle_r = 3//(scaleFactor < 10 ? scaleFactor*2 : 10);
          // console.log(showpoints1);
          var zoom_radius = circle_r;
          zoomCanvas.selectAll("circle")
            .data(showpoints1)
            .enter()
            .append('circle')
            // .attr("cx", function(d,i){return (showpointX1[i]-mouseX)*scaleFactor*200/60+100;})
            // .attr("cy", function(d,i){return (showpointY1[i]-mouseY)*scaleFactor*200/60+100;})
            .attr("cx", function (d, i) { return (showpointX1[i] - mouseX) * scaleFactor * 50 / 30; })
            .attr("cy", function (d, i) { return (showpointY1[i] - mouseY) * scaleFactor * 50 / 30; })
            .attr("r", function (d, i) {
              let dx = (showpointX1[i] - mouseX) * scaleFactor * 50 / 30;
              let dy = (showpointY1[i] - mouseY) * scaleFactor * 50 / 30;
              if (Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2)) > 48) { return 0 }
              else { return circle_r }
            })
            .attr("id", function (d, i) { return "zoom" + d.pid })
            .attr("pid", function (d, i) { return d.pid })
            .style("fill", function (d, i) { return colormap[showpointclass[i]] })
            .style("stroke", "black")
            .on('mouseover', function (d, i) {
              // if (d3.select("#nodePic").attr("sid") != 1) {
              // console.log(d);
              if (lasso == 0) {
                let selData = d.srcElement.__data__;
                //console.log(selData)
                //d3.select('#cir' + selData.pid).attr('r', 8).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
                zoom_radius = d3.select('#zoom' + selData.pid).attr("r")
                d3.select('#zoom' + selData.pid).attr('r', 2 * zoom_radius).attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
                // this.setSelect(selData, this.typeName);
                // let tx = selData.x0 * this.chartRadius + this.mainWidth / 2 - 30;
                // let ty = selData.y0 * this.chartRadius + this.mainHeight / 2 - 93;
                let tx = selData.x - 30;
                let ty = selData.y - 93;
                // console.log(tx)
                let tooltip = d3.select("#mainViewPic").append("div")
                  .attr("id", "tooltip") //用于css设置类样式
                  .attr("display", 'none')//新建一个tooltip

                tooltip.html("<img style='height: 70px; width: 140px; border-radius: 10px; border: solid 2px rgb(99,99,99);' src='" + "/src/assets" + selData.path.slice(1) + "'>")
                  .style("left", (tx) + "px")
                  .style('top', ty + 'px')
                  .style('position', 'absolute')
                  .attr('display', null);
                console.log(selData);
                // clickNode(selData);
                //this.clickNode(selData);
                //this.selectNode = selData;
                // this.setSelect(this.selectNode, this.typeName);
              }

            })
            .on('mouseout', d => {
              let selData = d.srcElement.__data__;
              // console.log(selData);
              // let selData = d.srcElement.__data__;
              // d3.select('#cir' + selData.pid).attr('r', 8).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
              //d3.select('#cir' + selData.pid).attr('r', 2).attr("fill", this.colormap[selData.class.toLowerCase()]).attr('stroke-width', 0.5);
              d3.select('#zoom' + selData.pid).attr('r', zoom_radius).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 0.5).attr('stroke', 'rgb(99,99,99)');
              d3.select("#tooltip").remove();
              // if (d3.select("#nodePic").attr("sid") != 1) {
              //   removeSelect(typeName);
              // }
            })
            .on("click", d => {
              let selData = d.srcElement.__data__;
              selectNode = selData;
              clickNode(selData);
              // d3.selectAll("tr").style("background-color", "white")
              // // console.log(selData.class)
              // let nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
              // let da = selData;
              // let class_score = [da.circle, da.map, da.line, da.area, da.bar, da.net, da.point, da.diagram, da.matrix, da.table, da.word];
              // let max_score = 0;
              // let max_idx = -1;
              // for (let i = 0; i < class_score.length; i++) {
              //   if (class_score[i] > max_score) {
              //     max_score = class_score[i];
              //     max_idx = i;
              //   }
              // }
              // let predict_class = nameorder1[max_idx];
              // if (selData.class != undefined) {
              //   color = this.colormap[selData.class.toLowerCase()]
              //   console.log(selData);
              //   d3.select("#row" + selData.class[0].toUpperCase() + selData.class.slice(1)).style("background-color", "#D7F4F2")
              // }
              // else {
              //   // color="yellow";
              //   color = this.colormap[predict_class]
              //   d3.select("#row" + predict_class[0].toUpperCase() + predict_class.slice(1)).style("background-color", "#D7F4F2")
              //   console.log(selData.area);
              // }
              setSelect(selData, typeName);
              d3.selectAll(".select_circle").remove();
              // d3.select('#zoom' + selData.pid)
              //   // .attr("r", 10)
              //   // .attr("fill", 'rgb(255,212,0)')
              //   .attr('r', 8).attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)')
              // .attr('cx', d3.select('#cir' + selData.pid).attr("cx"))
              // .attr('cy', d3.select('#cir' + selData.pid).attr("cy"))
              let cx = Number(d3.select('#zoom' + selData.pid).attr("cx"))
              let cy = Number(d3.select('#zoom' + selData.pid).attr("cy"))
              let c_fill = d3.select('#zoom' + selData.pid).style("fill")
              let zoomCanvas = d3.select("#zoomCanvas")
              d3.select("#zoom_select").remove()
              zoomCanvas.append("circle").attr('stroke-width', 3).attr("id", "zoom_select").attr('stroke', 'rgb(99,99,99)').attr("cx", cx).attr("cy", cy).attr("r", 8).style("fill", c_fill)
              let close_node = closeNode(scatterData, selData, distanceType);
              updateGallery(close_node);
            });
          showpoints1 = [];
          showpointX1 = [];
          showpointY1 = [];
          showpointclass = [];
          // console.log(showpoints1)
        }
      })

      document.getElementById("mainViewPicSvg").addEventListener("mousewheel", function (e) {
        //console.log(e.offsetX-mainW / 2)
        // console.log(e.wheelDelta)
        // console.log(positionfixed);
        console.log(e.offsetX)
        console.log(e.offsetY)

        if (!document.getElementById('Zoom').checked) {
          d3.select("#zoomCanvas").remove();
          d3.select("#zoomLens").remove();
          positionfixed = positionfixed * (-1);
        }
        else if (positionfixed == 1) {
          console.log("middle")
        }
        else {
          if (d3.select("#nodePic").attr("sid") != 1) {
            removeSelect(typeName);
          }
          d3.select("#tooltip").remove();
          let preX = mouseX
          let preY = mouseY
          // console.log("OffsetX:")
          // console.log(e.offsetX)
          mouseX = e.offsetX
          mouseY = e.offsetY

          // console.log(e.detail)
          if (mouseX != preX || mouseY != preY) {
            scrollSize = 2
          }
          let scaleFactor = scrollSize + e.wheelDelta / 120
          scrollSize = scrollSize + e.wheelDelta / 120
          d3.select("#zoomCanvas").remove();
          d3.select("#zoomLens").remove();
          // let zoomLens=d3.select("#mainViewPicSvg").append('rect')
          // .attr("id","zoomLens")
          // .attr("x",mouseX-30)
          // .attr("y",mouseY-30)
          // .attr("height", 60)
          // .attr("width", 60)
          // .style("fill",'transparent').style("outline", "3px red solid")
          // .on("click",function(){
          //   positionfixed=1
          // })
          // let zoomCanvas=d3.select("#zoomWindow")
          // .append('g')
          // .attr("id","zoomCanvas")
          // .attr('transform', 'translate(0,0)')
          // zoomCanvas.append('rect')
          // .attr("x",1)
          // .attr("y",1)
          // .attr('height',153)
          // .attr('width',153)
          // .style("fill", "transparent")
          // .style("outline", "1px solid #A5C6C6")
          // d3.select("#zoomCanvas").remove();
          // d3.select("#zoomLens").remove();
          // let zoomLens=d3.select("#mainViewPicSvg").append('rect')
          // .attr("id","zoomLens")
          // .attr("x",mouseX-60)
          // .attr("y",mouseY-60)
          // .attr("height",120)
          // .attr("width",120)
          // .style("fill",'transparent').style("outline", "3px red solid")
          // .on("click",function(){
          //   positionfixed=1
          // })
          let zoomCanvas = d3.select("#mainViewPicSvg").append('g')
            .attr("id", "zoomCanvas")
            // .attr('transform', `translate(${e.offsetX+5+50}, ${e.offsetY+5-70})`);
            .attr('transform', `translate(${e.offsetX}, ${e.offsetY})`);
          // zoomCanvas.append('rect').attr('x',-5).attr('y',-5).attr("width",210).attr("height",210)
          // .style("fill",'white').style("outline", "1px solid")
          zoomCanvas.append('circle').attr('x', 0).attr('y', 0).attr("r", 53)
            .style("fill", 'black')
          zoomCanvas.append('circle').attr('x', 0).attr('y', 0).attr("r", 50)
            .style("fill", 'white').attr("id", "lens")
          if (Math.sqrt(Math.pow(365 - e.offsetX, 2) + Math.pow(365 - e.offsetY, 2))>chartRadius-10)
          {
              d3.select("#zoomCanvas").style("display","none")
          }

          // document.getElementById('lens').onmousedown =  function (e) {
          //   var middleclick;
          //   if (!e) var e = window.event;
          //   if (e.which) {middleclick = (e.which == 2);positionfixed=positionfixed*(-1)}
          //   else if (e.button) {middleclick = (e.button == 2);positionfixed=positionfixed*(-1)}

          // }
          d3.selectAll('.rad_cir')
            .each(function (d, i) {
              let x = Number(d3.select(this).attr("cx")) + mainW / 2;
              let y = Number(d3.select(this).attr("cy")) + mainH / 2;
              let show = d3.select(this).attr("show")
              let state = d3.select(this).attr("r")
              let pointFilter = (state != 0)
              // if (lasso==0)
              // {
              //   pointFilter=(show=="true")
              // }
              // else 
              // {
              //   pointFilter=(state!=0)
              // }

              let dis = Math.sqrt(Math.pow(x - e.offsetX, 2) + Math.pow(y - e.offsetY, 2));
              let disX = Math.sqrt(Math.pow(x - e.offsetX, 2))
              let disY = Math.sqrt(Math.pow(y - e.offsetY, 2))
              let scope = 30 / scaleFactor;
              let dis_thresh = 30 / scaleFactor;
              if (disX < scope && disY < scope && pointFilter) {
                var closepoint = true;
                // for (let j=0;j<showpoints1.length;j++)
                // {
                //   if (Math.sqrt(Math.pow(showpointX1[j]-x,2)+Math.pow(showpointY1[j]-y,2))< dis_thresh)
                //   {
                //     closepoint=false;
                //     break;
                //   }
                // }
                if (closepoint == true) {
                  showpointX1.push(x);
                  showpointY1.push(y);
                  let x0_t = d3.select(this).attr("x0");
                  let y0_t = d3.select(this).attr("y0");
                  let circle = d3.select(this).attr("circle");
                  let map = d3.select(this).attr("map");
                  let line = d3.select(this).attr("line");
                  let area = d3.select(this).attr("area");
                  let bar = d3.select(this).attr("bar");
                  let net = d3.select(this).attr("net");
                  let point = d3.select(this).attr("point");
                  let diagram = d3.select(this).attr("diagram");
                  let matrix = d3.select(this).attr("matrix");
                  let table = d3.select(this).attr("table");
                  let word = d3.select(this).attr("word");
                  showpoints1.push({
                    "id": d3.select(this).attr("id"), "pid": d3.select(this).attr("id").substring(3), "class": d3.select(this).attr("class"), "path": d3.select(this).attr("path"), "x": x, "y": y,
                    "x0": Number(x0_t), "y0": Number(y0_t), "circle": Number(circle), "map": Number(map), "line": Number(line), "area": Number(area),
                    "bar": Number(bar), "net": Number(net), "point": Number(point), "diagram": Number(diagram), "matrix": Number(matrix), "table": Number(table), "word": Number(word)
                  });
                  showpointclass.push(d3.select(this).attr("type"));
                }
              }
            }
            )
          let circle_r = 3//(scaleFactor < 10 ? scaleFactor*2 : 10);
          // console.log(showpoints1);
          var zoom_radius = circle_r;
          zoomCanvas.selectAll("circle")
            .data(showpoints1)
            .enter()
            .append('circle')
            .attr("cx", function (d, i) { return (showpointX1[i] - mouseX) * scaleFactor * 50 / 30; })
            .attr("cy", function (d, i) { return (showpointY1[i] - mouseY) * scaleFactor * 50 / 30; })
            .attr("r", function (d, i) {
              let dx = (showpointX1[i] - mouseX) * scaleFactor * 50 / 30;
              let dy = (showpointY1[i] - mouseY) * scaleFactor * 50 / 30;
              if (Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2)) > 48) { return 0 }
              else { return circle_r }
            })
            .attr("id", function (d, i) { return "zoom" + d.pid })
            .attr("pid", function (d, i) { return d.pid })
            .style("fill", function (d, i) { return colormap[showpointclass[i]] })
            .style("stroke", "black")
            .on('mouseover', function (d, i) {
              // if (d3.select("#nodePic").attr("sid") != 1) {
              // console.log(d);
              if (lasso == 0) {
                let selData = d.srcElement.__data__;
                // console.log(selData)
                //d3.select('#cir' + selData.pid).attr('r', 8).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
                zoom_radius = d3.select('#zoom' + selData.pid).attr("r")
                d3.select('#zoom' + selData.pid).attr('r', 2 * zoom_radius).attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
                // this.setSelect(selData, this.typeName);
                // let tx = selData.x0 * this.chartRadius + this.mainWidth / 2 - 30;
                // let ty = selData.y0 * this.chartRadius + this.mainHeight / 2 - 93;
                let tx = selData.x - 30;
                let ty = selData.y - 93;
                let tooltip = d3.select("#mainViewPic").append("div")
                  .attr("id", "tooltip") //用于css设置类样式
                  .attr("display", 'none')//新建一个tooltip

                tooltip.html("<img style='height: 70px; width: 140px; border-radius: 10px; border: solid 2px rgb(99,99,99);' src='" + "/src/assets" + selData.path.slice(1) + "'>")
                  .style("left", (tx) + "px")
                  .style('top', ty + 'px')
                  .style('position', 'absolute')
                  .attr('display', null);
                //this.clickNode(selData);
                //this.selectNode = selData;
                // this.setSelect(this.selectNode, this.typeName);
              }

            })
            .on('mouseout', d => {
              let selData = d.srcElement.__data__;
              // console.log(selData);
              // let selData = d.srcElement.__data__;
              // d3.select('#cir' + selData.pid).attr('r', 8).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 3).attr('stroke', 'rgb(99,99,99)');
              //d3.select('#cir' + selData.pid).attr('r', 2).attr("fill", this.colormap[selData.class.toLowerCase()]).attr('stroke-width', 0.5);
              d3.select('#zoom' + selData.pid).attr('r', zoom_radius).attr('fill', 'rgb(255,212,0)').attr('stroke-width', 0.5).attr('stroke', 'rgb(99,99,99)');
              d3.select("#tooltip").remove();
              // if (d3.select("#nodePic").attr("sid") != 1) {
              //   removeSelect(typeName);
              // }
            })
            .on("click", d => {
              let selData = d.srcElement.__data__;
              selectNode = selData;
              d3.selectAll(".select_circle").remove();
              clickNode(selData);
              // d3.selectAll("tr").style("background-color", "white")
              // // console.log(selData.class)
              // let nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
              // let da = selData;
              // let class_score = [da.circle, da.map, da.line, da.area, da.bar, da.net, da.point, da.diagram, da.matrix, da.table, da.word];
              // let max_score = 0;
              // let max_idx = -1;
              // for (let i = 0; i < class_score.length; i++) {
              //   if (class_score[i] > max_score) {
              //     max_score = class_score[i];
              //     max_idx = i;
              //   }
              // }
              // let predict_class = nameorder1[max_idx];
              // if (selData.class != undefined) {
              //   color = this.colormap[selData.class.toLowerCase()]
              //   console.log(selData);
              //   d3.select("#row" + selData.class[0].toUpperCase() + selData.class.slice(1)).style("background-color", "#D7F4F2")
              // }
              // else {
              //   // color="yellow";
              //   color = this.colormap[predict_class]
              //   d3.select("#row" + predict_class[0].toUpperCase() + predict_class.slice(1)).style("background-color", "#D7F4F2")
              //   console.log(selData.area);
              // }
              // console.log(d.srcElement)
              // console.log(selData);
              // console.log(close_node);
              setSelect(selData, typeName);
              // d3.select('#zoom' + selData.pid)
              // .attr('r', 8).attr('stroke-width', 2*zoom_radius).attr('stroke', 'rgb(99,99,99)')
              let cx = Number(d3.select('#zoom' + selData.pid).attr("cx"))
              let cy = Number(d3.select('#zoom' + selData.pid).attr("cy"))
              let c_fill = d3.select('#zoom' + selData.pid).style("fill")
              let zoomCanvas = d3.select("#zoomCanvas")
              d3.select("#zoom_select").remove()
              zoomCanvas.append("circle").attr('stroke-width', 3).attr("id", "zoom_select").attr('stroke', 'rgb(99,99,99)').attr("cx", cx).attr("cy", cy).attr("r", 8).style("fill", c_fill)

              let close_node = closeNode(scatterData, selData, distanceType);
              // console.log(selData);
              // console.log(close_node);

              updateGallery(close_node);
            });
          showpoints1 = [];
          showpointX1 = [];
          showpointY1 = [];
          showpointclass = [];
          // console.log(showpoints1)
        }
      })

      // console.log(circles);
    },
    /**
     * @description: function of click a node
     * @param {*} selData selected node's data
     * @return {*}
     */
    clickNode(selData) {
      let color;
      d3.selectAll("tr").style("background-color", "white")
      // console.log(selData.class)
      let nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
      let d = selData;
      let class_score = [d.circle, d.map, d.line, d.area, d.bar, d.net, d.point, d.diagram, d.matrix, d.table, d.word];
      let max_score = 0;
      let max_idx = -1;
      for (let i = 0; i < class_score.length; i++) {
        if (class_score[i] > max_score) {
          max_score = class_score[i];
          max_idx = i;
        }
      }
      let predict_class = nameorder1[max_idx];
      if (selData.class != undefined) {
        color = this.colormap[selData.class.toLowerCase()]
        console.log(selData);
        d3.select("#row" + selData.class[0].toUpperCase() + selData.class.slice(1)).style("background-color", "#D7F4F2")
      }
      else {
        // color="yellow";
        color = this.colormap[predict_class]
        d3.select("#row" + predict_class[0].toUpperCase() + predict_class.slice(1)).style("background-color", "#D7F4F2")
        console.log(selData.area);
      }
      if (!document.getElementById('Zoom').checked) {
        d3.select("#mainScatter_g")
        .append("circle")
        .attr("id", "sel_circle" + selData.pid)
        .attr("class", 'select_circle')
        // .attr("r", 10)
        // .attr("fill", 'rgb(255,212,0)')
        .attr('cx', selData.x0 * this.chartRadius)
        .attr('cy', selData.y0 * this.chartRadius)
        .attr('r', 8).attr('stroke-width', 3).attr("fill", color).attr('stroke', 'rgb(99,99,99)')
        // .attr('cx', d3.select('#cir' + selData.pid).attr("cx"))
        // .attr('cy', d3.select('#cir' + selData.pid).attr("cy"))
        // .attr('stroke', 'black')
        // .attr('stroke-width', 0.5);

        d3.select('#nodePic').attr("sid", 1);
      }
    },
    /**
     * @description: Calculate the ten closest points
     * @param {*} scatterData all scatter data
     * @param {*} selectNode the selected node data
     * @param {*} dis_type computing method (Cosine / Projection)
     * @return {Array} Close Node data
     */
    closeNode(scatterData, selectNode, dis_type) {
      let distance = new Array();
      let points=new Array();
      scatterData.forEach(d => {
        let dis;
        if (dis_type == 'Cosine')
          dis = this.getCosineDistance([d.circle, d.map, d.line, d.area, d.bar, d.net, d.point, d.diagram, d.matrix, d.table, d.word], [selectNode.circle, selectNode.map, selectNode.line, selectNode.area, selectNode.bar, selectNode.net, selectNode.point, selectNode.diagram, selectNode.matrix, selectNode.table, selectNode.word])
        else if (dis_type == 'Projection')
          dis = this.getProjectionDistance([d.x0, d.y0], [selectNode.x0, selectNode.y0])
        distance.push({
          dis: dis,
          node: d
        });
      });
      distance.sort(function (a, b) {
        return a.dis - b.dis;
      })
      // console.log(distance);
      let close_node = new Array();
      let close_dis = new Array();
      let isDifer = 0;
      if (distance[0].pid == selectNode.pid)
        isDifer = 1;
      // console.log(distance.slice(0, 10))
      // distance.slice(1 - isDifer, 11 - isDifer).forEach(d => {
      //   close_node.push(d.node);
      // })
      let startIndex = 1 - isDifer;
      let movepoint = startIndex;
      while (startIndex < 11 - isDifer) {
        let dup = false;
        // for (let k=0;k<close_node.length;k++)
        // {
        //   let distan;
        //   let d=close_node[k];
        //   if (dis_type == 'Cosine')
        //     distan = this.getCosineDistance([d.circle, d.map, d.line, d.area, d.bar, d.net, d.point, d.diagram, d.matrix, d.table, d.word], [selectNode.circle, selectNode.map, selectNode.line, selectNode.area, selectNode.bar, selectNode.net, selectNode.point, selectNode.diagram, selectNode.matrix, selectNode.table, selectNode.word])
        //   else if (dis_type == 'Projection')
        //     distan = this.getProjectionDistance([d.x0, d.y0], [selectNode.x0, selectNode.y0])
        //   if (distan<0.00005)
        //     dup =true;
        // }
        if (dup == false) {
          startIndex = startIndex + 1;
          close_node.push(distance[movepoint].node);
          close_dis.push(distance[movepoint].dis);
        }
        // if (movepoint<startIndex+9)
        let filePath = this.fileP.filePath;
        if (filePath[13] == 'B' && startIndex>=6) {
        movepoint = movepoint + 2;}
        else
        {
          movepoint+=1;
        }

      }
      return close_node;
    },
    /**
     * @description: Projection Distance
     * @param {Array} nodeA [x, y]
     * @param {Array} nodeB [x, y]
     * @return {Float} distance between two nodes
     */
    getProjectionDistance(nodeA, nodeB) {
      //console.log(Math.pow(nodeA[0] - nodeB[0], 2) + Math.pow(nodeA[1] - nodeB[1], 2));
      return Math.pow(nodeA[0] - nodeB[0], 2) + Math.pow(nodeA[1] - nodeB[1], 2);
    },
    /**
     * @description: Cosine Distance
     * @param {Array} nodeA [x, y]
     * @param {Array} nodeB [x, y]
     * @return {Float} distance between two nodes
     */
    getCosineDistance(nodeA, nodeB) {
      let sa = 0, sb = 0, s = 0;
      let i = 0
      this.dimensions.forEach(d => {
        let a = parseFloat(nodeA[i]);
        // console.log("a")
        // console.log(a);
        let b = parseFloat(nodeB[i]);
        // console.log("b")
        // console.log(b);        
        sa += a * a;
        sb += b * b;
        s += a * b;
        i += 1;
      })
      return 1 - (s / Math.sqrt(sa * sb));
    },
    /**
     * @description: create a lasso
     * @param {*} data scatter data
     * @return {*}
     */
    setupLasso(data) {
      let _this = this;
      // console.log(data);
      let lasso_g;
      if (isRedraw == false) {
        d3.selectAll(".lasso").remove()
        lasso_g = d3.select("#mainViewPicSvg")
          .append('g')
          .attr('class', 'lasso')
          .attr('id', 'lasso_g');
      }
      else {
        lasso_g = d3.select('#lasso_g');
        lasso_g.select("#origin").remove();
        lasso_g.select("#drawn").remove();
        lasso_g.select("#loop_close").remove();
      }
      let origin_node = lasso_g
        .append("circle")
        .attr("id", "origin");
      let draw_path = lasso_g
        .append('path')
        .attr("id", 'drawn')
        .attr("class", "lassoDraw");
      let close_path = lasso_g
        .append("path")
        .attr("id", "loop_close")
        .attr("class", "lassoClose");

      let select_path = "";
      let end_path = "";
      let origin_circle;
      let target_circle;
      let closePathDistance = 500;

      let polygon = new Array();

      let dragStarted = function (event) {
        // console.log(event.x, event.y, 'st');
        // origin_node.attr("r", 10)
        //   .attr("cx", event.x)
        //   .attr('cy', event.y)
        //   .attr('stroke', 'gray')
        //   .attr("fill", 'red');
        // origin_circle = [event.x, event.y];
        // if (lasso==1)
        // {
        //   d3.select("#drawn").remove();
        //   d3.select("#loop_close").remove();
        //   draw_path = lasso_g
        // .append('path')
        // .attr("id", 'drawn')
        // .attr("class","lassoDraw");
        //   close_path = lasso_g
        // .append("path")
        // .attr("id", "loop_close")
        // .attr("class","lassoClose");  
        // }
        mousepreX = event.x;
        mousepreY = event.y;
      }
      let dragged = function (event) {
        // console.log(event.x, event.y, "ed");
        // islassoing=true
        let dx = mousepreX - event.x
        let dy = mousepreY - event.y
        if (Math.sqrt(Math.pow(dx, 2) + Math.pow(dy, 2)) > 10) {
          let tx = event.x;
          let ty = event.y;
          if (select_path == "") {
            select_path = select_path + "M " + tx + " " + ty;
            target_circle = [event.x, event.y];
            polygon.push([event.x, event.y]);
          } else {
            select_path = select_path + "L " + tx + " " + ty;
          }
          polygon.push([tx, ty]);
          let distance = Math.sqrt(Math.pow(tx - target_circle[0], 2) + Math.pow(ty - target_circle[1], 2));
          let close_draw_path = "M " + tx + " " + ty + " L " + target_circle[0] + " " + target_circle[1];
          draw_path.attr('d', select_path);

          close_path.attr("d", close_draw_path);
          if (distance < closePathDistance) {
            close_path.attr("display", null);
          } else {
            close_path.attr("display", "none");
          }
          lasso = 1
          console.log("dragged")
        }
      }
      let dragEnded = function () {
        console.log("lasso-ended")
        console.log(lasso)
        if (lasso == 1) {
          lasso = 0
          origin_node.attr("display", "none");
          if (d3.select("#mainScatter_g").attr("afterlasso") == "true") { d3.selectAll('.brush_rect').remove(); }
          d3.select("#mainScatter_g").attr("afterlasso", "true")
          // draw_path.attr("d", null);
          // close_path.attr("d", null);

          let levelType = undefined;
          let pidScatter = {};
          let filePath = _this.fileP.filePath;
          if (filePath[13] == 'B') {
            levelType = _this.levelCluster["Beagle"];
          }

          if (filePath[13] == 'v') {
            levelType = _this.levelCluster["VIS"];
          }

          if (filePath[13] == 'd') {
            levelType = _this.levelCluster["Data"];
          }
          else{
             levelType = _this.levelCluster["Beagle"];
          }
          let treeCnt = {};
          levelType.forEach(d => {
            treeCnt[d.toLowerCase()] = {
              value: 0,
              id: d
            }
          })
          let selectData = {};
          _this.typeName.forEach(d => {
            selectData[d] = {};
            for (let i = 1; i <= 9; ++i)
              selectData[d][i] = { cnt: 0 };
          })
          // console.log(polygon);

          data.forEach((allData, i) => {
            let cx = allData.x0 * _this.chartRadius + _this.mainWidth / 2;
            let cy = allData.y0 * _this.chartRadius + _this.mainHeight / 2;
            let cd = allData;
            // d3.select('#cir' + cd.pid).attr("hisShow")
            if (classifyPoint(polygon, [cx, cy]) < 1 && d3.select('#cir' + cd.pid).attr("hisShow") == "true") {
              pidScatter[cd.pid] = 1;
              _this.typeName.forEach(hisTag => {
                let indexNum = Math.floor(parseFloat(cd[hisTag.toLowerCase()]) * 10);
                if (indexNum == 10) indexNum--; // let 1 to 0.9 ~ 1
                if (indexNum != 0) {
                  selectData[hisTag][indexNum].cnt++;
                }
              })
              if (typeof (treeCnt[cd['class']]) != 'undefined')
                treeCnt[cd['class']].value++;
            }
          })

          let treeData = [];
          let sumTree = 0;
          for (let i in treeCnt) {
            if (treeCnt[i].value > 0) {
              treeData.push({
                value: treeCnt[i].value,
                id: treeCnt[i].id.toLowerCase(),
                top: sumTree
              });
              sumTree += treeCnt[i].value;
            }
          }

          d3.selectAll('.rad_cir')
            .attr('r', d => {
              return pidScatter[d.pid] == 1 ? 2 : 0;
            })
            .attr('state', d => {
              return pidScatter[d.pid] == 1 ? "lasso" : "unlasso"
            });

          for (let i in selectData) {
            for (let j in selectData[i]) {
              // console.log("#sel" + i + (j))
              // console.log(parseInt(d3.select("#sel" + i + (j)).attr("dmax")))
              if (d3.select("#sel" + i + (j))._groups[0][0] == null)
                continue;
              let yAxis = d3.scaleLinear()
                .domain([0, parseInt(d3.select("#sel" + i + (j)).attr("dmax"))])
                .range([d3.select("#sel" + i + (j)).attr("hisHeight") - 42, 0])
              d3.select("#sel" + i + (j))
                .transition().duration(500)
                .attr('y', yAxis(selectData[i][j].cnt) + 20)
                .attr("height", d3.select("#sel" + i + (j)).attr("hisHeight") - 42 - yAxis(selectData[i][j].cnt));
            }
          }

          _this.updateTree(treeCnt, treeData, sumTree);

          select_path = "";
          end_path = "";
          origin_circle = [];
          target_circle = [];
          closePathDistance = 300;
          polygon = new Array();
          d3.selectAll(".select_circle").remove();
          _this.removeSelect(_this.typeName)
        }
      }

      let drag = d3.drag()
        .on('start', dragStarted)
        .on('drag', dragged)
        .on('end', dragEnded);
      // console.log(drag);

      d3.select('#mainViewPicSvg').call(drag);
    },
    /**
     * @description: mouseover on a node or click
     * @param {*} selData the selected node
     * @param {*} typeName Feature Group
     * @return {*}
     */
    setSelect(selData, typeName) {
      console.log(selData);
      for (let i in typeName) {
        // console.log(selData[this.typeName[i].toLowerCase()])
        document.getElementById(typeName[i] + 'Table').innerHTML = Math.round((selData[typeName[i].toLowerCase()] * 100000)) / 100000;
      }
      d3.select("#nodePic").attr("src", '/src/assets' + selData.path.slice(1));
      let pw = document.getElementById("isChoose").offsetWidth;
      let ph = document.getElementById("isChoose").offsetHeight;
      // console.log(ph, pw);
      if (ph * 2 > pw)
        d3.select("#nodePic").attr("style", 'width: 95%; border: solid 1px rgba(0, 0, 0, 0.5); transform: translate(0,0)');
      else
        d3.select("#nodePic").attr("style", 'height: 95%; border: solid 1px rgba(0, 0, 0, 0.5); transform: translate(0,0)');
      // d3.select('#nodePic').attr("sid", 0);
    },
    /**
     * @description: mouseout
     * @param {*} typeName Feature Group
     * @return {*}
     */
    removeSelect(typeName) {
      for (let i in typeName) {
        // console.log(selData[this.typeName[i].toLowerCase()])
        document.getElementById(typeName[i] + 'Table').innerHTML = '';
      }
      // console.log(d3.select("#nodePic").attr("sid"))
      d3.select("#nodePic").attr("style", '');

      d3.select("#nodePic").attr("src", '');
      d3.selectAll(".gal_img").attr("src", '');
      d3.selectAll(".closeNode").style("border", "none");
      d3.selectAll(".select_circle").remove();
      d3.selectAll("tr").style("background-color", "white")
    },
    /**
     * @description: update dendrogram
     * @param {Array} treeData data of the tree
     * @param {Int} sumTree Number of all selected elements
     * @return {*}
     */
    updateTree(treeCnt, treeData, sumTree) {
      //this.$emit('updateTree', treeData, sumTree);
      let nameorder1 = ["circle", "map", "line", "area", "bar", "net", "point", "diagram", "matrix", "table", "word"];
      console.log(treeCnt["area"]);
      console.log(nameorder1[DAorder[0]]);
      var name1 = nameorder1[DAorder[0]];
      console.log(name1)
      console.log(treeCnt[name1])
      console.log(typeof treeCnt)
      for (let i = 0; i < DAorder.length; i++) {
        d3.select("#widget" + nameorder1[DAorder[i]])
          .attr("height", 190 * treeCnt[nameorder1[DAorder[i]]]["value"] / sumTree)
          .attr("y", 130 - 190 * treeCnt[nameorder1[DAorder[i]]]["value"] / sumTree);
        d3.select("#widgetCount" + nameorder1[DAorder[i]])
          .attr("y", 110 - 190 * treeCnt[nameorder1[DAorder[i]]]["value"] / sumTree)
          .text(treeCnt[nameorder1[DAorder[i]]]["value"])
      }
      //  d3.select("#widgetcircle")
      //   .attr("height", 290*treeCnt["circle"]["value"]/sumTree)
      //   .attr("y", 130-290*treeCnt["circle"]["value"]/sumTree)
    },
    /**
     * @description: update gallery 
     * @param {Array} data close node data
     * @return {*}
     */
    updateGallery(data) {
      this.$emit('updateGallery', data);
      d3.selectAll(".closeNode").style("border", "solid 1px rgba(0, 0, 0, 0.5)");
    },
    /**
     * @description: change gallery type
     * @param {*} data Cosine / Projection
     * @return {*}
     */
    setGalleryType(data) {
      this.distanceType = data;
    },
    /**
     * @description: set selected node
     * @param {*} data the selected node data
     * @return {*}
     */
    setSelectNode(data) {
      this.selectNode = data;
    },
    /**
     * @description: Query picture and show on system
     * @param {*} data query picture's data
     * @return {*}
     */
    setQuery(data) {
      let tempData = this.processedData;
      console.log(tempData[0].class)
      // console.log(data)
      tempData.push(data);
      let allData = this.getMainData(tempData, this.dimensions, DAorder);
      let nodeData = allData.pop();
      console.log(allData[0].class)
      console.log(nodeData)
      // tempData
      this.selectNode = nodeData;
      console.log("smooth")
    }
  },
  watch: {

    fileP: {
      handler(newValue, oldValue) {

        this.clearBrush();
        this.drawMain(this.fileP.filePath, this.dimensions, DAorder);
        // this.removeSelect();
        isRedraw = false;
      },
      deep: true
    },
    distanceType: {
      handler(newValue, oldValue) {
        if (this.selectNode != 0) {
          let close_node = this.closeNode(this.processedData, this.selectNode, this.distanceType);
          this.updateGallery(close_node);
        }
      }
    },
    selectNode: {
      handler(newValue, oldValue) {
        d3.selectAll(".select_circle").remove();
        // console.log(this.selectNode);
        this.clickNode(this.selectNode);
        // if (this.selectNode.pid > 0)
        //   this.setSelect(this.selectNode, this.typeName);
        let close_node = this.closeNode(this.processedData, this.selectNode, this.distanceType);
        this.updateGallery(close_node);
      }
    }
  }
}
</script>

<style>
.contour {
  mix-blend-mode: multiply;
}

.lasso path {
  stroke: #2378ae;
  stroke-width: 3;
  /* stroke-dasharray: 4, 4; */
}

.lasso #drawn {
  fill-opacity: 0.05;
}

.lasso #loop_close {
  /* fill: none;
  stroke-dasharray: 4, 4; */
  stroke: #2378ae;
  stroke-width: 3;
}

.lasso #origin {
  fill: rgb(180, 180, 180);
  fill-opacity: 0.5;
}

#tooltip {
  /* background-color: gray; */
  height: 70px;
  position: relative;
  width: 150px;
  /* border-radius: 15px; */
}

/* #tooltip:after {
  content: "";
  position: absolute;
  border: 8px solid transparent;
  border-top-color: rgb(99, 99, 99);

  top: calc(100% + 4px);
  left: 22px;
} */
</style>