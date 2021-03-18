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
        <button
          class="btn rounded ripple"
          :class="{ btnBg: btnChoose == 1 }"
          @click="ChooseWay(1)"
        >
          自行輸入
        </button>
        <button
          class="btn rounded ripple"
          :class="{ btnBg: btnChoose == 2 }"
          @click="ChooseWay(2)"
        >
          定位所在地
        </button>
      </div>
    </div>
    <div class="step">
      <button class="prev btn rounded ripple" @click="previous">上一步</button>
      <button
        class="next btn rounded ripple"
        :disabled="isChoose == false"
        :class="{ active: isChoose }"
        @click="next"
      >
        下一步
      </button>
    </div>
    <Modal :show="showPositioning">
      <div style="margin-top: 20px">定位中...</div>
    </Modal>
    <Modal 
      :show="showPlace" 
      ok-text="確定"
      @ok="confirmPlace">
      <div style="margin-top: 20px; line-height: 28px;">距離最近的點為：<br/>
        {{placeName}}
      </div>
    </Modal>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./Modal";
export default {
  name: "Positioning",
  components: { Modal },
  props: {
    isNext: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      showPositioning: false,
      showPlace: false,
      isChoose: false,
      btnChoose: 0,
      position: "",
      latitude: 0.0,
      longitude: 0.0,
      place: 0,
      placeName: "",
      isType: 0,
    };
  },
  methods: {
    ChooseWay(way) {
      this.btnChoose = way;
      if (this.btnChoose == 1) {
        this.isChoose = true;
      }
      if (this.btnChoose == 2) {
        this.isChoose = false;
        this.showPositioning = true;
        navigator.geolocation.getCurrentPosition(this.success, this.error);
      }
    },
    previous() {
      this.$router.go(-1);
    },
    next() {
      if (this.btnChoose == 1) {
        this.$router.push("/positioning/enterPosition");
      } else if (this.btnChoose == 2) {
        this.$router.push({ path: "ChooseTag", query: { place: this.place, isType: this.isType } });
      }
    },
    success(position) {
      this.latitude = position.coords.latitude;
      this.longitude = position.coords.longitude;
      console.log(this.latitude, this.longitude);
      const url = "http://127.0.0.1:5000/findNearestViewpoint";
      axios
        .get(url, {
          params: {
            lng: this.longitude,
            lat: this.latitude,
          },
        })
        .then((response) => {
          let data = response.data.split('@');
          console.log(data);
          this.place = data[0];
          this.placeName = data[1];
          this.isChoose = true;
          this.showPositioning = false;
          this.showPlace = true;
        })
        .catch((error) => {
          console.log(error.response);
        });
    },
    error() {
      console.log("fail to load location");
    },
    confirmPlace() {
      this.showPlace = false;
    }
  },
};
</script>

<style lang="scss" scoped>
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
      color: #dbdbdb;
      border: 0;
      background-color: transparent;
    }
    .btnBg {
      color: #9e5e25;
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