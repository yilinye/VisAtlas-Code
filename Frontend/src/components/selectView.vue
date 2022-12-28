<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-30 20:52:22
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div style="height: 100%">
    <div id="titleBar">
      {{ viewName }}
    </div>
    <div id="selectPic">
      <div
        v-if="isChoose"
        id="isChoose"
      >
        <img
          id="nodePic" style="width:300px; height:150px; border:solid 1px"
        >
      </div>
    </div>
    <div id="selectTable">
      <table style="width:calc(100% - 10px);text-align: center;margin-top:2px;height:calc(100% - 10px);margin-bottom:5px;margin-left:5px; margin-right: 5px;">
        <tr style="height:calc(8% - 30px)">
          <th>Class</th>
          <th>Score</th>
        </tr>
        <tr
          v-for="item in items"
          :key="item.className"
          :id="'row'+item.className"
          style="height:calc(8% - 30px)"
        >
          <td>{{ item.className }}</td>
          <td :id="item.className+'Table'">{{ item.classScore }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      viewName: "Selection",
      isChoose: true,
      picPath: "/src/assets/logo.svg",
      items: {
        Area: { className: "Area", classScore: "" },
        Bar: { className: "Bar", classScore: "" },
        Circle: { className: "Circle", classScore: "" },
        Diagram: { className: "Diagram", classScore: "" },
        Line: { className: "Line", classScore: "" },
        Map: { className: "Map", classScore: "" },
        Matrix: { className: "Matrix", classScore: "" },
        Net: { className: "Net", classScore: "" },
        Point: { className: "Point", classScore: "" },
        Table: { className: "Table", classScore: "" },
        Word: { className: "Word", classScore: "" },
      }
    }
  }
}
</script>

<style>
#selectPic {
  height: 30%;
  width: 100%;
}
#isChoose {
  text-align: center;
  margin-top: 1px;
  margin-left: 6px;
  margin-right: 6px;
  margin-bottom: 2px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#selectTable {
  height: calc(70% - 30px);
  width: 100%;
  overflow: auto;
  /* background-color: #000000; */
}

th {
  text-align: middle;
  /* padding-left: 45px; */
  /* border-bottom: 1px solid #ddd; */
  border: 1px solid rgb(138, 138, 138);
  /* background-color: white; */
  background-color: rgb(225, 225, 225);
  color: rgb(7, 7, 7);
  font-size: 16px;
  
  /* color: white; */
}

td {
  text-align: middle;
  /* padding-left: 45px; */
  width: 50%;
  /* border-bottom: 1px solid #ddd; */
  border: 1px solid rgb(138, 138, 138);
  font-size: 16px;
  color: black;
  /* height: 100% */
}

/* tr {
  height: calc(100%)
} */

tr:hover{
  /* background-color: rgb(231, 164, 179); */
  background-color: #D7F4F2;
}
</style>