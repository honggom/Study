# Reactive State 정의
Options API에서는 `data option`을 통해 컴포넌트의 reactive state를 정의한다. `data option`은 fcuntion 이어야 하고 Object를 리턴하여야 한다. 
캄포넌트의 인스턴스가 생성되면 `data option` fucntion을 호출한다. 그리고 리턴된 Object를 reactivity system에 래핑한다.
```vue
export default {
  data() {
    return {
      count: 1
    }
  },

  // `mounted` is a lifecycle hook which we will explain later
  mounted() {
    // `this` refers to the component instance.
    console.log(this.count) // => 1

    // data can be mutated as well
    this.count = 2
  }
}
```
이러한 인스턴스 속성은 인스턴스가 처음 생성될 때만 추가되므로 data함수에서 반환된 객체에 모두 존재하는지 확인해야 한다. 
아직 사용할 수 없는 속성에 대해 null, undefined를 할당할 수 있다.

this에 새 속성을 직접 추가할 수 있다. 그러나 이러한 방식으로 추가된 속성은 사후 업데이트를 트리거할 수 없다.

Vue 내부적으로 API를 사용할 때 `$`, `_` 접두사를 사용하니 해당 접두사 사용은 피해야 한다.

# Method 정의
컴포넌트 인스턴스의 메서드를 추가히기 위해서는 `methods` 옵션을 사용하여야 한다. 
```javascript
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    // methods can be called in lifecycle hooks, or other methods!
    this.increment()
  }
}
```
Vue는 항상 컴포넌트 인스턴스를 참조하도록 this값을 자동으로 바인딩한다. 
Vue가 적절한 methods을 바인딩하려면 methods 정의할 때 화살표 함수를 사용하지 않아야 한다.

# DOM Update Timing
```javascript
import { nextTick } from 'vue'

export default {
  methods: {
    increment() {
      this.count++
      nextTick(() => {
        // access updated DOM
      })
    }
  }
}
```
스테이트가 변경되고 DOM이 업데이트 되는 것을 기다리려면 `nextTick()` global API를 사용하면 된다.

# 깊은 반응성
Vue에서 상태는 기본적으로 매우 반응적이다. 즉, 중첩된 객체나 배열을 변경하는 경우에도 변경 사항을 감지할 수 있다.
```javascript
export default {
  data() {
    return {
      obj: {
        nested: { count: 0 },
        arr: ['foo', 'bar']
      }
    }
  },
  methods: {
    mutateDeeply() {
      // these will work as expected.
      this.obj.nested.count++
      this.obj.arr.push('baz')
    }
  }
}
```

# Stateful Methods
어떤 경우에는 메소드 함수를 동적으로 생성해야 할 수도 있다. 예를 들어 디바운스된 이벤트 핸들러 생성:
```javascript
import { debounce } from 'lodash-es'

export default {
  methods: {
    // Debouncing with Lodash
    click: debounce(function () {
      // ... respond to click ...
    }, 500)
  }
}
```
그러나 이 접근 방식은 디바운스된 함수가 stateful 이기 때문에 재사용되는 문제가 있다.
(debounce 시간 동안 일부 내부 상태를 유지한다.) 
여러 구성 요소 인스턴스가 동일한 디바운스 기능을 공유하는 경우 서로 간섭한다.

각 컴포넌트가 debounce 함수를 단독적으로 사용하려면 아래와 같이 라이프 사이클 훅을 사용하면 된다.
```javascript
export default {
  created() {
    // each instance now has its own copy of debounced handler
    this.debouncedClick = _.debounce(this.click, 500)
  },
  unmounted() {
    // also a good idea to cancel the timer
    // when the component is removed
    this.debouncedClick.cancel()
  },
  methods: {
    click() {
      // ... respond to click ...
    }
  }
}
```
