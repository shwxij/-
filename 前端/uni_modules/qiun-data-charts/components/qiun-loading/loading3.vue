<template>
	 <view class="container loading3">
		<view class="shape shape1"></view>
		<view class="shape shape2"></view>
		<view class="shape shape3"></view>
		<view class="shape shape4"></view>
	</view>
</template>

<script>
	export default {
		name: 'loading3',
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

.container.loading3 {
  animation-name: rotation;
  animation-duration: 1s;
  animation-iteration-count: infinite;
  animation-timing-function: linear;
}
@keyframes rotation {
  0% { transform: rotate(0deg);}
  100% { transform: rotate(360deg);}
}
.container.loading3 .shape1 {
  border-top-left-radius: 10px;
}
.container.loading3 .shape2 {
  border-top-right-radius: 10px;
}
.container.loading3 .shape3 {
  border-bottom-left-radius: 10px;
}
.container.loading3 .shape4 {
  border-bottom-right-radius: 10px;
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

.loading3 .shape1 {
  animation-name: animation3shape1;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation3shape1 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(5px, 5px);
  }
}
.loading3 .shape2 {
  animation-name: animation3shape2;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation3shape2 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(-5px, 5px);
  }
}
.loading3 .shape3 {
  animation-name: animation3shape3;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation3shape3 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(5px, -5px);
  }
}
.loading3 .shape4 {
  animation-name: animation3shape4;
  animation-duration: 0.5s;
  animation-timing-function: ease;
  animation-delay: 0s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}
@keyframes animation3shape4 {
  from {
    transform: translate(0, 0);
  }
  to {
    transform: translate(-5px, -5px);
  }
}
</style>