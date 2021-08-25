# Git - Commit Message Convention
    type: subject

    body

    footer

### Type
- feat : 새로운 기능 추가
- fix : 버그 수정
- design : CSS 등 사용자 UI 변경
- !breaking change : 커다란 API 변경
- !hotfix : 급하게 치명적인 버그를 고쳐야 하는 경우
- comment : 필요한 주석 추가 및 변경
- docs : 문서 수정
- style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- refactor : 코드 리팩토링
- test : 테스트 코드, 리팩토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정
- rename : 파일 혹은 폴더명을 수정 또는 옮기기만 한 경우
- remove : 파일을 삭제하는 작업만 수행한 경우

### Subject
- 제목은 50 글자를 넘기지 않는다.
- 대문자로 시작하고 마침표를 붙이지 않는다
- 과거시제를 사용하지 않는다.

### Body
- 옵셔널한 사항이기 때문에 꼭 작성할 필요는 없다.
- 제목과 구분되기 위해 한칸 띄워 작성한다.

### Footer
- 옵셔널한 사항이기 때문에 꼭 작성할 필요는 없다.
- 이슈 트래커 아이디를 작성할 때 사용한다. (ex: #123)
