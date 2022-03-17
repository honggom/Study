##### HTTP 요청 메시지 예
```
GET /search?q=hello&hi=ko HTTP/1.1
Host: www.google.com
// 공백라인
```
- 요청 메시지도 body 본문을 가질 수 있음

##### HTTP 응답 메시지 예
```
HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 3423
// 공백라인
<html>
    <body>...</body>
</html>
```

##### HTTP 메시지 구조
```
start-line 시작라인
header 헤더
empty line 공백 라인 (CRLF)
message body
```

##### 시작 라인 (요청 메시지)
```
GET /search?q=hello&hi=ko HTTP/1.1
Host: www.google.com
```
- start-line = reauest-line
  - reauest-line = method SP (공백) request-target SP HTTP-version CRLF(엔터)
- method SP : HTTP 메서드 (GET: 조회)
  - 종류 : GET, POST, PUT, DELETE ...
  - 서버가 수행해야 할 동작 지정
    - GET : 리소스 조회
    - POST : 요청 내역 처리
- request-target : 요청 대상 (/search?q=hello&hi=ko)
- HTTP-version : HTTP Version

##### 시작 라인 (응답 메시지)
```
HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 3423

<html>
    <body>...</body>
</html>
```
- start-line = status-line
  - status-line = HTTP-version SP status-code SP reason-phrase CRLF
- HTTP 버전
- HTTP 상태 코드 : 요청 성공, 실패 등을 나타냄
  - 200 : 성공
  - 400 : 클라이언트 요청 오류
  - 500 : 서버내부 오류
- 이유 문구 : 사람이 이해할 수 있는 짧은 상태 코드 설명 글

##### HTTP 헤더
- header-field = field-name ":" OWS field-value OWS (OWD : 띄어쓰기 허용)
- 용도
  - HTTP 전송에 필요한 모든 부가 정보
  - ex) 메시지 바디의 내용, 메시지 바디의 크기, 압축, 인증, 요청 클라이언트 정보, 서버애플리케이션 정보,
  캐시 관리 정보 ...
  - 표준 헤더가 너무 많음
  - 필요시 임의의 헤더 추가 가능

##### HTTP 메시지 바디
- 실제 전송할 데이터
- HTML 문서, 이미지, 영상, JSON 등등 byte로 표현할 수 있는 모든 데이터 전송 가능