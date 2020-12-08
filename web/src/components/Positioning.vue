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
      <button class="btn rounded ripple" :class="{btnBg: btnChoose==1}" @click="ChooseWay(1)">
        自行輸入
      </button>
      <button class="btn rounded ripple" :class="{btnBg: btnChoose==2}" @click="ChooseWay(2)">
        定位所在地
      </button>
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
import axios from "axios"
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
      btnChoose: 0,
      position: '',
      latitude: 0.0,
      longitude: 0.0,
      place: 0,
    };
  },
  methods: {
    ChooseWay(way) {
      this.btnChoose = way;
      this.isChoose = true;
      if(this.btnChoose == 2) {
        navigator.geolocation.getCurrentPosition(this.success, this.error);
      }
    },
    previous () {
      this.$router.go(-1);
    },
    next () {
      if(this.btnChoose == 1)
      {
        this.$router.push('/positioning/enterPosition');
      }
      else if(this.btnChoose == 2)
      {
        this.$router.push({path:'ChooseTag', query:{place: this.place}});
      }
    },            
    success(position) {
        this.latitude = position.coords.latitude;
        this.longitude = position.coords.longitude;
        console.log(this.latitude, this.longitude);
        const url = 'http://127.0.0.1:5000/findNearestViewpoint';
        axios.get(url, {
          params: {
            lng: this.longitude,
            lat: this.latitude
          }
        })
        .then((response) => {
          this.place = response.data;
          console.log(this.place);
        })
        .catch(error => {
          console.log(error.response);
        })
    },
    error() {
        console.log("fail to load location");
    },
  },
}
</script>

<style lang="scss" scoped>
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
    .btnBg {
        color: #5164AB;
        background-color: #ffffff;
        border-radius: 10px;
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