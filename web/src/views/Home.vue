<template>
    <div class="main text-center">
        <div class="block-btn">
            <Button class="btn" :style="true" @click="start">開始旅遊規劃</Button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Start',
  methods: {
    start() {
      this.isStart = true;
      this.$router.push('positioning');
    }
  }
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
      background-color: #738EEB;
      border-radius: 10px;
    }
  }
}
</style>