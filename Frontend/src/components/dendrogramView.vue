<template>
  <div style="height: 100%; width: 100%;">
    <div id="titleBar">
      {{ viewName }}
    </div>
    <div
      id="dendrogramViewPic"
      :style="{height: ht}"
    >

    </div>
  </div>
</template>

<script>
import * as d3 from 'd3';
export default {
  mounted () {
    this.createSVG();
    this.drawDedrogram(this.fileP.filePath);
  },
  data () {
    return {
      viewName: "Embedding Dendrogram",
      dendWidth: 0,
      dendHeight: 0,
      ht: "calc(100% - 30px)",
      levelCluster: {
        "Beagle": ['Circle', 'Map', 'Line', 'Area', 'Bar', 'Net', 'Point', 'Diagram', 'Matrix', 'Table', 'Word'],
        "VIS": ["Map", "Circle", "Bar", "Point", "Line", "Diagram", "Matrix", "Net", "Area", "Table", "Word"],
        "Data": ["Area", "Line", "Bar", "Point"]
      },
      colormap: { "circle": "#4A80CE", "point": "#FF931D", "net": "#42B287", "line": "#E5CD3C", "area": "#FF6224", "bar": "#A9DB63", "map": "#C192EA", "matrix": "#1C9AB7", "table": "#FF9896", "word": "#FFB839", "diagram": "#0ED88F" },
    }
  },
  inject: ['fileP'],
  methods: {
    /**
     * @description: create a svg
     * @param {*}
     * @return {*}
     */    
    createSVG () {
      const dendHeight = document.getElementById('dendrogramViewPic').offsetHeight;
      const dendWidth = document.getElementById('dendrogramViewPic').offsetWidth;
      this.dendHeight = dendHeight;
      this.dendWidth = dendWidth;
      d3.select("#dendrogramViewPicSvg").remove();
      d3.select("#dendrogramViewPic")
        .append('svg')
        .attr('id', 'dendrogramViewPicSvg')
        .attr('height', dendHeight)
        .attr('width', dendWidth);
    },
    /**
     * @description: update dendrogram
     * @param {Array} treeData data of the tree
     * @param {Int} sumTree Number of all selected elements
     * @return {*}
     */
    updateTree (treeData, sumTree) {
      this.$emit('updateTree', treeData, sumTree);
    },
    /**
     * @description: data process and call function
     * @param {*} filePath selected file path
     * @return {*}
     */    
    drawDedrogram (filePath) {
      let levelType = undefined;

      if (filePath[13] == 'B') {
        levelType = this.levelCluster["Beagle"];
      }

      if (filePath[13] == 'v') {
        levelType = this.levelCluster["VIS"];
      }

      if (filePath[13] == 'd') {
        levelType = this.levelCluster["Data"];
      }
      d3.csv(filePath).then((fileData) => {
        // console.log(fileData);
        let tempLevel = new Object();
        // console
        for (let i in levelType) tempLevel[levelType[i].toLowerCase()] = 0;
        for (let i = 0; i < fileData.length; ++i) {
          // if (i < 10) console.log(fileData[i]['class']);
          tempLevel[fileData[i]['class']]++;
        }
        let treeData = new Array();
        let sumTree = 0;
        for (let i in tempLevel) {
          if (tempLevel[i] > 0) {
            treeData.push({
              value: tempLevel[i],
              id: i,
              top: sumTree
            });
            sumTree += tempLevel[i];
          }
        }
        this.drawTree(treeData, sumTree);
        console.log("draw once");
        // this.drawTree([{value: 80, id:'circle', top: 0}, {value: 20, id: 'net', top: 80}], 100)
        // this.drawTree([{ value: 100, id: 'circle', top: 0 }], 100)
      })
    },
    /**
     * @description: draw dendrogram
     * @param {Array} treeData data of the tree
     * @param {Int} sumTree Number of all selected elements
     * @return {*}
     */    
    drawTree (treeData, sumTree) {
      let _this = this;
      d3.select('#tree_g').remove();
      const tree_g = d3.select('#dendrogramViewPicSvg')
        .append('g')
        .attr('id', 'tree_g');

      const yAxisTop = d3.scaleLinear()
        .domain([0, sumTree])
        .range([5, this.dendHeight - 5]);
      const yAxis = d3.scaleLinear()
        .domain([0, sumTree])
        .range([0, this.dendHeight - 10]);

      let tree_rect_g = tree_g.append('g')
        .selectAll("#treeRect")
        .attr('id', 'treeRect')
        .data(treeData)
        .enter()
      tree_rect_g.append('rect')
        .attr('x', this.dendWidth - 60)
        .attr('y', d => yAxisTop(d.top))
        .attr('width', 50)
        .attr('height', d => yAxis(d.value))
        .attr('fill', d => this.colormap[d.id])
        .on("click", d => {
          let treeData1 = new Array();
          let sumTree1 = 0;
          // console.log(treeData)
          console.log(d.srcElement.__data__)
          let dat=d.srcElement.__data__
          for (let k=0;k<treeData.length;k++)
          {
            // console.log(treeData[k])
            // console.log(d.id)
            
            if (treeData[k].id==dat.id)
            {
              treeData[k].top=sumTree1
              treeData1.push(treeData[k])
              sumTree1+=dat.value
            }
          }
          console.log(treeData1)
          this.updateTree(treeData1, sumTree1);
          d3.selectAll('.rad_cir')
          .attr('r', d1 => {
            if (d3.select("#cir"+d1.pid).attr("state")=="bflasso" && d3.select("#cir"+d1.pid).attr("show")=="true")
            {return d1.class == dat.id ? 2 : 0;}
            else if (d3.select("#cir"+d1.pid).attr("state")=="unlasso")
            {
              return 0;
            }
            else
            {
              return d1.class == dat.id && d3.select("#cir"+d1.pid).attr("show")=="true"? 2 : 0;
            }
          })
        })
      // .attr('fill-opacity', 0.7)
      tree_rect_g.append('text')
        .attr('x', this.dendWidth - 60)
        .attr('y', d => {
          return yAxisTop(d.top + d.value / 2);
        })
        .attr('text-anchor', 'middle')
        .attr('dx', 24)
        .attr('dy', 7)
        .attr('font-size', 14)
        .text(d => {
          if (yAxis(d.value) > 24)
            return d.value;
        });
      let scatterData = [];
      let lineData = [];
      let textData = [];
      treeData.forEach(d => {
        scatterData.push({
          cx: this.dendWidth - 60 - 1,
          cy: d.top + d.value / 2
        });
      });
      let lastScatterPos = scatterData[treeData.length - 1];
      if (treeData.length > 1) {
        lineData.push({
          x1: lastScatterPos.cx,
          y1: lastScatterPos.cy,
          x2: lastScatterPos.cx - ((this.dendWidth - 100) / (treeData.length - 1)),
          y2: lastScatterPos.cy
        });
        textData.push({
          x: (lastScatterPos.cx + lastScatterPos.cx - ((this.dendWidth - 100) / (treeData.length - 1))) / 2,
          y: lastScatterPos.cy,
          wid: ((this.dendWidth - 100) / (treeData.length - 1)),
          hei: lastScatterPos.cy - (treeData.length == 1 ? 5 : scatterData[treeData.length - 2].cy),
          id: treeData[treeData.length - 1].id
        })
      }
      for (let i = treeData.length - 2; i >= 0; --i) {
        let tempScatter = ({
          cx: lastScatterPos.cx - ((this.dendWidth - 100) / (treeData.length - 1)),
          cy: (scatterData[i].cy + lastScatterPos.cy) / 2
        });
        lineData.push({
          x1: scatterData[i].cx,
          y1: scatterData[i].cy,
          x2: tempScatter.cx,
          y2: scatterData[i].cy
        });
        lineData.push({
          x1: tempScatter.cx,
          y1: lastScatterPos.cy,
          x2: tempScatter.cx,
          y2: (scatterData[i].cy)
        });
        lineData.push({
          x1: tempScatter.cx,
          y1: lastScatterPos.cy,
          x2: lastScatterPos.cx,
          y2: lastScatterPos.cy
        });
        textData.push({
          x: (scatterData[i].cx + tempScatter.cx) / 2,
          y: scatterData[i].cy,
          wid: (scatterData[i].cx - tempScatter.cx),
          hei: scatterData[i].cy - (i == 0 ? 5 : scatterData[i - 1].cy),
          id: treeData[i].id
        })
        lastScatterPos = tempScatter;
        scatterData.push(tempScatter);
      }

      scatterData.push({
        cx: lastScatterPos.cx - (treeData.length > 1 ? 0 : (this.dendWidth - 100)) - 25,
        cy: lastScatterPos.cy
      });
      lineData.push({
        x1: lastScatterPos.cx,
        y1: lastScatterPos.cy,
        x2: lastScatterPos.cx - (treeData.length > 1 ? 0 : (this.dendWidth - 100)) - 25,
        y2: lastScatterPos.cy
      });

      if (treeData.length == 1) {
        textData.push({
          x: (scatterData[0].cx + 25) / 2,
          y: scatterData[0].cy,
          wid: (scatterData[0].cx - 25),
          hei: scatterData[0].cy - 5,
          id: treeData[0].id
        })
      }

      tree_g.append('g')
        .selectAll('#treeLine')
        .attr('id', 'treeLine')
        .data(lineData)
        .enter()
        .append('line')
        .attr('x1', d => d.x1)
        .attr('y1', d => yAxisTop(d.y1))
        .attr('x2', d => d.x2)
        .attr('y2', d => yAxisTop(d.y2))
        .attr('fill', 'none')
        .attr('stroke', 'rgb(120, 120, 120)')
        .attr('stroke-width', 1);
      tree_g.append('g')
        .selectAll('#treeCir')
        .attr('id', 'treeCir')
        .data(scatterData)
        .enter()
        .append('circle')
        .attr('cx', d => d.cx)
        .attr('cy', d => yAxisTop(d.cy))
        .attr('r', 2)
        .attr('fill', 'black')
        .attr('stroke', d3.rgb(120, 120, 120))
        .attr('stroke-width', 1);
      tree_g.append('g')
        .selectAll('#treeLineName')
        .attr('id', 'treeLineName')
        .data(textData)
        .enter()
        .append('text')
        .attr('text-anchor', 'middle')
        .attr('font-size', 14)
        .attr('dy', -5)
        .attr('x', d => d.x)
        .attr('y', d => yAxisTop(d.y))
        .text(d => {
          if (d.wid > 40 && yAxis(d.hei) > 18)
            return d.id[0].toUpperCase() + d.id.slice(1);
        })
    }
  },
  
  watch: {
    fileP: {
      handler (newValue, oldValue) {

        this.drawDedrogram(this.fileP.filePath);
      },
      deep: true
    },
  }
}
</script>

<style>
</style>