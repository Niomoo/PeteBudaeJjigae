<template>
<div>
  <div class="page">
      <div class="dot">
        <span></span>
        <span></span>
      </div>
  </div>
  <div class="container">
    <div class="content">請選擇你的定位方式</div>
    <div class="block-btn">
      <Button v-model="input" class="btn rounded ripple" @click="!isChoose">
        自行輸入
      </Button>
      <Button v-model="position" class="btn rounded ripple" @click="!isChoose">
        定位所在地
      </Button>
    </div>
  </div>
  <div class="step">
    <Button class="prev btn rounded ripple" @click="previous">
      上一步
      </Button>
    <Button class="next btn rounded ripple" :class="{active: isNext}" @click="next">
      下一步
    </Button>
  </div>
</div>
</template>

<script>
export default {
    name: 'Positioning',
    props: {
        isNext: {
            type: Boolean,
            default: false,
        },
    },
    data () {
        return {
            isChoose: false,
        };
    },
    
    methods: {/*
        Input() {
            this.isChoose = true;
        },
        position () {
            this.isChoose = true;
        },*/
        previous () {
            this.$router.push('/');
        },
        next () {
            this.$router.push('/');
        }
    }
}
</script>

<style lang="scss">
.page {
  position: relative;
  top: 14px;
  padding: 18px 100px;
  height: 44px;
    .dot{
      span{
        display: inline-flex;
        justify-content: space-around;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #ffffff;
        margin: 18px 10px;
      }
    }
    span:nth-child(1) {
        opacity: 1;
    }
    span:nth-child(2) {
      opacity: 0.2;
    }
}
.container {
  position: relative;
  margin: 30px auto;
  width: 316px;
  height: 311px;
  display: flex;
  flex-direction: column;
  background-color: #59575B;
  border-radius: 25px;
  .content {
    position: relative;
    margin: 50px 50px;
    line-height: 28px;
    font-size: 24px;
    font-weight: normal;
    text-align: center;
    color: #ffffff;
  }
  .block-btn {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    Button {
      margin: 10px 0;
      width: 120px;
      height: 45px;
      font-style: normal;
      font-weight: normal;
      font-size: 20px;
      line-height: 23px;
      letter-spacing: 0.15px;
      color: #DBDBDB;
      border: 0;
      background-color: transparent;
    }
  }
}
.step {
  position: relative;
  height: 60px;
  margin: 30px auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  Button {
    width: 143px;
    height: 60px;
    margin: 15px 15px;
    text-align: center;
    font-style: normal;
    font-weight: normal;
    font-size: 34px;
    line-height: 40px;
    letter-spacing: 0.25px;
    color: #ffffff;
    border: 0;
    border-radius: 10px;
  }
  Button:nth-child(1) {
      background-color: #738EEB;
  }
  Button:nth-child(2) {
      background-color: #9F9F9F;
      &.active {
          background-color: #738EEB;
      }
  }
}
</style>