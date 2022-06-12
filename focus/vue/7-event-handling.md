# Listening to Events
DOM 이벤트를 listen 하거나 JavaScript를 사용하기 위해 `v-on`를 사용할 수 있다.

`v-on:click="handler"`

handler의 value는 아래 두 개 중 하나가 될 수 있다.

1. Inline handlers : 이벤트가 트리거 됐을 때 실행되기 위한 인라인 JavaScript (네이티브 `onClick`와 비슷하다.)
2. Method handlers : 컴포넌트에 정의된 프로퍼티나 메소드 경로

# Inline handlers
```javascript
data() {
  return {
    count: 0
  }
}
```
```javascript
<button @click="count++">Add 1</button>
<p>Count is: {{ count }}</p>
```

# Method handlers
로직이 복잡한 경우 인라인 핸들러만 가지고 구현이 불가능 핤 수 있다.
이게 바로 `v-on`이 컴포넌트가 정의한 메서드나 프로퍼티를 호출할 수 있는 이유다.
```javascript
data() {
  return {
    name: 'Vue.js'
  }
},
methods: {
  greet(event) {
    // `this` inside methods points to the current active instance
    alert(`Hello ${this.name}!`)
    // `event` is the native DOM event
    if (event) {
      alert(event.target.tagName)
    }
  }
}
```
```javascript
<!-- `greet` is the name of the method defined above -->
<button @click="greet">Greet</button>
```
메서드 핸들러는 자동으로 네이티브 DOM 이벤트를 받는다.

## Method vs. Inline Detection
템플릿 컴파일러는 `v-on`의 String value를 확인하여 올바른 JavaScript 식별자인지 감지한다.
예를 들어, `foo`, `foo.bar` 그리고 `foo['bar']`는 method handlers로 감지되고,
`foo()` 그리고 `count++`는 inline handlers로 감지된다.

# Calling Methods in Inline Handlers
메서드 이름을 바로 바인딩하는 대신에 인라인 핸들러 안에 메서드를 호출할 수 있다.
이 방법은 네이티브 이벤트 대신에 커스텀한 인자를 메서드에 넘길 수 있다.
```javascript
methods: {
  say(message) {
    alert(message)
  }
}
```
```javascript
<button @click="say('hello')">Say hello</button>
<button @click="say('bye')">Say bye</button>
```

# Accessing Event Argument in Inline Handlers
때로는 인라인 핸들러에서 오리지널 DOM 이벤트에 접근해야 될 때도 있다.
`$event`라는 특수 변수를 사용하여 메서드에 이벤트를 전달할 수 있다. 또는 화살표 함수를 사용하면 된다.
```javascript
<!-- using $event special variable -->
<button @click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>

<!-- using inline arrow function -->
<button @click="(event) => warn('Form cannot be submitted yet.', event)">
  Submit
</button>
```
```javascript
methods: {
  warn(message, event) {
    // now we have access to the native event
    if (event) {
      event.preventDefault()
    }
    alert(message)
  }
}
```
# Event Modifiers
`event.preventDefault()` 또는 `event.stopPropagation()`는 매우 빈번하게 호출하게 된다.
메서드 내에서 이 작업을 쉽게 수행할 수 있지만 메서드가 DOM 이벤트 세부 정보를 처리하는 것보다 순전히 데이터 로직에만 관여한다면 더 좋을 것이다.

이 문제를 해결하기 위해 Vue는 이벤트 수정자를 제공한다.

- .stop
- .prevent 
- .self
- .capture
- .once
- .passive

```javascript
<!-- the click event's propagation will be stopped -->
<a @click.stop="doThis"></a>

<!-- the submit event will no longer reload the page -->
<form @submit.prevent="onSubmit"></form>

<!-- modifiers can be chained -->
<a @click.stop.prevent="doThat"></a>

<!-- just the modifier -->
<form @submit.prevent></form>

<!-- only trigger handler if event.target is the element itself -->
<!-- i.e. not from a child element -->
<div @click.self="doThat">...</div>
```
> 이벤트 수정자를 사용할 때는 순서가 중요함

# Key Modifiers
키보드 이벤트를 실행하기 위해, 자주 특정 키를 확인해야 될 때가 있다.
Vue는 key modifiers를 제공해 키보드 이벤트를 처리할 수 있다.
```javascript
<!-- only call `vm.submit()` when the `key` is `Enter` -->
<input @keyup.enter="submit" />
```
kebab-case로 변환하여 수정자로 키 이름을 직접 사용할 수 있다.
```javascript
<input @keyup.page-down="onPageDown" />
```

# Key Aliases
Vue는 자주 사용되는 keys를 별칭으로 제공한다.
- .enter
- .tab
- .delete (captures both "Delete" and "Backspace" keys)
- .esc
- .space
- .up
- .down
- .left
- .right

# System Modifier Keys
- .ctrl
- .alt
- .shift
- .meta

# .exact Modifier
```javascript
<!-- this will fire even if Alt or Shift is also pressed -->
<button @click.ctrl="onClick">A</button>

<!-- this will only fire when Ctrl and no other keys are pressed -->
<button @click.ctrl.exact="onCtrlClick">A</button>

<!-- this will only fire when no system modifiers are pressed -->
<button @click.exact="onClick">A</button>
```

# Mouse Button Modifiers
- .left
- .right
- .middle
