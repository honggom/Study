With Options API, we can use the watch option to trigger a function whenever a reactive property changes:
```javascript
export default {
  data() {
    return {
      question: '',
      answer: 'Questions usually contain a question mark. ;-)'
    }
  },
  watch: {
    // whenever question changes, this function will run
    question(newQuestion, oldQuestion) {
      if (newQuestion.indexOf('?') > -1) {
        this.getAnswer()
      }
    }
  },
  methods: {
    async getAnswer() {
      this.answer = 'Thinking...'
      try {
        const res = await fetch('https://yesno.wtf/api')
        this.answer = (await res.json()).answer
      } catch (error) {
        this.answer = 'Error! Could not reach the API. ' + error
      }
    }
  }
}
```
```javascript
<p>
  Ask a yes/no question:
  <input v-model="question" />
</p>
<p>{{ answer }}</p>
```

The watch option also supports a dot-delimited path as the key:
```javascript
export default {
  watch: {
    // Note: only simple paths. Expressions are not supported.
    'some.nested.key'(newValue) {
      // ...
    }
  }
}
```

# Deep Watchers
`watch`는 기본적으로 얕다. 추적하고 있는 값이 새로 할당될때만 동작한다.
만약 Object의 프로퍼티가 변경되는 것을 추적하고 싶으면 deep watcher를 사용해야 한다.
```javascript
export default {
  watch: {
    someObject: {
      handler(newValue, oldValue) {
        // Note: `newValue` will be equal to `oldValue` here
        // on nested mutations as long as the object itself
        // hasn't been replaced.
      },
      deep: true
    }
  }
}
```

# Eager Watchers
watch기본적으로 지연: 감시하는 값이 변경될 때까지 콜백이 호출되지 않는다. 
그러나 어떤 경우에는 동일한 콜백 로직이 바로 실행되기 원할 수 있다.

handler함수와 immediate: true옵션이 있는 객체를 선언함으로써 watch의 콜백이 즉시 실행되도록 강제할 수 있다.
```javascript
export default {
  // ...
  watch: {
    question: {
      handler(newQuestion) {
        // this will be run immediately on component creation.
      },
      // force eager callback execution
      immediate: true
    }
  }
  // ...
}
```

# Callback Flush Timing
Vue가 업데이트 한 후 watch의 콜백에서 DOM에 액세스하려면 다음 flush: 'post'옵션 을 지정해야 한다.
```javascript
export default {
  // ...
  watch: {
    key: {
      handler() {},
      flush: 'post'
    }
  }
}
```

# this.$watch()
watch를 명령적으로 정의하는 것도 가능하다.
```javascript
export default {
  created() {
    this.$watch('question', (newQuestion) => {
      // ...
    })
  }
}
```

# Stopping a Watcher
기본적으로 컴포넌트가 unmounted 되면 watch는 중지하지만, 특이한 케이스에서 특정한 시점에 watch를 중단하고 싶을 수도 있다.
그럴 경우에는 아래와 같이 `$watch`가 반환하는 함수를 통해 watch를 중단할 수 있다.

```javascript
const unwatch = this.$watch('foo', callback)

// ...when the watcher is no longer needed:
unwatch()
```
