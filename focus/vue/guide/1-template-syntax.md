# Mustache

```vue
<span>Message: {{ msg }}</span>
```
`mustache` 태그는 컴포넌트 인스턴스의 msg 프로퍼티의 값으로 replace 된다. 또한 msg 프로퍼티의 값이
변경될 때마다 재렌더링된다.

# 속성(attribute) 바인딩
```vue
<div v-bind:id="dynamicId"></div>
```
- mustache는 HTML 속성 내에서 사용할 수 없다. 대신에 `v-bind` `directive(지시문)`를 사용해야 된다.
- `v-bind`는 요소의 속성을 컴포넌트의 id속성과 동기화 하도록 Vue에 
지시한다. 바인딩된 값이 null또는 undefined이면 속성이 렌더링된 요소에서 제거된.

# v-bind 단축
```vue
<div :id="dynamicId"></div>
```
`v-bind`는 일반적으로 많이 사용되기 때문에 단축된 구문으로 위와 같이 사용할 수 있다.

# Boolean 속성
```vue
<button :disabled="isButtonDisabled">Button</button>
```
`v-bind`는 위와 같이 `isButtonDisabled` 값이 Boolean 타입이라면 조금 다르게 동작한다.

만약 `isButtonDisabled` 값이 `truthy value`라면 아래와 같이 해석된다.
```vue
<button disabled="">
```
그렇지 않고 `isButtonDisabled` 값이 `falsy value`라면 속성이 제거된다.

# 여러 속성을 동적으로 바인딩 하는 법
```vue
data() {
  return {
    objectOfAttrs: {
      id: 'container',
      class: 'wrapper'
    }
  }
}
```
아래와 같이 `v-bind`인수 없이 사용하여 단일 요소에 바인딩할 수 있다.
```vue
<div v-bind="objectOfAttrs"></div>
```

# JavaScript 표현식 사용
```vue
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div :id="`list-${id}`"></div>
```
Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원한다.

Vue 템플릿에서 JavaScript 표현식은 다음 위치에서 사용할 수 있다.
- Mustache
- 모든 Vue 지시문의 속성 값에서(로 시작하는 특수 속성 v-)

# 함수 호출
바인딩 식 내에서 메서드를 호출할 수 있다.
```vue
<span :title="toTitleDate(date)">
  {{ formatDate(date) }}
</span>
```

# Directive
`v-` `Directive`는 접두사 가 있는 특수 속성이다. 
Vue는 여러 내장 `Directive`을 제공한다.

- `Directive` 속성 값은 단일 JavaScript 표현식이어야 한다.( v-for, v-on및 v-slot, 제외). 
- `Directive` 역할은 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용하는 것이다.

# 동적 인수
대괄호로 감싸서 Directive 인수에서 JavaScript 표현식을 사용할 수도 있다.
```vue
<a v-bind:[attributeName]="url"> ... </a>

<!-- shorthand -->
<a :[attributeName]="url"> ... </a>
```
`attributeName`에서는 JavaScript 표현식으로 동적으로 평가되며 평가된 값은 인수의 최종 값으로 사용된다. 
예를 들어 컴포넌트 인스턴스에 `attributeName`값이 `"href"` 경우 `v-bind:href` 과 동일하다.

### 참조
- https://vuejs.org/guide/essentials/template-syntax.html