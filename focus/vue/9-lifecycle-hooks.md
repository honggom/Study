## Registering Lifecycle Hooks
예를 들어 `mounted` 훅은 컴포넌트가 초기 렌더링이 끝난 시점 또는 DOM 노드를 만든 직후에 코드를 실행할 수 있다.
```javascript
export default {
  mounted() {
    console.log(`the component is now mounted.`)
  }
}
```

# Lifecycle Diagram
모든 라이프사이클 훅은 this를 참조하기 때문 라이프사이클 훅을 화살표 함수로 작성하면 안 된다
![](../../../lifecycle.16e4c08e.png)