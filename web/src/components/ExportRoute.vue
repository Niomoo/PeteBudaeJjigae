<template>
  <div>
    <div class="container">
      <div class="detail">
        <div class="viewpoint" v-for="item in viewpoint" :key="item.id">
          <div class="number">景點{{ item.number }}</div>
          <div class="name">{{ item.name }}</div>
          <div class="address">{{ item.address }}</div>
          <button class="change" @click="getInformation(item.id)">
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
      points: [],
      viewpoint: [
        { id: 0, number: "一" },
        { id: 1, number: "二" },
        { id: 2, number: "三" },
        { id: 3, number: "四" },
        { id: 4, number: "五" },
        { id: 5, number: "六" },
      ],
    };
  },
  mounted() {
    this.getViewpoint();
  },
  methods: {
    getViewpoint() {
      for (var i = 0; i < this.route.length; i++) {
        this.viewpoint[i].pid = this.route[i].pid;
        this.viewpoint[i].name = this.route[i].name;
        this.viewpoint[i].number = this.route[i].number;
        this.viewpoint[i].address = this.route[i].address;
      }
    },
    getInformation(id) {
      this.$router.push({
        path: "Information",
        query: { pid: this.viewpoint[id].pid, name: this.viewpoint[id].name },
      });
    },
    getCompleteRoute() {
      this.$router.push({
        path: "ExportRoute",
        query: { route: JSON.stringify(this.route) },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.container{
	position: relative;
	margin: 30px auto;
	width: 300px;
	height: 580px;
	background-color: #5164AB;
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
				background-color: #28335C;
				border-radius: 5px;
				font-size: 34px;
				line-height: 52px;
				letter-spacing: 0.25px;
				color: #FFFFFF;
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
				color: #5164AB;
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
			background-color: #738EEB;
			box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
		}
	}
}
</style>