<template>
<div>
  <div class="content">推薦旅遊路線</div>
    <div class="recommendation">
      <div v-for="(route, index) in routes"
          :key="route"
          @click="handleClick(route, index)"
          class="routes">{{ route }}
    </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'Routes',
  data () {
    return {
      routes: this.$route.query.routes,
      // recommendation: [
      //   {value:'', viewpoint: ' ', id: "1"},
      //   {value:'', viewpoint: ' ', id: "2"},
      //   {value:'', viewpoint: ' ', id: "3"},
      //   {value:'', viewpoint: ' ', id: "4"},
      //   {value:'', viewpoint: ' ', id: "5"}
      // ],
      chooseRoute: []
    };
  },
  
  methods: {
    // listRoutes() {
    //   this.recommendation.value = this.routes;
    //   for(var i = 0; i < 5; i++) {
    //     for(var j = 0; j < 3; j++) {
    //       this.recommendation.viewpoint = this.recommendation.value[i].split(' ');
    //     }
    //   }
    //   console.log(this.recommendation.viewpoint[0]);
    // },
    handleClick(el, index) {
      this.chooseRoute = el;
      this.$router.push({path:'DetailedRoute', query:{route: this.chooseRoute, id: index}});
    }
  }
}
</script>

<style lang="scss" scoped>
.content {
  position: relative;
  margin: 35px auto 23px auto;
  line-height: 28px;
  font-size: 24px;
  font-weight: normal;
  text-align: center;
  color: #ffffff;
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
    background-color: #738EEB;
    border-radius: 5px;
    line-height: 38.4px;
    font-size: 24px;
    font-weight: normal;
    text-align: left;
    align-content: center;
    color: #ffffff;
  };
}
</style>