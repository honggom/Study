# 논리 자료형(Boolean) 전달
```javascript
<!-- 값이 없는 prop은 `true` 를 전달합니다.. -->
<blog-post is-published></blog-post>

<!-- `false`는 정적인 값이지만, Vue에서 해당 값이 논리 자료형이라는 것을 알 수 있도록 하기 위해 -->
<!-- v-bind를 이용해 문자열이 아닌 JavaScript 표현식이라는 것을 알려줍니다.                -->
<blog-post v-bind:is-published="false"></blog-post>

<!-- 변수의 값을 동적으로 할당할 수도 있습니다. -->
<blog-post v-bind:is-published="post.isPublished"></blog-post>
```