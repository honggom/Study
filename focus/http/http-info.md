##### 일반 정보
- From : 유저 에이전트의 이메일 정보
- Referer : 이전 웹 페이지 주소
- User-Agent : 유저 에이전트 애플리케이션 정보
- Server : 요청을 처리하는 오리진 서버의 소프트웨어 정보
- Date : 메시지가 생선된 날짜

##### From
- 일반적으로 잘 사용되지 않음
- 검색 엔진 같은 곳에서, 주로 사용
- 요청에서 사용

##### Referer
- 현재 요청된 페이지의 이전 웹 페이지 주소
- A -> B로 이동하는 경우 B를 요청할 때 Referer: A를 포함해서 요청
- Referer를 사용해서 유입 경로 분석 가능
- 요청에서 사용
- 참고 : referer는 단어 referrer의 오타

##### User-Agent
- 클라이언트의 애플리케이션 정보 (웹 브라우저 정보, 등등)
- 통계 정보
- 어떤 종류의 브라우저에서 장애가 발생하는지 파악 가능 
- 요청에서 사용

##### Server 요청을 처리하는 ORIGIN 서버의 소프트웨어 정보
- server: nginx
- 응답에서 사용

##### Date (메시지가 발생한 날짜와 시간)
- 응답에서 사용

##### 특별한 정보
- Host : 요청한 호스트 정보
- Location : 페이지 리다이렉션
- Allow : 허용 가능한 HTTP 메서드
- Retry-After : 유저 에이전트가 다음 요청을 하기까지 기다려야 하는 시간

##### Host
- 요청에서 사용
- 필수 
- 하나의 서버가 여러 도메인을 처리해야 할 때
- 하나의 IP 주소에 여러 도메인이 적용되어 있을 때

##### Location
- 웹 브라우저는 3xx 응답의 결과에 Location 헤더가 있으면, Location 위치로 자동 이동 (리다이렉트)
- 201 (Created) : Location 값은 요청에 의해 생성되 리소스 URI
- 3xx (Redirection) : Location 값은 요청을 자동으로 리디렉션하기 위한 대상 리소스를 가리킴

##### Allow (허용 가능한 메서드)
- 405 (Method Not Allowed) 에서 응답에 포함해야 함
- Allow : GET, HEAD, PUT

##### Retry-After (유저 에이전트가 다음 요청을 하기까지 기다려야 하는 시간)

##### 인증
- Authorization : 클라이언트 인증 정보를 서버에 전달
- WWW-Authenticate : 리소스 접근시 필요한 인증 방법 정의

##### Authorization (클라이언트 인증 정보를 서버에 전달)
- Authorization: Basic xxxxxxxxxxxx

##### WWW-Authenticate (리소스 접근시 필요한 인증 방법 정의)
- 리소스 접근시 필요한 인증 방법 정의
- 401 Unauthorized 응답과 함께 사용