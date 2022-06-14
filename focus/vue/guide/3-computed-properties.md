# 기본 예
```javascript
export default {
  data() {
    return {
      author: {
        name: 'John Doe',
        books: [
          'Vue 2 - Advanced Guide',
          'Vue 3 - Basic Guide',
          'Vue 4 - The Mystery'
        ]
      }
    }
  },
  computed: {
    // a computed getter
    publishedBooksMessage() {
      // `this` points to the component instance
      return this.author.books.length > 0 ? 'Yes' : 'No'
    }
  }
}
```
`publishedBooksMessage`는 `computed property`를 정의한 것이다.  

템플릿 내부에서 평범한 프로퍼티 처럼 `computed property`를 바인딩 할 수 있다.   
또한 `this.publishedBooksMessage`는 `this.author.books`를 의존하게 되고 `this.author.books`가 바뀌게 되면 `this.publishedBooksMessage`가 업데이트 된다.

# Computed Caching vs Methods
```javascript
<p>{{ calculateBooksMessage() }}</p>
```
```javascript
// in component
methods: {
  calculateBooksMessage() {
    return this.author.books.length > 0 ? 'Yes' : 'No'
  }
}
```
computed 프로퍼티를 사용하는 대신 메서드를 정의해서 똑같은 결과를 얻을 수 있다.

하지만 둘 사이는 차이점이 있다. computed 프로퍼티는 의존하는 리액티브를 캐싱하고 있으며 리액티브가 변경될 시에만 재평가 되지만
메서드는 호출할 때마다 평가를 거치게 된다.

# Writable Computed
computed 프로퍼티는 기본적으로 getter only 이다. 
만약 computed 프로퍼티에 새로운 값을 할당하려고 하면 `runtime warning`를 받게된다. `setter`가 필요한 경우에
`setter`를 작성하여 사용할 수 있다.
```javascript
export default {
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe'
    }
  },
  computed: {
    fullName: {
      // getter
      get() {
        return this.firstName + ' ' + this.lastName
      },
      // setter
      set(newValue) {
        // Note: we are using destructuring assignment syntax here.
        [this.firstName, this.lastName] = newValue.split(' ')
      }
    }
  }
}
```
`this.fullName = 'John Doe'`이 실행되면 `setter`가 동작하여 `this.firstName`,`this.lastName` 가 업데이트 된다.

# Best Practices
### computed의 getter는 사이드 이펙트가 발생하지 않게 작성해야 된다.
computed는 다른 값을 기반으로 값을 파생하는 선언적인 방법으로 생각해야 된다. 

### computed 값을 직접 변경하는 것을 피하라.
computed는 일시적인 스냅샷이라고 생각해야 된다. 매번 값이 변경될 때마다 새로운 스냅샷이 생성된다.
스냅샷을 변경한다는 것은 말이 되지 않는다.