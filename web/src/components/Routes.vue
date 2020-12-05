<template>
<div>
  <div class="content">推薦旅遊路線</div>
  <button @click="listRoutes">listRoutes</button>
      <!-- <div v-for="foo in routes" 
        :key="foo.id" 
        @click="handleClick(foo)"
        class="pref check">{{ foo.value }}
        <div class="check" :class="{checked: foo.checked}">
        {{routes}}  
      </div>
  </div> -->
</div>
</template>

<script>
import axios from "axios";
export default {
  name: 'Routes',
  data () {
    return {
      routes: [
        {value: '', checked: true, id: "1"},
        {value: '', checked: true, id: "2"},
        {value: '', checked: true, id: "3"},
        {value: '', checked: true, id: "4"},
        {value: '', checked: true, id: "5"}
      ],
    };
  },
  methods: {
    listRoutes () {
      let departure = this.$route.query.place;
      let tag = this.$route.query.inputTags;
      console.log(departure, tag);
      const url = 'http://127.0.0.1:5000/firstRecommend';
        axios.get(url, {
          params: {
            start: departure,
            inputTags: tag,
          }
        })
        .then((response) => {
          this.routes.value = response.data;
          console.log(this.routes);
        })
        .catch(error => {
          console.log(error.response);
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.content {
  position: relative;
  margin: 35px auto;
  line-height: 28px;
  font-size: 24px;
  font-weight: normal;
  text-align: center;
  color: #ffffff;
}
</style>