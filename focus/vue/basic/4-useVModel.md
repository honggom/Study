# useVModel
vueuse 라이브러리에서 제공하는 함수다. 양방향 데이터 바인딩을 간략하게 구현할 수 있게 해준다.

## 사용법
```javascript
import { useVModel } from '@vueuse/core'

export default {
  setup(props, { emit }) {
    const data = useVModel(props, 'data', emit)

    console.log(data.value) // props.data
    data.value = 'foo' // emit('update:data', 'foo')
  },
}
```

### `<script setup>`
```javascript
<script lang="ts" setup>
import { useVModel } from '@vueuse/core'

const props = defineProps<{
  modelValue: string
}>()
const emit = defineEmits(['update:modelValue'])

const data = useVModel(props, 'modelValue', emit)
</script>
```

## 겪었던 문제
`ParentComponent.vue`
```javascript
<ChildComponent
    v-model="something"
/>

<script setup>
  const something = ref(false);
</script>
```

`ChildComponent.vue`
```javascript
<script setup>
  const props = defineProps<{
    value: boolean
  }>();
  
  const vModel = useVModel(props, "value");
</script>
```
대충 위와 같이 구현돼 있었는데 ChildComponent에서 vModel값을 바꿔도 ParentComponent에서 값이
바뀌지 않으면서 양방향 데이터 바인딩이 일어나지 않았다.

우선 위 문제를 정확하기 위해서는 `v-model`에 대해 알아야 한다.

## `v-model`
`v-model`은 `value` 속성과 `input` 이벤트를 함께 사용하는 것과 같다.
즉, `v-model`을 사용한다는 것은 `input` 이벤트가 발생 했을 때, `value` 값을 변경하는 것과 동일하다.

v-model은 내부적으로 서로 다른 속성을 사용하고 서로 다른 입력 요소에 대해 서로 다른 이벤트를 전송한다.

- text 와 textarea 태그는 value속성과 input이벤트를 사용한다.
- 체크박스들과 라디오버튼들은 checked 속성과 change 이벤트를 사용한다.
- Select 태그는 value를 prop으로, change를 이벤트로 사용한다.

기본적으로 `v-model`에 대한 설명은 위와 같다.

---
### 예시

```javascript
<input v-model="something">
```
이 `v-model`은 아래와 완전히 같다.
```javascript
<input
  v-bind:value="something"
  v-on:input="something = $event.target.value">
```

컴포넌트도 마찬가지다.

```javascript
<cumstom-component v-model="something">
```

```javascript
<cumstom-component
  v-bind:value="something"
  v-on:input="something = $event.target.value">
```

---
위와 같이 Vue2 에서는 `v-model`을 사용하면 바인딩하는 prop을 `value`라는 이름으로 받고
값을 업데이트하기 위해 부모 컴포넌트에 보내는 이벤트명이 `input`이 기본값이다.

따라서 prop을 `value`로 값을 받고 이벤트를 `input`이라는 이름으로 보내야 한다.

하지만 위 사항을 숙지하고 있었고, `useVModel`을 사용하면 해당 부분을 자동으로 해주는 것으로 알고 있엇기 때문에
여전히 의문이 있었다.

그래서 내가 `useVModel`에 대하여 잘 모르고 있기 때문에 발생하는 문제라 생각해서 `useVModel`이 어떻게 구현되어 있나
소스를 직접 보기로 했다.

### `useVModel 소스`

```javascript
export function useVModel<P extends object, K extends keyof P, Name extends string>(
  props: P,
  key?: K,
  emit?: (name: Name, ...args: any[]) => void,
  options: VModelOptions<P[K]> = {},
) {
    ...
  if (!key) {
    if (isVue2) {
      const modelOptions = vm?.proxy?.$options?.model
      key = modelOptions?.value || 'value' as K
      if (!eventName)
        event = modelOptions?.event || 'input'
    }
    else {
      key = 'modelValue' as K
    }
  }
  event = eventName || event || `update:${key!.toString()}`
    ...
  if (passive) {
    ...
  }
  else { // 컴퓨티드로 리턴
    return computed<P[K]>({
      get() {
        return getValue()!
      },
      set(value) {
        _emit(event, value)
      },
    })
  }
}
```
위의 소스를 보면 알 수 있는데 만약 임시로 `key` 값을 보내주면 

```javascript
...
if (!key) {
  ...
}
...
```
위의 분기문을 지나치기 때문에 이벤트 명이 `input`이 아니라 `update:임의의 key`로 만들어 지게 된다.


따라서 자식 컴포넌트에서 값을 변경한다고 해도 `update:key`라는 이름의 이벤트를 발생시키기 `input`이벤트를 기대하는
부모 컴포넌트는 `update:key` 이벤트를 수신하지 않고 그렇기 때문에 양방향 데이터 바인딩이 이뤄지지 않는다.

결과적으로 `useVModel`로 `key`를 넘기지 않으면 Vue2나 Vue3 버전에 맞게 이벤트 명을 알아서 맞춰주기 때문에
문제는 해결된다.

하지만 위와 같이 `key`를 넘겨주지 않는 방식도 문제가 하나 있다. `key`를 넘겨주지 않으면 `useVModel`로 만들어진 `ref`의 타입을
정확히 인식하지 못하는 경우가 있다.

그렇기 때문에 아래와 같은 방식으로 타입을 인식하지 못하는 문제를 해결할 수 있다.
```javascript
const vModel = useVModel(props, "value", undefined, { eventName: "input" });
```

## 추가사항
위 문제를 겪으면서 `key`값을 임의로 넘기는데 정상적으로 동작하는 경우도 있었다.
동작하는 경우의 공통점이 있었는데 그것은 바로 부모 컴포넌트 입장에서 `v-model`을 사용하는 것이 아니라
`.sync`를 사용하는 경우였다.

### `.sync`

`.sync`도 양방향 데이터 바인딩을 구현할 때 사용하며 `v-model`과 유사하나 Vue2 기준에서는 다른 점이 하나있다.

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

--- 

위 설명처럼 Vue2 기준에서는 `.sync`는 양방향 데이터 바인딩을 구현하기 위해 사용하는 이벤트 명이 `update:something`이다.

그렇기 때문에 `useVModel`을 `key`값과 함께 사용해도 정상적으로 동작한다.

--- 
Vue3에서는 `v-model`과 `.sync`가 양방향 데이터 바인딩을 위해 사용하는 이벤트 명이 둘다 `update:something`이기 때문에
Vue3를 사용하고 있다면 사실 고민할 필요가 없는 문제다.

### 참고
- https://vueuse.org/core/usevmodel/
- https://kr.vuejs.org/v2/guide/components.html
- https://kr.vuejs.org/v2/guide/components.html#sync-%EC%88%98%EC%8B%9D%EC%96%B4
