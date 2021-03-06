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
          <button
            class="change"
            @click="getChangeViewpoint(item.id)"
            v-if="item.isChanged"
          >
            更換地點
          </button>
        </div>
        <button class="add" @click="showAddPointConfirm = true"></button>
        <button class="finish" @click="showFinishConfirm = true">
          規劃完成
        </button>
      </div>
    </div>
    <Modal
      :show="showAddPointConfirm"
      cancel-text="取消"
      ok-text="確定"
      @ok="getNewViewpoint"
      @cancel="showAddPointConfirm = false"
    >
      <div>開始新增就無法更換囉</div>
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
  name: "DetailedRoute",
  components: {
    Modal,
  },
  data() {
    return {
      showAddPointConfirm: false,
      showFinishConfirm: false,
      route: JSON.parse(this.$route.query.route),
      id: this.$route.query.id,
      points: [],
      viewpoint: [
        { id: 0, isChanged: false, number: "一" },
        { id: 1, isChanged: true, number: "二" },
        { id: 2, isChanged: true, number: "三" },
      ],
    };
  },
  mounted() {
    this.getViewpoint();
    this.getAddress();
  },
  methods: {
    getViewpoint() {
      for (var i = 0; i < this.viewpoint.length; i++) {
        this.viewpoint[i].pid = this.route[i].pid;
        this.viewpoint[i].name = this.route[i].name;
        this.viewpoint[i].isMrt = this.route[i].isMrt;
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
    getChangeViewpoint(index) {
      const url = "http://127.0.0.1:5000/changePoint";
      axios
        .get(url, {
          params: {
            changeIndex: this.id,
            change: index,
          },
        })
        .then((response) => {
          let data = response.data.split(",");
          console.log(data);
          this.viewpoint[index].pid = data[0];
          this.viewpoint[index].name = data[1];
          this.viewpoint[index].isMrt = data[2];
          this.getNewAddress(index);
        })
        .catch((error) => {
          console.log("fail");
          console.log(error.response);
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
      this.viewpoint.isChanged = false;
      this.$router.push({
        path: "AddPoint",
        query: { id: this.id, route: JSON.stringify(this.route) },
      });
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
	text-align: center;
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
				text-align: center;
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
      .change {
        margin: 0px 0px 3px 190px;
        padding: 5px 10px;
        width: 101px;
        height: 33px;
        background-color: #ffffff;
        color: #9e5e25;
        border: none;
        border-radius: 10px;
        line-height: 23px;
        letter-spacing: 0.15px;
        font-size: 20px;
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