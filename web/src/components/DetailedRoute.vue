<template>
  <div class="container">
		<div class="detail">
			<div class="viewpoint" 
				v-for="item in viewpoint"
				:key="item.id">
				<div class="number">景點{{item.number}}</div>
				<div class="block">
					<div class="more"></div>
					<div class="name">{{item}}</div>
				</div>
				<div class="address"></div>
				<button class="change">更換地點</button>
			</div>
		</div>
  </div>
</template>

<script>
//import axios from "axios"
export default {
	name: 'DetailedRoute',
  data() {
    return {
			route: this.$route.query.route,
			viewpoint: [
				{ id: 1, number: '一'}, 
				{ id: 2, number: '二'}, 
				{ id: 3, number: '三'}
			],
    }
	},
	mounted() {
		this.getViewpoint();
	},
	methods: {
		getViewpoint() {
			this.viewpoint = this.route.split('>').map(point => point);
			console.log(this.viewpoint);
		}
	}
}
</script>

<style lang="scss" scoped>
.container{
	position: relative;
	margin: 30px auto;
	width: 300px;
	height: 550px;
	background-color: #5164AB;
	border-radius: 20px;
	padding: 19px 30px;
	.detail {
		position: relative;
		display: flex;
		flex-direction: column;
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
			.block {
				display: flex;
				flex-direction: row;
				height: 40px;
				margin: 16px 0px;
				justify-content: flex-start;
				align-content: center;
				.more {
					z-index: 9999;
					margin: 2px 14px 0px 0px;
					width: 27px;
					height: 27px;
					background-image: url("../assets/info.svg");
				}
				.name {
					text-align: left;
					font-size: 24px;
					color: #ffffff;
					
				}
			}
			.address {
				color: #ffffff;
			}
			button {
				position: relative;
				margin: 10px 0px 3px 164px;
				right: 0px;
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
	}
}
</style>