<template>
<div>
  <div class="page">
      <div class="dot">
        <span></span>
        <span></span>
      </div>
  </div>
    <div class="content">請選擇你的喜好</div>
      <div v-for="foo in preferences" 
        :key="foo.id" 
        @click="handleClick(foo)"
        class="pref check"
        :class="{checked: foo.checked}">{{ foo.value }}
        <div class="check" :class="{checked: foo.checked}"></div>
      </div>
  <div class="step">
    <button class="prev btn rounded ripple" @click="previous">
      上一步
      </button>
    <button class="next btn rounded ripple" :class="{active: isChoose}" :disabled="isChoose == false" @click="next">
      下一步
    </button>
  </div>
</div>
</template>

<script>
import axios from "axios"
export default {
  name: 'ChooseTag',
  props: {
    isNext: {
      type: Boolean,
        default: false,
    },
  },
  data () {
    return {
      isChoose: true,
      preferences: [
        {value: '美食小吃', checked: false, id: "1"},
        {value: '自然風景', checked: false, id: "2"},
        {value: '購物消費', checked: false, id: "3"},
        {value: '休閒娛樂', checked: false, id: "4"},
        {value: '藝術文化', checked: false, id: "5"},
        {value: '歷史古蹟', checked: false, id: "6"}
      ],
      departure: this.$route.query.place,
      isType: this.$route.query.isType,
      inputTag: '',
      routes: []
    };
  },

  methods: {
    handleClick(el) {
      el.checked = !el.checked;
      this.preferences = this.preferences.slice().sort((a, b) => b.checked - a.checked);
    },
    previous () {
      this.$router.go(-1);
    },
    next () {
      let tag = this.preferences;
      for(var i = 0; i < this.preferences.length; i++){
        if(tag[i].checked){
          this.inputTag += tag[i].value + " ";
        }
      }
      console.log(this.departure, this.inputTag);
      this.listRoutes();
    },
    listRoutes () {
      const url = 'http://127.0.0.1:5000/firstRecommend';
      axios.get(url, {
        params: {
          start: this.departure,
          inputTags: this.inputTag,
          isType: this.isType,
        }
      })
      .then((response) => {
          let routes = response.data.split(',');
          this.routes = routes;
          this.$router.push({path:'Routes', query:{routes: routes}});
      })
      .catch(error => {
        console.log(error.response);
      })
    }
  }
}
</script>

<style lang="scss" scoped>

.page {
  position: relative;
  top: 14px;
  padding: 18px 100px;
  height: 44px;
    .dot{
      text-align: center;
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
        opacity: 0.2;
    }
    span:nth-child(2) {
      opacity: 1;
    }
}

  .content {
    position: relative;
    margin: 21px 50px 22px 50px;
    line-height: 28px;
    font-size: 24px;
    font-weight: normal;
    text-align: center;
    color: #A08F82;
  }
  .pref {
    position: relative;
    display: flex;
    flex-direction: column;
    margin: 15px  auto;
    width: 310px;
    height: 40px;
    background-color: #c4c4c4;
    border-radius: 10px;
    line-height: 40px;
    font-size: 24px;
    font-weight: normal;
    text-align: center;
    align-content: center;
    color: #ffffff;
    .check {
      position: absolute;
      margin: 5px 9px 5px 271px;
      width: 30px;
      height: 30px;
      //background-image: url("../assets/cross.svg");
    }
    &.checked {
      background-color: #F2994A;
      .check {
        position: absolute;
        width: 30px;
        height: 30px;
        background-image: url("../assets/check.svg");
      }
    }
  }

.step {
  position: relative;
  height: 60px;
  margin: 40px auto;
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
      background-color: #F2994A;
  }
  Button:nth-child(2) {
      background-color: #9F9F9F;
      &.active {
          background-color: #F2994A;
      }
  }
}
</style>