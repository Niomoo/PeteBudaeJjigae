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
        :class="{checked: foo.checked}">{{ foo.value }} - {{ foo.checked }}</div>
    <!-- <div class="block">
      <input type="checkbox" id="food123" value="美食小吃" class="checkbox" v-model="preferences">
      <label for="food123">
        <span>
          <div class="pref">美食小吃</div>
          <div class="check"></div>
        </span>
      </label>
      <label for="nature">
        <input type="checkbox" id="nature" value="自然風景" class="checkbox" v-model="preferences">
        <span>
          <div class="pref">自然風景</div>
          <div class="check"></div>
        </span>
      </label>
      <label for="shopping">
        <input type="checkbox" id="shopping" value="購物消費" class="checkbox" v-model="preferences">
        <span>
          <div class="pref">購物消費</div>
          <div class="check"></div>
        </span>
      </label>
      <label for="entertain">
        <input type="checkbox" id="entertain" value="休閒娛樂" class="checkbox" v-model="preferences">
        <span>
          <div class="pref">休閒娛樂</div>
          <div class="check"></div>
        </span>
      </label>
      <label for="art">
        <input type="checkbox" id="art" value="藝術文化" class="checkbox" v-model="preferences">
        <span>
          <div class="pref">藝術文化</div>
          <div class="check"></div>
        </span>
      </label>
    </div> -->
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
            default: true,
        },
    },
    data () {
        return {
            isChoose: false,
            place: '',
            isValid: false,
            check: 0,
            // preferences: ['美食小吃','自然風景','購物消費','休閒娛樂','藝術文化'],
            preferences: [
              {value: '美食小吃', checked: false, id: "1"},
              {value: '自然風景', checked: false, id: "2"},
              {value: '購物消費', checked: false, id: "3"},
              {value: '休閒娛樂', checked: false, id: "4"},
              {value: '藝術文化', checked: false, id: "5"}
            ]
        };
    },
    // computed: {
    //   sortedPreferences() {
    //     return this.preferences.slice().sort((a, b) => b.checked - a.checked);
    //   }
    // },
    // watch: {
    //   // preferences(newValue) {
    //   //   this.preferences = newValue.sort((a, b) => b.checked - a.checked);
    //   // }
    //   preferences: {
    //     handler(val) {
    //       this.preferences = val.sort((a, b) => b.checked - a.checked);
    //       console.table(this.preferences);
    //     },
    //     deep: true
    //   }
      
    // },
    methods: {
        labelCheck() {

        },
        previous () {
            this.$router.go(-1);
        },
        next () {
            this.$router.go('/');
        },
        handleClick(el) {
          el.checked = !el.checked;
          this.preferences = this.preferences.slice().sort((a, b) => b.checked - a.checked);
        }
    }
}
</script>

<style lang="scss" scoped>
.checked {
  background-color: lightblue;
}


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
    margin: 21px 50px 17px 50px;
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
    label {
      margin: 7.5px 0;
      cursor: pointer;
    }
    input[type=checkbox]{
      display: none;
    }
    input[type=checkbox]+span {
      display: inline-block;
      width: 310px;
      height: 40px;
      background-color: #c4c4c4;
      border-radius: 10px;
      display: flex;
      .pref {
        position: relative;
        margin: auto auto;
        line-height: 28px;
        font-size: 24px;
        font-weight: normal;
        text-align: center;
        align-content: center;
        color: #ffffff;
      }
      .check {
        position: absolute;
        margin: 5px 9px 5px 271px;
        width: 30px;
        height: 30px;
        background-image: url("../assets/check.svg");
      }
    }
    input[type=checkbox]:checked+span {
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