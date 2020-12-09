<template>
<div>
  <div class="page">
    <div class="dot">
      <span></span>
      <span></span>
    </div>
  </div>
  <div class="container">
    <div class="content">請輸入你的出發地</div>
    <div class="block">
      <div class="inputbox">
      <input v-model="inputPlace" 
             placeholder="請輸入你的出發地"
             class ="inputPlace" 
             type="text"
             @input = "inputDeparture" 
      >{{inputPlace}}
      <div v-for="item in searchPlace" :key="item">{{item.name}}</div>
      </div>
      <div class="hint" :class="{active: checkInput}">請輸入高雄地標</div>
    </div>
  </div>
  <div class="step">
    <button class="prev btn rounded ripple" @click="previous">
      上一步
      </button>
    <button class="next btn rounded ripple" :class="{active: isChoose}" @click="next">
      下一步
    </button>
  </div>
</div>
</template>

<script>
import axios from "axios";
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
      inputPlace: '',
      isValid: false,
      check: 0,
      searchPlace: [{
        id: 0,
        name: ''
      }],
      departure: '',
    };
  }, 
  methods: {
    checkInput (){
      if(this.isValid==true){
        this.isChoose=true;
      }
    },
    previous () {
      this.$router.go(-1);
    },
    next () {
      this.$router.go('/');
    },
    inputDeparture() {
      const url = 'http://127.0.0.1:5000/findAllViewpoint';
        axios.get(url, {
          params: {
            userInput: this.inputPlace 
          }
        })
        .then((response) => {
          this.searchPlace = response.data;
          console.log(this.searchPlace);
        })
        .catch(error => {
          console.log(error.response);
        })
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
  margin: 51px auto;
  width: 316px;
  height: 311px;
  display: flex;
  flex-direction: column;
  background-color: #59575B;
  border-radius: 25px;
  .content {
    position: relative;
    margin: 50px 62px 50px 62px;
    line-height: 28px;
    font-size: 24px;
    font-weight: normal;
    text-align: center;
    color: #ffffff;
  }
  .block {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    .inputbox {
      padding: 16px 20px;
      width: 200px;
      height: 28px;
      border: 0;
      background-color: #EAEAEA;
      border-radius: 10px;
      align-content: center;
      .inputPlace {
        padding: 0;
        height: 28px;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
        letter-spacing: 0.15px;
        color: #59575B;
        background-color: transparent;
        border: none;
      }
    }
    .hint {
      position: absolute;
      margin: 32px 22.5px;
      font-size: 16px;
      line-height: 18.75px;
      color: #9E9E9E;
      left: 38px;
      top: 60px;
    }
  }
}
.step {
  position: relative;
  height: 60px;
  margin: 64px auto;
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
    box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
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