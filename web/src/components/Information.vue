<template>
  <div class="boxer">
    <div class="box">
      <div class="name">{{ name }}</div>
      <img :src="imgUrl" />
      <div class="info">
        <div class="info a">地址：{{ detail.address }}</div>
        <div class="info b">評價星數：{{ detail.star }}</div>
        <div class="info c">評價人數：{{ detail.comments }}</div>
        <div class="info d">簡介：{{ info }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Information",
  data() {
    return {
      pid: this.$route.query.pid,
      name: this.$route.query.name,
      detail: [],
      info: "",
      imgUrl: "",
      data: [],
    };
  },
  mounted() {
    this.getDetail();
    this.getInformation();
  },
  methods: {
    getInformation() {
      axios
        .get("intro.json")
        .then((response) => {
          this.data = response.data;
          for (var i = 0; i < this.data.length; i++) {
            if (this.data[i].aId == this.pid) {
              this.imgUrl = this.data[i].aImage;
              this.info = this.data[i].aIntroduction;
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getDetail() {
      const url = "http://127.0.0.1:5000/pointDetail";
      axios
        .get(url, {
          params: {
            aId: this.pid,
          },
        })
        .then((response) => {
          let data = response.data.split(">").map((point) => point);
          this.detail.address = data[0];
          this.detail.star = data[1];
          this.detail.comments = data[2];
          if (this.detail.star == 0) {
            this.detail.star = "--";
          }
          if (this.detail.comments == 0) {
            this.detail.comments = "--";
          }
          console.log(this.detail);
        })
        .catch((error) => {
          console.log("fail");
          console.log(error.response);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.boxer {
  margin: 30px auto;
  width: 300px;
  height: 580px;
  background-color: #F2994A;
  border-radius: 20px;
  padding: 19px 30px;
  text-align: left;
  .box {
    height: 100%;
    overflow: scroll;
    .name {
      margin-top: 8px;
      font-size: 34px;
      color: #ffffff;
    }
    img {
      margin: 9px 0 20px 0;
      width: 300px;
    }
    .info {
      color: #ffffff;
      font-size: 20px;
      line-height: 25px;
      word-break: break-all;
      .d {
        margin-top: 25px;
      }
    }
  }
}
</style>