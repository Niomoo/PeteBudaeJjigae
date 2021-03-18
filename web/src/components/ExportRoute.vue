<template>
  <div>
    <div class="container">
      <div class="detail">
        <div class="viewpoint" v-for="item in route" :key="item.id">
          <div class="number">景點{{ item.number }}</div>
          <div class="name">{{ item.name }}</div>
          <div class="address">{{ item.address }}</div>
          <button class="mrt" v-if="item.isMrt==1" disabled>
            捷運景點
          </button>
          <button class="detail" v-else @click="getInformation(item.id)">
            詳細資訊
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DetailedRoute",
  data() {
    return {
      route: JSON.parse(this.$route.query.route),
      id: this.$route.query.id,
    };
  },
  methods: {
    getInformation(id) {
      this.$router.push({
        path: "Information",
        query: { pid: this.route[id].pid, name: this.route[id].name },
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
        text-align: center;
        line-height: 52px;
        letter-spacing: 0.25px;
        color: #ffffff;
      }
      .name {
        display: flex;
        flex-direction: row;
        margin: 16px 0px 0px 0px;
        justify-content: flex-start;
        align-content: center;
        width: 270px;
        text-align: left;
        font-size: 24px;
        color: #ffffff;
        margin-bottom: 10px;
      }
      .address {
        display: flex;
        justify-content: flex-start;
        text-align: left;
        margin-bottom: 10px;
        font-size: 20px;
        color: #ffffff;
      }
      .mrt {
        margin: 0px 0px 3px 190px;
        padding: 5px 10px;
        width: 101px;
        height: 33px;
        background-color: #9e5e25;
        color: #d8d8d8;
        border: none;
        border-radius: 10px;
        line-height: 23px;
        letter-spacing: 0.15px;
        font-size: 20px;
      }
      .detail {
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
  }
}
</style>