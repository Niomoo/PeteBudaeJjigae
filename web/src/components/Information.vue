<template>
<div class="container">
  <div class="content">
		<div class="name"></div>
		<div class="image"></div>
		<div class="info">
			<div class="info 1">地址：{{viewpoint}}</div>			
			<div class="info 2">評價星數：</div>
			<div class="info 3">評價人數：</div>			
			<div class="info 4">分類：</div>
			<div class="info 5">簡介：</div>
		</div>
  </div>
</div>
</template>

<script>
export default {
	name: 'Information',
	data() {
		return {
			viewpoint: this.$route.query.viewpoint,
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
}
</style>