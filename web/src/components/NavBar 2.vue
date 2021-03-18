<template>
  <div id="nav">
    <div v-if="back" :nostyle="true" class="back ripple" @click="$router.go(-1)">
      <span></span>
      <span></span>
    </div>
    <div class="title" @click="$router.push('/')">高雄旅遊推薦</div>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    back: {
      type: Boolean,
      default: true,
    },
  },
}
</script>

<style lang="scss" scoped>
#nav {
  top: 0;
  z-index: 9999;
  width: 100%;
  height: 56px;
  max-width: 100%;
  background-color: #242424;
  justify-content: center;
  justify-items: center;

  .title {
    display: flex;
    width: 100%;
    height: 100%;
    font-family: Roboto;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    letter-spacing: 0.15px;
    align-items: center;
    justify-content: center;
    color: #FFFFFF;
  }
  .back {
    span {
      display: flex;
      position: absolute;
      background-color: #ffffff;
      width: 3px;
      height: 16px;
      left: 20px;
    }
    & > span:nth-child(1) {
      top: 18px;
      transform: rotate(60deg);
    }
    & > span:nth-child(2) {
      top: 25px;
      transform: rotate(-60deg);
    }
  }
}
</style>