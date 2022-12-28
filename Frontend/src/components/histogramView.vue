<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-30 23:33:59
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div>
    <div id="titleBar">
      <span style="text-align:center">{{ viewName }}</span>
      <!-- <button style="float:right" @click="clearBrush($event)">Clear Brush</button> -->
    </div>
    <div id="mainHistogram" second="false">
      <!-- <div
        v-for="(ty, index) in typeName"
        :key="ty"
        :id="'His' + ty"
        v-bind:style="{ border: 'solid 1px rgba(0, 0, 0, 0.5)', width: wd, height:hs, position: 'absolute', left: '10px', transform: 'translate(' + (index == 10 ? 'calc(50% + 10px)' : index % 2 ? 'calc(100% + 10px)' : '0') + ',' + 'calc(' + ((Math.floor(index / 2)) * 100) + '% + ' + ((Math.floor(index / 2)) * 5) + 'px' + ' + 5px)' + ')' }"
      > -->
      <!-- <div
        v-for="(ty, index) in typeName"
        :key="ty"
        :id="'His' + ty"
        v-bind:style="{ overflow: 'visible', width: wd, height:hs, position: 'absolute', left: '13px', transform: 'translate(' + (index == 9 ? 'calc(50% + 12px)' : index == 10 ? 'calc(150% + 24px)' : index % 3 == 0 ? '0' : index % 3 == 1 ? 'calc(100% + 12px)' : 'calc(200% + 24px)') + ',' + 'calc(' + ((Math.floor(index / 3)) * 100) + '% + ' + ((Math.floor(index / 3)) * 12) + 'px' + ' + 12px)' + ')' }"
      > -->
      <div
        v-for="(ty, index) in typeName"
        :key="ty"
        :id="'His' + ty"
        v-bind:style="{ overflow: 'visible', width: wd, height:hs, position: 'absolute', left: '13px', transform: 'translate(' + (index % 4 == 0 ? '0' : index % 4 == 1 ? 'calc(100% + 12px)' : index % 4 == 2 ? 'calc(200% + 24px)': 'calc(300% + 36px)') + ',' + 'calc(' + ((Math.floor(index / 4)) * 100) + '% + ' + ((Math.floor(index / 4)) * 22) + 'px' + ' + 15px)' + ')' }"
      >
      <!-- border: 'solid 1px rgba(127, 127, 127, 0.5)' -->
      </div>
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import { dataService } from '../service';
var previous_selected={};
var isSecondFiltering=false;
export default {
  mounted () {
    // dataService.fetchData({ 'filePath': this.fileP.filePath }, fileData => {
    //   console.log(11111);

    //   // this.drawHistogram(fileData.data.data, this.typeName);
    // });
    this.typeName.forEach(d => {
      this.createSVG(d);
    })

    this.drawHistogram(this.fileP.filePath, this.typeName);
  },
  data () {
    return {
      viewName: "Embedding Histogram",
      typeName: ["Area", "Bar", "Circle", "Diagram", "Line", "Map", "Matrix", "Net", "Point", "Table", "Word"],
      // hs: "calc(16.6% - 12px)",
      // hs: "calc(23.6% - 12px)",
      hs: "calc(28.6% - 12px)",
      // wd: "calc(50% - 15px)",
      // wd: "calc(33% - 15px)",
      wd: "calc(25% - 15px)",
      selectType: '',
      xAxis: undefined,
      yAxis: {},
      hisWidth: 0,
      hisHeight: 0,
      levelCluster: {
        "Beagle": ['Circle', 'Map', 'Line', 'Area', 'Bar', 'Net', 'Point', 'Diagram', 'Matrix', 'Table', 'Word'],
        "VIS": ["Map", "Circle", "Bar", "Point", "Line", "Diagram", "Matrix", "Net", "Area", "Table", "Word"],
        "Data": ["Area", "Line", "Bar", "Point", "Diagram", "Matrix", "Net","Circle",'Table', 'Word',"Map"]
      },

    };
  },
  inject: ['fileP'], // get file path from visView.vue
  methods: {
    /**
     * @description: create svg for every histogram
     * @param {*} hisType Feature
     * @return {*}
     */    
    createSVG: function (hisType) {
      d3.select("#" + hisType + 'Svg').remove();
      const hisHeight = document.getElementById(('His' + hisType)).offsetHeight;
      const hisWidth = document.getElementById(('His' + hisType)).offsetWidth;
      this.hisHeight = hisHeight;
      this.hisWidth = hisWidth;
      d3.select('#His' + hisType)
        .append('svg')
        .attr('id', hisType + 'Svg')
        .attr('width', hisWidth)
        .attr('height', hisHeight)
        .style('border', 'solid 1px rgba(127, 127, 127, 0.5)')
        .style('overflow', 'visible')
      d3.select('#' + hisType + 'Svg')
        .append('rect')
        // .attr('y', 15)
        .attr('y', -9)
        .attr('x', hisWidth / 2-30)
        .attr('width', 60)
        .attr('height', 20)
        .style('fill','white')

      d3.select('#' + hisType + 'Svg')
        .append('text')
        .text(hisType)
        .attr('font-size', 15)
        .attr('text-anchor', 'middle')
        // .attr('y', 15)
        .attr('y', 5)
        .attr('x', hisWidth / 2)
    },
    /**
     * @description: data processing and use function
     * @param {String} filePath: which file will be used, selected in modelView.vue
     * @param {Array} hisTypeArray: Feature Group
     * @return {*}
     */
    drawHistogram: function (filePath, hisTypeArray) {
      d3.csv(filePath).then((fileData) => {
        hisTypeArray.forEach(hisType => {
          // index name need small letters
          let hisTag = hisType.toLowerCase();
          const hisData = new Object();
          for (let i = 0; i < fileData.length; ++i) {
            let indexNum = Math.floor(parseFloat(fileData[i][hisTag]) * 10);
            if (indexNum == 10) indexNum--; // let 1 to 0.9 ~ 1
            if (indexNum == 0) continue;
            if (typeof (hisData[indexNum]) == 'undefined') {
              hisData[indexNum] = { cnt: 0, items: [] };
            }
            hisData[indexNum].cnt++;
            hisData[indexNum].items.push(fileData[i]);
          }

          // remove old View
          d3.select("#his_g_" + hisType).remove();
          // define new View
          d3.select("#" + hisType + "Svg")
            .append('g')
            .attr("id", "his_g_" + hisType);

          this.drawRectAndAxis(hisData, hisType);
          this.drawSelectRect(hisData, hisType);
          this.RectBrush(hisData, hisType);
          // this.allHisData[hisType] = hisData;
          // d3.select("#selCircle8").transition().duration(2000).attr('y', 20).attr("height", 70);
        })
      });
    },
    /**
     * @description: draw bar charts and x/y axises
     * @param {Array} hisData bar chart data
     * @param {String} hisType Feature
     * @return {*}
     */    
    drawRectAndAxis: function (hisData, hisType) {
      // remove old View
      d3.select("#his_rect_g_" + hisType).remove();
      // define new View
      const his_g = d3.select("#his_g_" + hisType)
        .append('g')
        .attr("id", "his_rect_g_" + hisType);

      const hisArray = new Array();

      for (let i in hisData)
        hisArray.push(hisData[i].cnt);

      const xAxis = d3.scaleLinear()
        .domain([0.1, 1.0])
        .range([0, this.hisWidth - 45])
      const yAxis = d3.scaleLinear()
        .domain([0, d3.max(hisArray)])
        .range([this.hisHeight - 42, 0]);
      this.xAxis = xAxis;
      this.yAxis[hisType] = yAxis;

      his_g.append('g').attr("class","grid")
      .call(d3.axisLeft(yAxis).ticks(4).tickSize(-this.hisWidth + 45).tickFormat(""))
      .attr("transform", `translate(${35}, ${20})`);
      
      his_g.append('g')
        .selectAll("#hisRect" + hisType)
        .attr('id', "hisRect" + hisType)
        .data(hisArray)
        .enter()
        .append('rect')
        .attr("dmax", d3.max(hisArray))
        .attr('x', (d, i) => {
          return this.xAxis((i + 1) / 10) + 35 + 5;
        })
        // .attr('x', (d, i) => {
        //   return this.xAxis((i + 1) / 10) + 35 + 35;
        // })
        .attr('y', (d, i) => {
          return this.yAxis[hisType](d) + 20;
        })
        .attr('height', d => {
          return this.hisHeight - 42 - this.yAxis[hisType](d)
        })
        // .attr('width', 17)
        .attr('width', 10)
        .attr('fill', "rgb(198, 198, 198)");
      // draw Axis
      his_g.append('g')
        .call(d3.axisBottom(xAxis).ticks(5))
        .attr("transform", `translate(${35}, ${this.hisHeight - 22})`);
      his_g.append('g')
        .call(d3.axisLeft(yAxis).ticks(4))
        // .call(d3.axisLeft(yAxis))
        .attr("transform", `translate(${35}, ${20})`);

    },
    /**
     * @description: draw bar charts which be select. I draw them without height. When I select some data, I will change the height of them.
     * @param {*} hisData bar chart data
     * @param {*} hisType Feature
     * @return {*}
     */    
    drawSelectRect: function (hisData, hisType) {
      // remove old View
      d3.select("#his_sel_g_" + hisType).remove();
      // define new View
      const his_g = d3.select("#his_g_" + hisType)
        .append('g')
        .attr('class', '#his_sel_g')
        .attr("id", "his_sel_g_" + hisType);

      const hisArray = new Array();
      for (let i in hisData)
        hisArray.push(hisData[i].cnt);
      // console.log()
      his_g.append('g')
        .selectAll("#hisSelRect" + hisType)
        .attr('id', "hisSelRect" + hisType)
        .data(hisArray)
        .enter()
        .append('rect')
        .attr("dmax", this.yAxis[hisType].domain()[1])
        .attr("hisHeight", this.hisHeight)
        .attr("class","selrect")
        .attr("id", (d, i) => {
          return "sel" + hisType + (i + 1);
        })
        .attr('x', (d, i) => {
          return this.xAxis((i + 1) / 10) + 40;
        })
        .attr('y', (d, i) => {
          return this.hisHeight - 20;
        })
        .attr('height', d => {
          return 0;
        })
        // .attr('width', 17)
        .attr('width', 10)
        // .attr('fill', "orange");
        .attr('fill', "#95BCBA");
    },
    /**
     * @description: second step of filtering
     * @param {*} hisData bar chart data
     * @param {*} hisType Feature
     * @return {*}
     */  
    FilterIter: function (hisData, hisType)
    {

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
      isSecondFiltering=false;
      d3.select("#mainHistogram").attr("second","false");
    },
    /**
     * @description: a brush. Select areas in the bar chart 
     * @param {*} hisData bar chart data
     * @param {*} hisType Feature
     * @return {*}
     */    

    RectBrush (hisData, hisType) {

      let _this = this;
      const hisArray = new Array();
      for (let i in hisData)
        hisArray.push(hisData[i].cnt);
      if (d3.select("#mainHistogram").attr("second")=="false")
      {
        isSecondFiltering=false;
      }
      else
      {
        isSecondFiltering=true;
      }
      const brush = d3.brush()
        .extent([
          [30, 15],
          [_this.hisWidth - 5, _this.hisHeight - 10]
        ])
        .on('start', function ({ selection }) {
          if (selection != null && isSecondFiltering==false) {
            d3.selectAll('.brush_rect').remove();
          }
        })
        // .on('brush', brushing)
        .on('end', brushed);
      // console.log(hisData)
      const brush_g = d3.select("#his_g_" + hisType)
        .append('g')
        .attr('id', 'brush_g' + hisType)
        .call(brush);

      // I really don't like programing this function, but it's the method which can clear the brush.
      function brushed ({ selection }) {
        //console.log(isSecondFiltering)
        // console.log(previous_selected)
        
        if (selection != null) {
          d3.selectAll(".select_circle").remove();
          d3.select("#mainScatter_g").attr("afterhis","true")
          console.log(previous_selected)
          if (d3.select("#mainHistogram").attr("second")=="false")
          {
            isSecondFiltering=false;
          }
          else
          {
            isSecondFiltering=true;
          }
          if (isSecondFiltering==false){
          const [
            [x0, y0],
            [x1, y1]
          ] = selection;
          d3.select('#his_g_' + hisType)
            .append("rect")
            .attr('class', 'brush_rect')
            .attr('x', x0)
            .attr('y', y0)
            .attr('width', x1 - x0)
            .attr('height', y1 - y0)
            .attr('fill', 'white')
            .attr('fill-opacity', 0)
            .attr('stroke', '#2378ae')
            .attr('stroke-dasharray', '4, 4')
            .attr('stroke-width', 3);

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
          for (let i = 0; i < 9; ++i) {
            if (x0 < _this.xAxis((i + 1) / 10) + 35 + 5 && _this.xAxis((i + 1) / 10) + 35 + 5 < x1) {
              hisData[i + 1].items.forEach(d => {
                pidScatter[d.pid] = 1;
                // d3.select("#rad_cir" + d.pid).attr('opacity', 1).attr('r', 4);
                let lassoflag=d3.select("#cir" + d.pid).attr("state")
                _this.typeName.forEach(hisTag => {
                  let indexNum = Math.floor(parseFloat(d[hisTag.toLowerCase()]) * 10);
                  if (indexNum == 10) indexNum--; // let 1 to 0.9 ~ 1
                  if (indexNum != 0 && (lassoflag=="bflasso"||lassoflag=="lasso")) {
                    selectData[hisTag][indexNum].cnt++;
                  }
                })
                // console.log(treeCnt)
                // console.log(d['class'])
                if (lassoflag=="bflasso"||lassoflag=="lasso")
                {treeCnt[d['class']].value++;}
              })
            }
          }
          previous_selected=pidScatter;
          isSecondFiltering=true;
          d3.select("#mainHistogram").attr("second","true")

          console.log(d3.select("#cir1000").attr("state"))
          d3.selectAll('.rad_cir')
            .attr('r', d => {
              if (d3.select("#cir"+d.pid).attr("state")=="bflasso")
              {return pidScatter[d.pid] == 1 ? 2 : 0;}
              else if (d3.select("#cir"+d.pid).attr("state")=="unlasso")
              {
                return 0;
              }
              else
              {
                return pidScatter[d.pid] == 1 ? 2 : 0;
              }
            })
            .attr('show',d =>{
              if (d3.select("#cir"+d.pid).attr("state")=="bflasso")
              {return pidScatter[d.pid] == 1 ? "true" : "false";}
              else if (d3.select("#cir"+d.pid).attr("state")=="unlasso")
              {
                return "false";
              }
              else
              {
                return pidScatter[d.pid] == 1 ? "true" : "false";
              }
            })
            .attr('hisShow',d =>{
              if (d3.select("#cir"+d.pid).attr("state")=="bflasso")
              {return pidScatter[d.pid] == 1 ? "true" : "false";}
              else if (d3.select("#cir"+d.pid).attr("state")=="unlasso")
              {
                return "false";
              }
              else
              {
                return pidScatter[d.pid] == 1 ? "true" : "false";
              }
            })
          // console.log(selectData)
          for (let i in selectData) {
            for (let j in selectData[i]) {
              d3.select("#sel" + i + (j))
                .transition().duration(1000)
                .attr('y', _this.yAxis[i](selectData[i][j].cnt) + 20)
                .attr("height", _this.hisHeight - 42 - _this.yAxis[i](selectData[i][j].cnt));
            }
          }
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
          // _this.updateTree(treeData, sumTree);
          // clear brush
          d3.select(this).call(brush.move, null);
        }
              else 
      {
            // console.log(previous_selected)
            // if (selection != null) {
              console.log(isSecondFiltering)
          const [
            [x0, y0],
            [x1, y1]
          ] = selection;
          d3.select('#his_g_' + hisType)
            .append("rect")
            .attr('class', 'brush_rect')
            .attr('x', x0)
            .attr('y', y0)
            .attr('width', x1 - x0)
            .attr('height', y1 - y0)
            .attr('fill', 'white')
            .attr('fill-opacity', 0)
            .attr('stroke', '#2378ae')
            .attr('stroke-dasharray', '4, 4')
            .attr('stroke-width', 3);

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
          console.log(previous_selected)
          isSecondFiltering=false
          d3.select("#mainHistogram").attr("second","false")

          for (let i = 0; i < 9; ++i) {
            if (x0 < _this.xAxis((i + 1) / 10) + 35 + 5 && _this.xAxis((i + 1) / 10) + 35 + 5 < x1) {
              hisData[i + 1].items.forEach(d => {
                if (previous_selected[d.pid]==1)
                {pidScatter[d.pid] = 1;
                let lassoflag=d3.select("#cir" + d.pid).attr("state")
                // d3.select("#rad_cir" + d.pid).attr('opacity', 1).attr('r', 4);
                _this.typeName.forEach(hisTag => {
                  let indexNum = Math.floor(parseFloat(d[hisTag.toLowerCase()]) * 10);
                  if (indexNum == 10) indexNum--; // let 1 to 0.9 ~ 1
                  if (indexNum != 0 && (lassoflag=="bflasso"||lassoflag=="lasso")) {
                    selectData[hisTag][indexNum].cnt++;
                  }
               
                })
                
                // console.log(treeCnt)
                // console.log(d['class'])
                if (lassoflag=="bflasso"||lassoflag=="lasso")
                {treeCnt[d['class']].value++;}
                }
              })
            }
          }
          // previous_selected=pidScatter;
          // isSecondFiltering=true;
          // d3.selectAll('.rad_cir')
          //   .attr('r', d => {
              
          //     return pidScatter[d.pid] == 1 ? 2 : 0;
          //   })
          //   .attr('show',d =>{
          //     return pidScatter[d.pid] == 1 ? "true":"false"
          //   })
          d3.selectAll('.rad_cir')
            .attr('r', d => {
              if (d3.select("#cir"+d.pid).attr("state")=="bflasso")
              {return pidScatter[d.pid] == 1 ? 2 : 0;}
              else if (d3.select("#cir"+d.pid).attr("state")=="unlasso")
              {
                return 0;
              }
              else
              {
                return pidScatter[d.pid] == 1 ? 2 : 0;
              }
            })
            .attr('show',d =>{
              if (d3.select("#cir"+d.pid).attr("state")=="bflasso")
              {return pidScatter[d.pid] == 1 ? "true" : "false";}
              else if (d3.select("#cir"+d.pid).attr("state")=="unlasso")
              {
                return "false";
              }
              else
              {
                return pidScatter[d.pid] == 1 ? "true" : "false";
              }
            })
            .attr('hisShow',d =>{
              if (d3.select("#cir"+d.pid).attr("state")=="bflasso")
              {return pidScatter[d.pid] == 1 ? "true" : "false";}
              else if (d3.select("#cir"+d.pid).attr("state")=="unlasso")
              {
                return "false";
              }
              else
              {
                return pidScatter[d.pid] == 1 ? "true" : "false";
              }
            })
          // console.log(selectData)
          for (let i in selectData) {
            for (let j in selectData[i]) {
              d3.select("#sel" + i + (j))
                .transition().duration(1000)
                .attr('y', _this.yAxis[i](selectData[i][j].cnt) + 20)
                .attr("height", _this.hisHeight - 42 - _this.yAxis[i](selectData[i][j].cnt));
            }
          }
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
          // _this.updateTree(treeData, sumTree);
          // clear brush
          d3.select(this).call(brush.move, null);
        
      }
      }

    }
    },
    /**
     * @description: update Dendrogram
     * @param {Array} treeData data of the tree
     * @param {Int} sumTree Number of all selected elements
     * @return {*}
     */    
    updateTree (treeData, sumTree) {
      this.$emit('updateTree', treeData, sumTree);
    }
  },
  watch: {
    fileP: {
      handler (newValue, oldValue) {
        console.log(newValue)
        this.drawHistogram(this.fileP.filePath, this.typeName);
      },
      deep: true
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
.selection {
  fill: none;
  stroke: #2378ae;
  stroke-width: 3;
  stroke-dasharray: 4, 4;
}
</style>