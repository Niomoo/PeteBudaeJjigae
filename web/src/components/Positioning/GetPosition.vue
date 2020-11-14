<template>
<div>
  <div class="page">
      <div class="dot">
        <span></span>
        <span></span>
      </div>
  </div>
  <div class="container">
    <div class="content">請確認你的出發地</div>
    <div class="block">
        <div class="inputbox">
        <input v-model="place" 
               class ="inputPlace" 
               type="text"
               @input="checkInput"
        >{{place}}
        </div>
        <div class="hint" :class="{active: checkInput}">請輸入高雄地標</div>
    </div>
  </div>
  <div class="step">
    <Button class="prev btn rounded ripple" @click="previous">
      上一步
      </Button>
    <Button class="next btn rounded ripple" :class="{active: isChoose}" @click="next">
      下一步
    </Button>
  </div>
</div>
</template>

<script>
export default {
    name: 'Positioning',
    props: {
        isNext: {
            type: Boolean,
            default: false,
        },
    },
    data () {
        return {
            isChoose: false,
            place: '',
            isValid: false,
            check: 0,
        };
    },
    
    methods: {
        getGeo(){
            var latitude;
            var longtitude;
            var output = document.getElementById("out");

            if (!navigator.geolocation) {
                output.innerHTML = "<p>Geolocation is not supported by your browser</p>";
                return;
            }

            function success(position) {
                var lat1 = position.coords.latitude;
                var long1 = position.coords.longitude;

                output.innerHTML = '<p>Latitude is ' + lat1 + '° <br>Longitude is ' + long1 + '°</p>';
                console.log(lat1,long1);
                latitude=lat1;
                longtitude=long1;
                console.log(latitude,longtitude,"hi");
            };

            function error() {
                output.innerHTML = "Unable to retrieve your location";
            };

            output.innerHTML = "<p>Locating…</p>";
            navigator.geolocation.getCurrentPosition(success, error);
            
            console.log(latitude,longtitude,"001");
        },
        previous () {
            this.$router.go(-1);
        },
        next () {
            this.$router.go('/');
        }
    }
}
</script>

<style lang="scss">
.page {
  position: relative;
  top: 14px;
  padding: 18px 100px;
  height: 44px;
    .dot{
      span{
        display: inline-flex;
        justify-content: space-around;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #ffffff;
        margin: 18px 10px;
      }
    }
    span:nth-child(1) {
        opacity: 1;
    }
    span:nth-child(2) {
      opacity: 0.2;
    }
}
.container {
  position: relative;
  margin: 30px auto;
  width: 316px;
  height: 311px;
  display: flex;
  flex-direction: column;
  background-color: #59575B;
  border-radius: 25px;
  .content {
    position: relative;
    margin: 50px 50px;
    line-height: 28px;
    font-size: 24px;
    font-weight: normal;
    text-align: center;
    color: #ffffff;
  }
  .block {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    .inputbox {
      padding: 16px 20px;
      width: 210px;
      height: 28px;
      border: 0;
      background-color: #EAEAEA;
      border-radius: 10px;
      align-content: center;
      .inputPlace {
        padding: 0;
        height: 28px;
        font-style: normal;
        font-weight: normal;
        font-size: 20px;
        letter-spacing: 0.15px;
        color: #59575B;
        background-color: transparent;
        border: none;
      }
    }
    .hint {
      position: absolute;
      margin: 22.5px;
      font-size: 16px;
      line-height: 18.75px;
      color: #9E9E9E;
      left: 38px;
      top: 60px;
    }
  }
}
.step {
  position: relative;
  height: 60px;
  margin: 30px auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  Button {
    width: 143px;
    height: 60px;
    margin: 15px 15px;
    text-align: center;
    font-style: normal;
    font-weight: normal;
    font-size: 34px;
    line-height: 40px;
    letter-spacing: 0.25px;
    color: #ffffff;
    border: 0;
    border-radius: 10px;
  }
  Button:nth-child(1) {
      background-color: #738EEB;
  }
  Button:nth-child(2) {
      background-color: #9F9F9F;
      &.active {
          background-color: #738EEB;
      }
  }
}
</style>