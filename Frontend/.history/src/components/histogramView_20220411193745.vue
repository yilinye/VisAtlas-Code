<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-11 19:37:34
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
      :id="'His' + ty"
      v-bind:style="{ border: 'solid 1px', width: wd, height:hs, position: 'absolute', left: '2px', transform: 'translate(' + (index == 10 ? 'calc(50% + 5px)' : index % 2 ? 'calc(100% + 5px)' : '0') + ',' + 'calc(' + ((Math.floor(index / 2)) * 100) + '% + ' + ((Math.floor(index / 2)) * 3) + 'px' + ' + 5px)' + ')' }"
    >

      <svg
        width="100%"
        height="100%"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
      >

        <rect
          v-for="(c,j) in typeName"
          :key="j"
          :x="20"
          y="20"
          rx="20"
          ry="20"
          width="25"
          height="10"
          :style="{fill:'red', stroke:'black',
strokeWidth:'5',opacity:'0.5', transform:'translate(j*100,0)'}"
        />

      </svg>
    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
export default {
  mounted () {
    // this.typeName.forEach(d => {
    //   this.createSVG(d);
    // })
    // this.drawHistogram(this.fileP.filePath, this.typeName);
  },
  data () {
    return {
      viewName: "Embedding Histogram",
      typeName: ["Area", "Bar", "Circle", "Diagram", "Line", "Map", "Matrix", "Net", "Point", "Table", "Word"],
      hs: "calc(16.6% - 11px)",
      wd: "calc(50% - 7px)",
      xAxis: 0,
      yAxis: 0
    };
  },
  inject: ['fileP'],
  methods: {
    createSVG: function (hisType) {
      const hisHeight = document.getElementById(('His' + hisType)).offsetHeight;
      const hisWidth = document.getElementById(('His' + hisType)).offsetWidth;
      d3.select('#His' + hisType)
        .append('svg')
        .attr('id', hisType + 'Svg')
        .attr('width', hisWidth)
        .attr('height', hisHeight)
      d3.select('#' + hisType + 'Svg')
        .append('text')
        .text(hisType)
        .attr('font-size', 15)
        .attr('text-anchor', 'middle')
        .attr('y', 15)
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

          this.RectBrush(hisData, hisType);
          this.drawRectAndAxis(hisData, hisType);
          this.drawSelectRect(hisData, hisType);
          // d3.select("#selCircle8").transition().duration(2000).attr('y', 20).attr("height", 70);
        })
      });
    },
    drawRectAndAxis: function (hisData, hisType) {
      const hisHeight = document.getElementById(('His' + hisType)).offsetHeight;
      const hisWidth = document.getElementById(('His' + hisType)).offsetWidth;

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
        .range([0, hisWidth - 45])
      const yAxis = d3.scaleLinear()
        .domain([0, d3.max(hisArray)])
        .range([hisHeight - 40, 0]);

      his_g.append('g')
        .selectAll("#hisRect" + hisType)
        .attr('id', "hisRect" + hisType)
        .data(hisArray)
        .enter()
        .append('rect')
        .attr('x', (d, i) => {
          return xAxis((i + 1) / 10) + 40;
        })
        .attr('y', (d, i) => {
          return yAxis(d) + 20;
        })
        .attr('height', d => {
          return hisHeight - 42 - yAxis(d)
        })
        .attr('width', 12)
        .attr('fill', "rgb(198, 198, 198)");
      // draw Axis
      his_g.append('g')
        .call(d3.axisBottom(xAxis).ticks(5))
        .attr("transform", `translate(${35}, ${hisHeight - 22})`);
      his_g.append('g')
        .call(d3.axisLeft(yAxis).ticks(5))
        .attr("transform", `translate(${35}, ${18})`);
    },
    drawSelectRect: function (hisData, hisType) {
      const hisHeight = document.getElementById(('His' + hisType)).offsetHeight;
      const hisWidth = document.getElementById(('His' + hisType)).offsetWidth;
      // remove old View
      d3.select("#his_sel_g_" + hisType).remove();
      // define new View
      const his_g = d3.select("#his_g_" + hisType)
        .append('g')
        .attr("id", "his_sel_g_" + hisType);

      const hisArray = new Array();
      for (let i in hisData)
        hisArray.push(hisData[i].cnt);
      const xAxis = d3.scaleLinear()
        .domain([0.1, 1.0])
        .range([0, hisWidth - 45])
      const yAxis = d3.scaleLinear()
        .domain([0, d3.max(hisArray)])
        .range([hisHeight - 42, 0]);

      his_g.append('g')
        .selectAll("#hisSelRect" + hisType)
        .attr('id', "hisSelRect" + hisType)
        .data(hisArray)
        .enter()
        .append('rect')
        .attr("id", (d, i) => {
          return "sel" + hisType + i;
        })
        .attr('dmax', d3.max(hisArray))
        .attr('x', (d, i) => {
          return xAxis((i + 1) / 10) + 40;
        })
        .attr('y', (d, i) => {
          return hisHeight - 20;
        })
        .attr('height', d => {
          return 0;
        })
        .attr('width', 12)
        .attr('fill', "orange");
    },
    RectBrush (hisData, hisType) {
      const hisHeight = document.getElementById(('His' + hisType)).offsetHeight;
      const hisWidth = document.getElementById(('His' + hisType)).offsetWidth;

      const hisArray = new Array();
      for (let i in hisData)
        hisArray.push(hisData[i].cnt);
      const xAxis = d3.scaleLinear()
        .domain([0.1, 1.0])
        .range([0, hisWidth - 45])
      const yAxis = d3.scaleLinear()
        .domain([0, d3.max(hisArray)])
        .range([hisHeight - 42, 0]);

      const brush = d3.brush()
        .extent([
          [30, 15],
          [hisWidth - 5, hisHeight - 10]
        ])
      // .on('brush', brushing)
      // .on('end', brushed);
      const brush_g = d3.select("#his_g_" + hisType)
        .append('g')
        .attr('id', 'brush_g')
        .call(brush)
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
</style>