Form을 사용할 때 입력 요소의 상태를 JavaScript의 해당 상태와 동기화해야 하는 경우가 많다. 이런 상태를
동기화하는 것은 매우 번거롭다.
```javascript
<input
  :value="text"
  @input="event => text = event.target.value">
```

`v-model`은 위의 과정을 쉽게 처리해준다.
```javascript
<input v-model="text">
```
> Note
> > v-model will ignore the initial value, checked or selected 
> attributes found on any form elements. It will always treat the current 
> bound JavaScript state as the source of truth. You should declare the 
> initial value on the JavaScript side, using the data option.

# Basic Usage
```javascript
<p>Message is: {{ message }}</p>
<input v-model="message" placeholder="edit me" />
```

> Note
> > For languages that require an IME (Chinese, Japanese, Korean etc.), 
> you'll notice that v-model doesn't get updated during IME composition. 
> If you want to respond to these updates as well, use an input event listener 
> and value binding instead of using v-model.

# Multiline text
```javascript
<span>Multiline message is:</span>
<p style="white-space: pre-line;">{{ message }}</p>
<textarea v-model="message" placeholder="add multiple lines"></textarea>
```

```javascript
<!-- 동작하지 않음!!-->
<textarea>{{ text }}</textarea>

<!-- good -->
<textarea v-model="text"></textarea>
```

# Checkbox
한 개의 체크박스
```javascript 
<input type="checkbox" id="checkbox" v-model="checked" />
<label for="checkbox">{{ checked }}</label>
```

여러 체크박스를 하나의 Set 또는 Array에 바인딩 할 수 있다.
```javascript
export default {
  data() {
    return {
      checkedNames: []
    }
  }
}
```
```javascript
<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
<label for="jack">Jack</label>

<input type="checkbox" id="john" value="John" v-model="checkedNames">
<label for="john">John</label>

<input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
<label for="mike">Mike</label>
```

# Radio
```javascript
<div>Picked: {{ picked }}</div>

<input type="radio" id="one" value="One" v-model="picked" />
<label for="one">One</label>

<input type="radio" id="two" value="Two" v-model="picked" />
<label for="two">Two</label>
```

# Select
Single select:
```javascript
<div>Selected: {{ selected }}</div>

<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>
```
Multiple select (bound to array):
```javascript
<div>Selected: {{ selected }}</div>

<select v-model="selected" multiple>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>
```
Select options can be dynamically rendered with v-for:
```javascript
export default {
  data() {
    return {
      selected: 'A',
      options: [
        { text: 'One', value: 'A' },
        { text: 'Two', value: 'B' },
        { text: 'Three', value: 'C' }
      ]
    }
  }
}
```
```javascript
<select v-model="selected">
  <option v-for="option in options" :value="option.value">
    {{ option.text }}
  </option>
</select>

<div>Selected: {{ selected }}</div>
```

# Value Bindings
radio, checkbox 및 select 옵션의 경우 v-model의 바인딩 값은 일반적으로 정적 문자열이다.
```javascript
<!-- `picked` is a string "a" when checked -->
<input type="radio" v-model="picked" value="a" />

<!-- `toggle` is either true or false -->
<input type="checkbox" v-model="toggle" />

<!-- `selected` is a string "abc" when the first option is selected -->
<select v-model="selected">
  <option value="abc">ABC</option>
</select>
```
하지만 때로는 특정 문자열이 바인딩 되게 하고 싶을 때도 있다.

# Checkbox
```javascript
<input
  type="checkbox"
  v-model="toggle"
  true-value="yes"
  false-value="no" />
```
true-value, false-value는 오직 v-model과 같이 동작하고 Vue에서 제공하는 특수한 어트리뷰트다. 위 상황에서
checkbox가 체크되면 toggle에 yes가 바인딩 되고 반대는 no가 바인딩 된다.

```javascript
<input
  type="checkbox"
  v-model="toggle"
  :true-value="dynamicTrueValue"
  :false-value="dynamicFalseValue" />
```
위 처럼 v-bind를 사용하여 값을 바인딩 할 수도 있다.

# Radio
```javascript
<input type="radio" v-model="pick" :value="first" />
<input type="radio" v-model="pick" :value="second" />
```
첫 번째 라디오가 선택되면 pick에 first가 할당되고 두 번째 라디오가 선택되면 pick에 second가 할당된다.

# Select Options
```javascript
<select v-model="selected">
  <!-- inline object literal -->
  <option :value="{ number: 123 }">123</option>
</select>
```
위에 예제에서는 객체 리터럴이 selected 에 저장된다.

# Modifiers
## `.lazy`
v-model은 디폴트로 매 input event 마다 값을 동기화한다. 그러나 `.lazy` 수정자를 통해 `change` 이벤트 후에 동기화하게 할 수 있다.

## `.number`
자동으로 number로 타입캐스팅
```javascript
<input v-model.number="age" />
```

## `.trim`
자동으로 trim
```javascript
<input v-model.trim="msg" />
```