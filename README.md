# 코드 레벨업

## 공통
- 최대한 쉽고 멍청하게(간략하게) 작성한다.
- 하나의 함수는 무조건 하나의 기능만 하게 작성한다.
- 분기는 최대한 피하는게 좋은 듯 하다..
- 라이브러리, api를 사용하려면 최대한 제공하는 기능으로 해결하자..(안 그러고 직접 만들어 쓰면 코드만 길어짐..)

## JavaScript
- JS는 onload 깔고 가는게 편하다.
- 코드 영역 나누기 > 1. 변수 2. 함수 3. 이벤트 4. 동작코드
- 콜백 함수의 정의 :
  - 어떤 이벤트에 의해 호출되어지는 함수 ex) click keyup ..
  - 다른 함수의 인자로써 사용되는 함수
  
![캡처](https://user-images.githubusercontent.com/67107008/120966888-d1e46380-c7a1-11eb-801e-16dea1793fa7.PNG)
<br>위 상황 속 printHello(), printBye()

## Java
- Vo는 필요에 맞게 쪼개 쓰기
- 모든 Req, Res를 Vo로 쓰려고 고집하기 보다는 적당히 변수(ex: int, String...)로 요청하고 받는게 가독성이 좋은 듯
- DB result는 String으로 받는게 편함 int로 받으면 null을 받아야 될 것 같은 경우에 0을 받음../mybatis int 결과 null로 받고 싶으면 Integer쓰면 됨

## DB
- WHERE 1=1 넣어주면 동적 쿼리 추가 및 코드 정리가 편하다.

## ETC
- for문 사용팁

![arr](https://user-images.githubusercontent.com/67107008/117932069-ebc58e80-b33a-11eb-8f73-319efef09f15.PNG)

## 알고리즘
- 노트에 경우의 수를 적어보며 규칙을 찾아본다.
- 코드 작성보다 규칙을 찾는게 우선

## 코딩하며 느낀 점
- 함수를 작성할 때 최대한 독자적으로 작동하는 함수를 작성하는 것이 좋다.
