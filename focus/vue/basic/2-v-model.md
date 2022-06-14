# `v-model`
`v-model`은 `value` 속성과 `input` 이벤트를 함께 사용하는 것과 같다. 
즉, `v-model`을 사용한다는 것은 `input` 이벤트가 발생 했을 때, `value` 값을 변경하는 것과 동일하다.

v-model은 내부적으로 서로 다른 속성을 사용하고 서로 다른 입력 요소에 대해 서로 다른 이벤트를 전송한다.

- text 와 textarea 태그는 value속성과 input이벤트를 사용한다.
- 체크박스들과 라디오버튼들은 checked 속성과 change 이벤트를 사용한다.
- Select 태그는 value를 prop으로, change를 이벤트로 사용한다.