<template>
	 <view class="container loading2">
		<view class="shape shape1"></view>
		<view class="shape shape2"></view>
		<view class="shape shape3"></view>
		<view class="shape shape4"></view>
	</view>
</template>

<script>
	export default {
		name: 'loading2',
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

.container.loading2 {
  transform: rotate(10deg);
  animation-name: rotation;
  animation-duration: 1s;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
@keyframes rotation {
  0% { transform: rotate(0deg);}
  100% { transform: rotate(360deg);}
}
.container.loading2 .shape {
  border-radius: 5px;
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

/* 动画全部标准写法 */
.loading2 .shape1 {
  animation-name: animation2shape1;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation2shape1 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(20px, 20px);
  }
}
.loading2 .shape2 {
  animation-name: animation2shape2;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation2shape2 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(-20px, 20px);
  }
}
.loading2 .shape3 {
  animation-name: animation2shape3;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation2shape3 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(20px, -20px);
  }
}
.loading2 .shape4 {
  animation-name: animation2shape4;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation2shape4 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(-20px, -20px);
  }
}
</style>