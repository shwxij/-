<template>
	 <view class="container loading6">
		<view class="shape shape1"></view>
		<view class="shape shape2"></view>
		<view class="shape shape3"></view>
		<view class="shape shape4"></view>
	</view>
</template>

<script>
	export default {
		name: 'loading6',
		data() {
			return { };
		}
	}
</script>
<style scoped>
.container {
  width: 30px;
  height: 30px;
  position: relative;
}

.container.loading6 {
  animation-name: rotation;
  animation-duration: 1s;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
@keyframes rotation {
  0% { transform: rotate(0deg);}
  100% { transform: rotate(360deg);}
}

.container.loading6 .shape {
  width: 12px;
  height: 12px;
  border-radius: 2px;
}
.container .shape {
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 1px;
}
.container .shape.shape1 {
  left: 0;
  background-color: #1890FF;
}
.container .shape.shape2 {
  right: 0;
  background-color: #91CB74;
}
.container .shape.shape3 {
  bottom: 0;
  background-color: #FAC858;
}
.container .shape.shape4 {
  bottom: 0;
  right: 0;
  background-color: #EE6666;
}

/* ================== 动画部分 ===================== */
.loading6 .shape1 {
  animation-name: animation6shape1;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: normal;
}
@keyframes animation6shape1 {
  0% { transform: translate(0, 0);}
  25% { transform: translate(0, 18px);}
  50% { transform: translate(18px, 18px);}
  75% { transform: translate(18px, 0);}
}

.loading6 .shape2 {
  animation-name: animation6shape2;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: normal;
}
@keyframes animation6shape2 {
  0% { transform: translate(0, 0);}
  25% { transform: translate(-18px, 0);}
  50% { transform: translate(-18px, 18px);}
  75% { transform: translate(0, 18px);}
}

.loading6 .shape3 {
  animation-name: animation6shape3;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: normal;
}
@keyframes animation6shape3 {
  0% { transform: translate(0, 0);}
  25% { transform: translate(18px, 0);}
  50% { transform: translate(18px, -18px);}
  75% { transform: translate(0, -18px);}
}

.loading6 .shape4 {
  animation-name: animation6shape4;
  animation-duration: 2s;
  animation-timing-function: linear;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: normal;
}
@keyframes animation6shape4 {
  0% { transform: translate(0, 0);}
  25% { transform: translate(0, -18px);}
  50% { transform: translate(-18px, -18px);}
  75% { transform: translate(-18px, 0);}
}
</style>