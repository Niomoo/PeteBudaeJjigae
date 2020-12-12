<template>
  <div>
    <div class="content">新增景點{{ choose.name }}</div>
    <div class="container">
      <div
        v-for="item in viewpoint"
        :key="item"
        class="viewpoint"
        :class="{ active: item.checked }"
      >
        <div class="block">
          <div class="name">{{ item[1] }}</div>
          <button class="more" @click="getInformation(item.id)"></button>
        </div>
        <div class="address">{{ item.address }}</div>
        <button class="add" @click="handleClick(item)">選擇加入</button>
      </div>
    </div>
    <button class="confirm" :class="{ active: isChoose }">確定更改</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AddPoint",
  data() {
    return {
      id: this.$route.query.id,
      data: [],
      isChoose: false,
      viewpoint: [],
      choose: [],
    };
  },
  mounted() {
    this.getNewPoint();
  },
  methods: {
    getNewPoint() {
      const url = "http://127.0.0.1:5000/addPoint";
      axios
        .get(url, {
          params: {
            addIndex: this.id,
          },
        })
        .then((response) => {
          this.data = response.data.split(">").map((point) => point);
          for (var i = 0; i < this.data.length; i++) {
						this.viewpoint[i] = this.data[i].split(",").map((point) => point);
						this.viewpoint[i].push({checked: false});
          }
          console.log(this.viewpoint);
        })
        .catch((error) => {
          console.log("fail");
          console.log(error.response);
        });
    },
    handleClick(el) {
			this.isChoose = !this.isChoose;
			el.checked = !el.checked;
      this.choose = el;
    },
  },
};
</script>

<style lang="scss" scoped>
.content {
  position: relative;
  margin: 30px 30px;
  text-align: left;
  line-height: 28px;
  font-size: 34px;
  font-weight: normal;
  color: #ffffff;
}
.container {
  width: 412px;
  height: 480px;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
  align-content: center;
  overflow: auto;
  .viewpoint {
    width: 370px;
    margin: 0 auto 25px auto;
    background-color: #738eeb;
    border-radius: 20px;
    &.active {
      background-color: #40559F;
    }
    .block {
      display: flex;
      flex-direction: row;
      justify-content: flex-start;
      align-content: center;
      padding: 12px 30px;
      .more {
        margin-top: 9px;
        // margin: auto;
        width: 27px;
        height: 27px;
        border: none;
        background-color: transparent;
        background-image: url("../assets/info.svg");
      }
      .name {
        margin: auto;
        width: 300px;
        text-align: left;
        font-size: 32px;
        color: #ffffff;
      }
    }
    .address {
      display: flex;
      justify-content: flex-start;
      margin-bottom: 10px;
      font-size: 20px;
      color: #ffffff;
    }
    .add {
      margin: 0px 0px 21px 209px;
      padding: 5px 10px;
      width: 101px;
      height: 33px;
      background-color: #ffffff;
      color: #5164ab;
      border: none;
      border-radius: 10px;
      line-height: 23px;
      letter-spacing: 0.15px;
      font-size: 20px;
    }
  }
}
.confirm {
  position: absolute;
  width: 136px;
  height: 56px;
  bottom: 30px;
  right: 27px;
  font-size: 24px;
  line-height: 40px;
  letter-spacing: 0.25px;
  color: #ffffff;
  border: 0;
  border-radius: 10px;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
  background-color: #9f9f9f;
  &.active {
    background-color: #738eeb;
  }
}
</style>