# `sync`
부모와 자식 컴포넌트 사이의 양방향 데이터 바인딩이 가능하게 해주는 syntax sugar

## 사용 예

### parentComponent.vue
```javascript
<template>
  <div>
    접속중인 {{ mySiteName }} 사이트입니다.
    <br />
    <child-component :my-sitename.sync="mySitename" />
  </div>
</template>

<script>
export default {
  data: {
    return function() {
      mySitename: 'webisfree.com'
    }
  }
}
</script>
```

### child-component.vue
```javascript
<template>
  <div>
    {{ mySitename }}
    <br /><br />
    <button @click="updateName">[ 바꾸기 ]</button>
  </div>
</template>

<script>
export default {
  props: [ 'mySitename' ],
  methods: {
    updateName: function() {
      this.$emit('update:mySitename', '');
    }
  }
}
</script>
```
자식 컴포넌트에서 살펴볼 부분은 아래와 같다.
```javascript
this.$emit('update:mySitename', '');
```
위와 같이 $emit()을 사용하여 값을 업데이트 한다.

이처럼 자식 컴포넌트에서 sync가 적용된 props 값을 바꾸기 위해서 다음과 같은 문법을 사용해야 한다.
```javascript
this.$emit('update:prop이름', 변경할 값);
```

이제 버튼을 클릭할 경우 update 함수가 동작하며 부모 컴포넌트에 적용된 
mySitename의 값을 빈 값인 ''로 업데이트 하게된다.

---

# 사용 예

```javascript
<comp :foo.sync="bar"></comp>
```
위 코드는 아래와 같다.
```javascript
<comp :foo="bar" @update:foo="val => bar = val"></comp>
```
하위 컴포넌트가 foo를 갱신하려면 속성을 변경하는 대신 명시적으로 이벤트를 보내야한다.
```javascript
this.$emit('update:foo', newValue)
```