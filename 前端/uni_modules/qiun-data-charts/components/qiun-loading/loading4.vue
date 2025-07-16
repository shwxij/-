<template>
	 <view class="container loading5">
		<view class="shape shape1"></view>
		<view class="shape shape2"></view>
		<view class="shape shape3"></view>
		<view class="shape shape4"></view>
	</view>
</template>

<script>
	export default {
		name: 'loading5',
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

.container.loading5 .shape {
  width: 15px;
  height: 15px;
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

/* ------------------ 
  uvue/uni-app x 兼容动画写法：
  1. animation 属性改为 animation-name/animation-duration/animation-timing-function/animation-iteration-count/animation-direction
  2. 只保留标准 @keyframes，去掉 @-webkit-keyframes
-------------------*/

.loading5 .shape1 {
  animation-name: animation5shape1;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: reverse;
}
@keyframes animation5shape1 {
  0% {
    transform: translate(0, 0);
  }
  25% {
    transform: translate(0, 15px);
  }
  50% {
    transform: translate(15px, 15px);
  }
  75% {
    transform: translate(15px, 0);
  }
}

.loading5 .shape2 {
  animation-name: animation5shape2;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: reverse;
}
@keyframes animation5shape2 {
  0% {
    transform: translate(0, 0);
  }
  25% {
    transform: translate(-15px, 0);
  }
  50% {
    transform: translate(-15px, 15px);
  }
  75% {
    transform: translate(0, 15px);
  }
}

.loading5 .shape3 {
  animation-name: animation5shape3;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: reverse;
}
@keyframes animation5shape3 {
  0% {
    transform: translate(0, 0);
  }
  25% {
    transform: translate(15px, 0);
  }
  50% {
    transform: translate(15px, -15px);
  }
  75% {
    transform: translate(0, -15px);
  }
}

.loading5 .shape4 {
  animation-name: animation5shape4;
  animation-duration: 2s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: reverse;
}
@keyframes animation5shape4 {
  0% {
    transform: translate(0, 0);
  }
  25% {
    transform: translate(0, -15px);
  }
  50% {
    transform: translate(-15px, -15px);
  }
  75% {
    transform: translate(-15px, 0);
  }
}
</style>