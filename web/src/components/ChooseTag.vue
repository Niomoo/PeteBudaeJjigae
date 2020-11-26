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
    <button class="next btn rounded ripple" :class="{active: isChoose}" @click="next">
      下一步
    </button>
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
      isChoose: true,
      place: '',
      preferences: [
        {value: '美食小吃', checked: true, id: "1"},
        {value: '自然風景', checked: true, id: "2"},
        {value: '購物消費', checked: true, id: "3"},
        {value: '休閒娛樂', checked: true, id: "4"},
        {value: '藝術文化', checked: true, id: "5"}
     ]
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
          this.place = this.place + tag[i].value + ' ';
        }
      }console.log(this.place);
      //this.$router.go('/');
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
    color: #ffffff;
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
        background-image: url("../assets/check.svg");
    }
    &.checked {
      background-color: #738EEB;
      .check {
        position: absolute;
        width: 30px;
        height: 30px;
        background-image: url("../assets/cross.svg");
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