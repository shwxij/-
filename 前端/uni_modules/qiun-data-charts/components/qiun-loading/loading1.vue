<template>
	 <view class="container loading1">
		<view class="shape shape1"></view>
		<view class="shape shape2"></view>
		<view class="shape shape3"></view>
		<view class="shape shape4"></view>
	</view>
</template>

<script>
	export default {
		name: 'loading1',
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
.container.loading1 {
  transform: rotate(45deg);
}

/* 基础方块样式 */
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

/* 各角动画，全部用标准属性 */
.loading1 .shape1 {
  animation-name: animation1shape1;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation1shape1 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(16px, 16px);
  }
}
.loading1 .shape2 {
  animation-name: animation1shape2;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation1shape2 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(-16px, 16px);
  }
}
.loading1 .shape3 {
  animation-name: animation1shape3;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation1shape3 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(16px, -16px);
  }
}
.loading1 .shape4 {
  animation-name: animation1shape4;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation1shape4 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(-16px, -16px);
  }
}
</style>