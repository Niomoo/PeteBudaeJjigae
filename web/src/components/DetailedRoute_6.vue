<template>
  <div>
    <div class="container">
      <div class="detail">
        <div class="viewpoint" v-for="item in viewpoint" :key="item.id">
          <div class="number">景點{{ item.number }}</div>
          <div class="block">
            <button class="mrt" v-if="item.isMrt==1"></button>
            <button class="more" v-else @click="getInformation(item.id)"></button>
            <div class="name">{{ item.name }}</div>
          </div>
          <div class="address">{{ item.address }}</div>
        </div>
        <button class="add" v-if="isAdd" @click="showCannotAdd = true"></button>
        <button class="finish" @click="showFinishConfirm = true">
          規劃完成
        </button>
      </div>
    </div>
    <Modal
      :show="showCannotAdd"
      cancel-text="取消"
      ok-text="確定"
      @ok="getNewViewpoint"
      @cancel="showCannotAdd = false"
    >
      <div>已達上限無法再新增囉！</div>
    </Modal>
    <Modal
      :show="showFinishConfirm"
      cancel-text="取消"
      ok-text="確定"
      @ok="getCompleteRoute"
      @cancel="showFinishConfirm = false"
    >
      <div>即將匯出完整旅程</div>
    </Modal>
  </div>
</template>

<script>
import axios from "axios";
import Modal from "./Modal";
export default {
  name: "DetailedRoute_6",
  components: {
    Modal,
  },
  data() {
    return {
      showCannotAdd: false,
      showFinishConfirm: false,
      isAdd: true,
      route: JSON.parse(this.$route.query.route),
      id: this.$route.query.id,
      points: [],
      viewpoint: [
        { id: 0, isChanged: false, number: "一" },
        { id: 1, isChanged: false, number: "二" },
        { id: 2, isChanged: false, number: "三" },
        { id: 3, isChanged: false, number: "四" },
        { id: 4, isChanged: false, number: "五" },
        { id: 5, isChanged: false, number: "六" },
      ],
    };
  },
  mounted() {
    this.getViewpoint();
    this.getAddress();
  },
  methods: {
    getViewpoint() {
      let route = this.route.split(">").map((point) => point);
      for (var i = 0; i < route.length; i++) {
        let data = route[i];
        let point = data.split("@").map((point) => point);
        this.viewpoint[i].pid = point[0];
        this.viewpoint[i].isEnd = point[1];
        this.viewpoint[i].name = point[2];
        this.viewpoint[i].isMrt = point[3];
      }
    },
    getAddress() {
      const url = "http://127.0.0.1:5000/findAddress";
      axios
        .get(url, {
          params: {
            Id: this.id,
          },
        })
        .then((response) => {
          let data = response.data.split(">").map((point) => point);
          for (var i = 0; i < this.viewpoint.length; i++) {
            this.viewpoint[i].address = data[i];
          }
          console.log(this.viewpoint);
        })
        .catch((error) => {
          console.log("fail");
          console.log(error.response);
        });
    },
    getInformation(id) {
      this.$router.push({
        path: "Information",
        query: { pid: this.viewpoint[id].pid, name: this.viewpoint[id].name },
      });
    },
    getNewAddress(index) {
      const url = "http://127.0.0.1:5000/changeOrAddAddress";
      axios
        .get(url, {
          params: {
            routeIdx: this.id,
            pointIdx: index,
          },
        })
        .then((response) => {
          let data = response.data;
          this.viewpoint[index].address = data;
        })
        .catch((error) => {
          console.log("fail");
          console.log(error.response);
        });
    },
    getNewViewpoint() {
      this.isAdd = false;
      this.showCannotAdd = false;
    },
    getCompleteRoute() {
      this.$router.push({
        path: "ExportRoute",
        query: { route: JSON.stringify(this.viewpoint) },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  position: relative;
  margin: 30px auto;
  width: 300px;
  height: 580px;
  background-color: #F2994A;
  border-radius: 20px;
  padding: 19px 30px 19px 30px;
  .detail {
    display: flex;
    flex-direction: column;
    overflow: scroll;
    width: 300px;
    height: 100%;
    .viewpoint {
      .number {
        width: 123px;
        height: 52px;
        padding: 6px 10px 6px 10px;
        left: 0;
        background-color: #9e5e25;
        border-radius: 5px;
        font-size: 34px;
        line-height: 52px;
        letter-spacing: 0.25px;
        color: #ffffff;
        text-align: center;
      }
      .block {
        display: flex;
        flex-direction: row;
        margin: 16px 0px 0px 0px;
        justify-content: flex-start;
        align-content: center;
        .more {
          top: 0px;
          margin: 0px 14px 0px 0px;
          width: 32px;
          height: 32px;
          border: none;
          background-color: transparent;
          background-image: url("../assets/info_2.svg");
          background-repeat: no-repeat;
          background-position: center center;
        }
        .mrt {
					top: 0px;
          margin: 0px 14px 0px 0px;
          width: 32px;
          height: 32px;
          border: none;
          background-size: 32px;
          background-color: transparent;
          background-image: url("../assets/train.svg");
					background-repeat: no-repeat;
					background-position: center center;
        }
        .name {
          width: 270px;
          text-align: left;
          font-size: 24px;
          color: #ffffff;
          margin-bottom: 10px;
        }
      }
      .address {
        display: flex;
        justify-content: flex-start;
        text-align: left;
        margin-bottom: 10px;
        font-size: 20px;
        color: #ffffff;
      }
    }
    .add {
      padding: 31px 0;
      width: 62px;
      height: 62px;
      border: none;
      margin: 10px auto;
      background-color: transparent;
      background-image: url("../assets/addBtn.svg");
    }
    .finish {
      position: relative;
      width: 177px;
      height: 60px;
      padding: 10px;
      margin: 13px auto;
      text-align: center;
      font-size: 34px;
      line-height: 40px;
      letter-spacing: 0.25px;
      color: #ffffff;
      border: 0;
      border-radius: 10px;
      background-color: #9e5e25;
      box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
    }
  }
}
</style>