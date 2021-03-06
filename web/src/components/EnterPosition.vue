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
      <div class="blocks">
        <div class="inputbox">
          <input
            placeholder="請輸入你的出發地"
            class="inputPlace"
            v-model="inputPlace"
            type="text"
          />
          <!-- @key-up="getSearchPlace" -->
        </div>
        <ul v-show="showSearchResult" class="list">
          <li
            v-for="item in searchPlace"
            :value="item"
            :key="item.id"
            class="option"
            @click="getSelect(item)"
          >
            {{ item.name }}
          </li>
        </ul>
        <ul v-show="showWaitResult" class="list">
          <li class="option">搜尋中...</li>
        </ul>
        <div
          class="hint"
          :class="{ right: check == 2, wrong: check == 1, default: check == 0 }"
        >
          <div
            class="hint-icon"
            v-show="isValid"
            :class="{ success: check == 2, fail: check == 1 }"
          ></div>
          請輸入高雄地標
        </div>
      </div>
    </div>
    <div class="step">
      <button class="prev btn rounded ripple" @click="previous">上一步</button>
      <button
        class="next btn rounded ripple"
        :class="{ active: isChoose }"
        :disabled="isChoose == false"
        @click="next"
      >
        下一步
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
export default {
  name: "Positioning",
  props: {
    isNext: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isChoose: false,
      inputPlace: "",
      isValid: false,
      isSelected: false,
      check: 0,
      searchPlace: [],
      selected: [],
      showSearchResult: false,
      showWaitResult: false,
    };
  },
  watch: {
    inputPlace() {
      this.showWaitResult = true;
      this.debouncedGetAnswer();
    }
  },
  created() {
    this.debouncedGetAnswer = _.debounce(this.getSearchPlace, 200);
  },
  methods: {
    checkInput() {
      if (this.check == 2) {
        this.showWaitResult = false;
        this.isValid = true;
        this.isChoose = true;
      } else if (this.check == 1) {
        this.showWaitResult = false;
        this.showSearchResult = false;
        this.isValid = true;
        this.isChoose = false;
      } else {
        this.showWaitResult = false;
        this.showSearchResult = false;
        this.isValid = false;
        this.isChoose = false;
      }
    },
    getSelect(item) {
      this.selected = item;
      this.inputPlace = this.selected.name;
      this.showSearchResult = false;
      this.isSelected = true;
      this.check = 2;
      this.checkInput();
    },
    previous() {
      this.$router.go(-1);
    },
    next() {
      this.$router.push({
        path: "../chooseTag",
        query: { place: this.selected.id, isType: this.selected.type},
      });
    },
    getSearchPlace() {
      const url = "http://127.0.0.1:5000/findAllViewpoint";
      axios
        .get(url, {
          params: {
            userInput: this.inputPlace,
          },
        })
        .then((response) => {
          let data = response.data;
          this.searchPlace = [];
          if (String(data) == "noInput") {
            this.check = 0;
            this.checkInput();
          } else if (String(data) == "noPoint") {
            this.check = 1;
            this.checkInput();
          } else {
            for (var i in data) {
              this.searchPlace.push({ id: data[i].id, name: data[i].name, type: data[i].type});
            }
            console.log(this.searchPlace);
            this.showWaitResult = false;
            if(this.inputPlace == this.selected.name){
              this.showSearchResult = false;
              this.isSelected = true;
            }
            else{
              this.showSearchResult = true;
              this.isSelected = false;
            }
          }
        })
        .catch((error) => {
          console.log("fail");
          this.check = 1;
          this.checkInput();
          console.log(error.response);
        });
    },
  },
};
</script>

<style lang="scss">
.page {
  position: relative;
  top: 14px;
  padding: 18px 100px;
  height: 44px;
  .dot {
    text-align: center;
    span {
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
  background-color: #302B23;
  border-radius: 25px;
  .content {
    position: relative;
    margin: 50px 62px 50px 62px;
    line-height: 28px;
    font-size: 24px;
    font-weight: normal;
    color: #ffffff;
  }
  .blocks {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    .inputbox {
      padding: 16px 20px;
      width: 200px;
      height: 28px;
      margin: 0 auto;
      border: 0;
      background-color: #eaeaea;
      border-radius: 10px;
      align-content: center;
      z-index: 999;
      .inputPlace {
        padding: 0;
        height: 28px;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
        letter-spacing: 0.15px;
        color: #59575b;
        background-color: transparent;
        border: none;
      }
    }
    .list {
        position: absolute;
        top: 41px;
        margin: 0, auto;
        height: 200px;
        width: 240px;
        word-wrap: none;
        list-style-type: none;
        text-align: left;
        overflow: auto;
        padding: 0;
        z-index: 99;
        .option {
          position: relative;
          margin-left: 0;
          background-color: #eaeaea;
          border: 1px solid #ccc;
          opacity: 0.95;
          box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
          border-radius: 0 0 4px 4px;
          padding: 7px 16px;
          font-size: 18px;
          color: #59575b;
        }
      }
    .hint {
      .hint-icon {
        position: absolute;
        left: -22px;
        width: 18px;
        height: 18px;
        background-repeat: no-repeat;
        background-position: center center;
        &.success {
          background-image: url("../assets/right.svg");
        }
        &.fail {
          background-image: url("../assets/wrong.svg");
        }
      }
      position: absolute;
      margin: 32px 22.5px;
      font-size: 16px;
      line-height: 18.75px;
      color: #9e9e9e;
      left: 38px;
      top: 60px;
      &.right {
        color: #4ad079;
      }
      &.wrong {
        color: #ff5a79;
      }
      &.default {
        color: #9e9e9e;
      }
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
    background-color: #F2994A;
  }
  Button:nth-child(2) {
    background-color: #9f9f9f;
    &.active {
      background-color: #F2994A;
    }
  }
}
</style>