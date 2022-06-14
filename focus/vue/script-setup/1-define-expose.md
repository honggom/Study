# 자식 컴포넌트 Child.vue 작성 및 defineExpose 사용
```javascript
<template>
  ...
    <div class="color" :style="{ backgroundColor }"></div>
  ...
</template>

<script setup>
function changeBackgroundColor(color) {
  backgroundColor.value = color;
}

// defineExpose를 통하여 함수를 내보낸다.
defineExpose({ changeBackgroundColor });
</script>
```

# 부모 컴포넌트 Parent.vue 작성 및 ref로 내보낸 자식 컴포넌트 함수 호출
```javascript
<!-- Parent.vue -->
<template>
  ...
    <button @click="clickColorChangeButton">button</button>
    <child ref="child" />
  ...
</template>

<script setup>
import { ref } from "vue";

// 설정한 ref 명이랑 똑같은 변수명으로 선언한다.
const child = ref("");

function clickColorChangeButton() {
  // 내보낸 자식 컴포넌트 함수를 호출한다.
  child.value.changeBackgroundColor(input.value.value);
}
</script>
```