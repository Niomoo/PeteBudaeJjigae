<template>
  <div>
    <NavBar />
    <Main />
  <router-view/>
  </div>
</template>
<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import NavBar from '@/components/NavBar.vue'
import Main from '@/components/Main.vue'
export default {
  name: 'Home',
    components: {
      NavBar,
      Main,
  }
}
Vue.use(VueAxios, axios)
</script>

<style lang="scss">
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background: url("assets/Background.svg");
  position: absolute;
  right: 0;
  left: 0;
  top: 0;
  widows: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position-x: left;
  background-position-y: center;
}

</style>
