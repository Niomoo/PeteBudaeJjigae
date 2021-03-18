<template>
  <div class="main">
    <div class="block-btn">
      <button class="btn" :style="true" @click="this.$router.push('positioning')">開始旅遊規劃</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Start',
}
</script>

<style lang="scss" scoped>
.main {
  position: relative;
  .block-btn {
    display: flex;
    padding: 10px 0px 0px 20px;
    align-items: flex-start;
    margin-top: 255px;
    .btn {
      position: absolute;
      left: calc(50% - 246px/2 + 0.5px);
      top: calc(50% - 60px/2 + 31.5px);
      display: block;
      width: 246px;
      height: 60px;
      font-size: 32px;
      font-weight: normal;
      line-height: 40px;
      color: #FFFFFF;
      background-color: #F2994A;
      border-radius: 10px;
      border: none;
    }
  }
}
</style>