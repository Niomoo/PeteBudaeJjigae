<template>
<div>
  <div class="content">推薦旅遊路線</div>
  <div v-for="foo in recommendation" 
    :key="foo.id" 
    @click="handleClick(foo)"
    class="path"
    :class="{checked: foo.checked}">{{ foo.value }}
    <div class="check" :class="{checked: foo.checked}"></div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Routes',
  data () {
    return {
      place:'',
      recommendation: ''
    };
  }
}
</script>

<style lang="scss" scoped>
.content {
  position: relative;
  margin: 35px auto;
  line-height: 28px;
  font-size: 24px;
  font-weight: normal;
  text-align: center;
  color: #ffffff;
}
</style>