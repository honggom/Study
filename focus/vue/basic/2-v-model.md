# `v-model`
`v-model`은 `value` 속성과 `input` 이벤트를 함께 사용하는 것과 같다. 
즉, `v-model`을 사용한다는 것은 `input` 이벤트가 발생 했을 때, `value` 값을 변경하는 것과 동일하다.

v-model은 내부적으로 서로 다른 속성을 사용하고 서로 다른 입력 요소에 대해 서로 다른 이벤트를 전송한다.

- text 와 textarea 태그는 value속성과 input이벤트를 사용한다.
- 체크박스들과 라디오버튼들은 checked 속성과 change 이벤트를 사용한다.
- Select 태그는 value를 prop으로, change를 이벤트로 사용한다.

--- 

# 사용 예

```javascript
<custom-input v-model="something">
```
위 문장은 아래와 같다.

```javascript
<input
  v-bind:value="something"
  v-on:input="something = $event.target.value">
```
```javascript
<custom-input
  :value="something"
  @input="value => { something = value }"> 
</custom-input>
```

### v-model 특징
- value prop를 가진다.
- 새로운 값으로 input 이벤트를 내보낸다.
- two-way binding로 value가 바뀌면 input이 바뀌고, input이 바뀌면 value가 바뀐다.