<template>
  <div>
    <div class="content">推薦旅遊路線</div>
    <div class="recommendation">
      <div
        v-for="(item, index) in route"
        :key="item"
        @click="handleClick(item, index)"
        :pid="item.viewpoint.pid"
        :pname="item.viewpoint.name"
        class="routes"
      >
        {{ item.display }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Routes",
  data() {
    return {
      routes: this.$route.query.routes,
      route: [
        {
          id: 1,
          viewpoint: [
            { pid: 0, isEnd: false, name: "" },
            { pid: 1, isEnd: false, name: "" },
            { pid: 2, isEnd: true, name: "" },
            { pid: 3, isEnd: true, name: "" },
            { pid: 4, isEnd: true, name: "" },
            { pid: 5, isEnd: true, name: ""}
          ],
          display: "",
        },
        {
          id: 2,
          viewpoint: [
            { pid: 0, isEnd: false, name: "" },
            { pid: 1, isEnd: false, name: "" },
            { pid: 2, isEnd: true, name: "" },
            { pid: 3, isEnd: true, name: "" },
            { pid: 4, isEnd: true, name: "" },
            { pid: 5, isEnd: true, name: "" },
          ],
          display: "",
        },
        {
          id: 3,
          viewpoint: [
            { pid: 0, isEnd: false, name: "" },
            { pid: 1, isEnd: false, name: "" },
            { pid: 2, isEnd: true, name: "" },
            { pid: 3, isEnd: true, name: "" },
            { pid: 4, isEnd: true, name: "" },
            { pid: 5, isEnd: true, name: "" },
          ],
          display: "",
        },
        {
          id: 4,
          viewpoint: [
            { pid: 0, isEnd: false, name: "" },
            { pid: 1, isEnd: false, name: "" },
            { pid: 2, isEnd: true, name: "" },
            { pid: 3, isEnd: true, name: "" },
            { pid: 4, isEnd: true, name: "" },
            { pid: 5, isEnd: true, name: "" },
          ],
          display: "",
        },
        {
          id: 5,
          viewpoint: [
            { pid: 0, isEnd: false, name: "" },
            { pid: 1, isEnd: false, name: "" },
            { pid: 2, isEnd: true, name: "" },
            { pid: 3, isEnd: true, name: "" },
            { pid: 4, isEnd: true, name: "" },
            { pid: 5, isEnd: true, name: "" },
          ],
          display: "",
        },
      ],
      chooseRoute: [],
    };
  },
  mounted() {
    this.getRoute();
  },
  methods: {
    getRoute() {
      for (var i = 0; i < this.routes.length; i++) {
        let route = this.routes[i].split(">").map((point) => point);
        for (var j = 0; j < route.length; j++) {
          let data = route[j];
          let point = data.split("@").map((point) => point);
          this.route[i].viewpoint[j].pid = point[0];
          this.route[i].viewpoint[j].name = point[1];
          this.route[i].viewpoint[j].isMrt = point[2];
        }
      }
      this.displayRoute();
    },
    displayRoute() {
      for (var i = 0; i < this.route.length; i++) {
        for (var j = 0; j < this.route[i].viewpoint.length; j++) {
          this.route[i].display += this.route[i].viewpoint[j].name;
          if (this.route[i].viewpoint[j].isEnd == false) {
            this.route[i].display += " > ";
          }
        }
      }
      console.log(this.route);
    },
    handleClick(el, index) {
      this.chooseRoute = el.viewpoint;
      this.$router.push({
        path: "DetailedRoute",
        query: { route: JSON.stringify(this.chooseRoute), id: index },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.content {
  position: relative;
  margin: 35px auto 23px auto;
  line-height: 28px;
  font-size: 24px;
  font-weight: normal;
  text-align: center;
  color: #A08F82;
}
.recommendation {
  position: relative;
  padding: 0 8px;
  overflow: auto;
  height: 555px;
  .routes {
    margin: 0px auto 18px auto;
    width: 320px;
    padding: 10px 10px;
    background-color: #F2994A;
    border-radius: 5px;
    line-height: 38.4px;
    font-size: 24px;
    font-weight: normal;
    text-align: left;
    align-content: center;
    color: #ffffff;
  }
}
</style>