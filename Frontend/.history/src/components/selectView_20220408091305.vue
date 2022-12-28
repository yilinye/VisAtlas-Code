<!--
 * @Author: Qing Shi
 * @LastEditTime: 2022-04-08 09:13:05
 * @Knowledge: 
 * @Description: 
 * @Attention: 
-->
<template>
  <div id="titleBar">
    {{ viewName }}
  </div>
  <div id="selectPic">
    <div
      v-if="isChoose"
      id="isChoose"
    >
      <img
        :src="picPath"
        style="width: auto; height: 100%; border: solid 1px"
      >
    </div>
  </div>
  <div id="selectTable">

    <table style="width:100%;text-align: center;margin-top:2px">
      <tr>
        <th>Class</th>
        <th>Score</th>
      </tr>
      <tr
        v-for="item in items"
        :key="item.className"
      >
        <td>{{ item.className }}</td>
        <td :id="item.className">{{ item.classScore }}</td>
      </tr>
    </table>
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
}
#selectTable {
  height: 60%;
  width: 100%;
  overflow: auto;
  /* background-color: #000000; */
}

th {
  text-align: left;
  padding-left: 45px;
  /* border-bottom: 1px solid #ddd; */
  border: 1px solid rgb(138, 138, 138);
  /* background-color: white; */
  background-color: rgb(225, 225, 225);
  color: rgb(7, 7, 7);
  font-size: 20px;
  /* color: white; */
}

td {
  text-align: left;
  padding-left: 45px;
  /* border-bottom: 1px solid #ddd; */
  border: 1px solid rgb(138, 138, 138);
  font-size: 18px;
  color: black;
}

tr:hover {
  background-color: rgb(231, 164, 179);
}
</style>