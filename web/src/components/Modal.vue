<template>
  <transition name="slot-modal-transition">
    <div v-if="show" class="slot-modal">
      <div class="slot-modal__overlay" :class="{ 'full-screen-overlay': isFullScreen}" />
      <div class="slot-modal__window text-center">
        <div class="slot-modal__content">
          <slot />
        </div>
        <div>
          <button v-if="cancelText" class="btn btn-default rounded ripple" @click="cancel">{{ cancelText }}</button>
          <button v-if="okText" class="btn btn-tertiary rounded ripple" @click="ok">{{ okText }}</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Modal',
  props: ['show', 'okText', 'cancelText', 'isFullScreen'],
  data() {
    return {};
  },
  methods: {
    ok() {
      this.$emit('ok');
    },
    cancel() {
      this.$emit('cancel');
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss' scoped>
.slot-modal {
  position: fixed;
  z-index: 999;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.slot-modal__overlay {
  position: absolute;
  top: 45px;
  left: 0;
  width: 100%;
  height: calc(100% - 45px);
  background: rgba(0, 0, 0, 0.48);
  background-repeat: no-repeat;
  background-size: cover;
  opacity: 0.48;
  z-index: 999;
}

.full-screen-overlay {
  top: 0px;
  height: 100%;
}

.slot-modal__window {
  width: 280px;
  background-color: #ffffff;
  padding: 32px 29px 25px 29px;
  box-sizing: border-box;
  border-radius: 10px;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.29);
  z-index: 100;
  color: #28335C;
  z-index: 999;
}
.slot-modal__content {
  text-align: center;
  margin-bottom: 20px;
  font-size: 20px;
  line-height: 23px;
}
.btn {
  width: 61px;
  height: 43px;
  margin: 0 10px 0 10px;
  font-size: 20px;
  line-height: 23px;
  border-radius: 10px;
  text-align: center;
  &.btn-default {
    border: 0.5px solid #9e5e25;
    background-color: #ffffff;
    color: #9e5e25;
  }
  &.btn-tertiary {
    border: 0.5px solid #9e5e25;
    background-color: #9e5e25;
    color: #ffffff;
  }
}

.slot-modal-transition-enter-active,
.slot-modal-transition-leave-active {
  transition: .2s opacity ease-in-out;
}

.slot-modal-transition-enter,
.slot-modal-transition-leave-to {
  opacity: 0;
}
</style>
