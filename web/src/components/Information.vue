<template>
<div class="container">
  <div class="content">
		<div class="name">{{name}}</div>
		<img :src="imgUrl"/>
		<div class="info">
			<div class="info a">地址：{{address}}</div>	
			<div class="info b">評價星數：{{star}}</div>
			<div class="info c">評價人數：{{comments}}</div>			
			<div class="info d">簡介：{{info}}</div>
		</div>
  </div>
</div>
</template>

<script>
import axios from "axios";
export default {
	name: 'Information',
	data() {
		return {
			name: this.$route.query.name,
			address: this.$route.query.address,
			star: 0.0,
			comments: 0,
			info: "",
			imgUrl: "",
			data: [],
		}
	},
	mounted() {
		this.getInformation();
	},
	methods: {
		getInformation() {
			axios.get('intro.json')
			.then(response => {
				this.data = response.data;
				for(var i = 0; i < this.data.length; i++) {
				if (this.data[i].aName == this.name) {
					console.log(this.data[i].aImage)
					console.log(this.data[i].aIntroduction);
					this.imgUrl = this.data[i].aImage;
					this.info = this.data[i].aIntroduction;
				}				
			}
				})
			.catch(error => {
					console.log(error);
			});
		},
	}
}
</script>

<style lang="scss" scoped>
.container{
	margin: 30px auto;
	width: 300px;
	height: 580px;
	background-color: #5164AB;
	border-radius: 20px;
	padding: 19px 30px;
	text-align: left;
	.content {
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
			.d {
				margin-top: 25px;
			}
		}
	}
}
</style>