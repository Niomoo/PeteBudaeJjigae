<template>
  <div>
    <NavBar />
  <router-view/>
  </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'Home',
    components: {
      NavBar,
  }
}
</script>

<style lang="scss"> 
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: url("assets/Background_2.svg");
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
