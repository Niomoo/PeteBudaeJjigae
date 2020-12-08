<template>
  <div class="container">
		<div class="detail">
			<div class="viewpoint" 
				v-for="item in viewpoint"
				:key="item.id">
				<div class="number">景點{{item.number}}</div>
				<div class="block">
					<button class="more" @click="getInformation(item.id)"></button>
					<div class="name">{{item.name}}</div>
				</div>
				<div class="address">{{item.address}}</div>
				<button class="change">更換地點</button>
			</div>
		</div>
  </div>
</template>

<script>
import axios from "axios"
export default {
	name: 'DetailedRoute',
  data() {
    return {
			route: this.$route.query.route,
			points:[],
			viewpoint: [
				{ id: 0, number: '一'}, 
				{ id: 1, number: '二'}, 
				{ id: 2, number: '三'}
			],
    }
	},
	mounted() {
		this.getViewpoint();
	},
	methods: {
		getViewpoint() {
			this.points = this.route.split('>').map(point => point);
			for(var i = 0;i < this.viewpoint.length;i++) {
				this.viewpoint[i].name = this.points[i];
				console.log(this.viewpoint[i].name);
				this.getAddress(i, this.viewpoint[i].name);
				
				// console.log(this.viewpoint[i].address);
			}
		},
		getAddress(index, name) {
			const url = 'http://127.0.0.1:5000/findAddress';
			name = String(name);
			console.log(index, name);
      axios.get(url, {
        params: {
          aName: name,
        }
      })
      .then((response) => {
				let a = response.data;
				console.log(a);
				//this.viewpoint[index].address = response.data;
				//console.log(this.viewpoint[index].address);
      })
      .catch(error => {
				console.log("fail");
        console.log(error.response);
      })
		},
		getInformation(id){
			this.$router.push({path:'Information', query:{viewpoint: this.viewpoint[id].name}});
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
				button {
					z-index: 9999;
					margin: 2px 14px 0px 0px;
					width: 27px;
					height: 27px;
					border: none;
					background-color: transparent;
					background-image: url("../assets/info.svg");
				}
				.name {
					width: 224px;
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