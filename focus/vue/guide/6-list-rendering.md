# `v-for`
`v-for` 디렉티브를 사용하여 array를 렌더링 할 수 있다.
```javascript
data() {
  return {
    items: [{ message: 'Foo' }, { message: 'Bar' }]
  }
}
```
```javascript
<li v-for="item in items">
  {{ item.message }}
</li>
```
`index`에 접근하는 것도 가능하다.
```javascript
data() {
  return {
    parentMessage: 'Parent',
    items: [{ message: 'Foo' }, { message: 'Bar' }]
  }
}
```
```javascript
<li v-for="(item, index) in items">
  {{ parentMessage }} - {{ index }} - {{ item.message }}
</li>
```
- Parent - 0 - Foo
- Parent - 1 - Bar

---

`v-for`의 변수 스코프는 아래 JavaScript와 비슷하다.
```javascript
const parentMessage = 'Parent'
const items = [
  /* ... */
]

items.forEach((item, index) => {
  // has access to outer scope `parentMessage`
  // but `item` and `index` are only available in here
  console.log(parentMessage, item.message, index)
})
```
destructuring를 사용하는 예
```javascript
<li v-for="{ message } in items">
  {{ message }}
</li>

<!-- with index alias -->
<li v-for="({ message }, index) in items">
  {{ message }} {{ index }}
</li>
```
중첩 `v-for` 예
```javascript
<li v-for="item in items">
  <span v-for="childItem in item.children">
    {{ item.message }} {{ childItem }}
  </span>
</li>
```

`of`를 쓰는것도 가능하다.
```javascript
<div v-for="item of items"></div>
```

# `v-for` with an Object
object를 프로퍼티로 `v-for`를 사용하는 것도 가능하다.
```javascript
data() {
  return {
    myObject: {
      title: 'How to do lists in Vue',
      author: 'Jane Doe',
      publishedAt: '2016-04-10'
    }
  }
}
```
```javascript
<ul>
  <li v-for="value in myObject">
    {{ value }}
  </li>
</ul>
```
```javascript
<li v-for="(value, key) in myObject">
  {{ key }}: {{ value }}
</li>
```
```javascript
<li v-for="(value, key, index) in myObject">
  {{ index }}. {{ key }}: {{ value }}
</li>
```

# `v-for` with a Range
`v-for`는 integer를 받아 반복할 수 있다.
```javascript
<span v-for="n in 10">{{ n }}</span>
```
- n은 0이 아닌 1부터 시작한다.

# `v-for` on `<template>`
```javascript
<ul>
  <template v-for="item in items">
    <li>{{ item.msg }}</li>
    <li class="divider" role="presentation"></li>
  </template>
</ul>
```

# `v-for` with `v-if`
> 기본적으로 `v-for`와 `v-if`를 같이 쓰는 것은 추천하지 않는다.

같은 노드에 `v-for`와 `v-if`가 같이 있다면 `v-if`가 더 높은 우선순위를 갖는다. 
```javascript
<!--
This will throw an error because property "todo"
is not defined on instance.
-->
<li v-for="todo in todos" v-if="!todo.isComplete">
  {{ todo.name }}
</li>
```
따라서 위 `v-if`에서 todo에 접근할 수 없다.

아레와 같이 수정하면 정상적으로 동작
```javascript
<template v-for="todo in todos">
  <li v-if="!todo.isComplete">
    {{ todo.name }}
  </li>
</template>
```

# Maintaining State with `key`
Vue에서 `v-for`와 함께 list의 요소를 업데이트 하면 DOM 요소를 list의 순서와 일치시키기 위해 
움직이는 대신 렌더링 되야하는 요소만 특정해서 반영한다.

이러한 점은 기본적으로 효율적이지만 자식 컴포넌트의 스태이트에 의존하지 않고 임시 DOM 스테이트가 아닐때만 적절하다.

위 방법을 Vue가 사용하기 위해서는 `key`를 제공해줘야 한다.

```javascript
<div v-for="item in items" :key="item.id">
  <!-- content -->
</div>
```
```javascript
<template v-for="todo in todos" :key="todo.name">
  <li>{{ todo.name }}</li>
</template>
```