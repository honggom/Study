# Gradle
## dependencies
- implementation : 의존 라이브러리 수정시 본 모듈까지만 재빌드한다.
본 모듈을 의존하는 모듈은 해당 라이브러리의 api 를 사용할 수 없음
- api : 의존 라이브러리 수정시 본 모듈을 의존하는 모듈들도 재빌드
본 모듈을 의존하는 모듈들도 해당 라이브러리의 api 를 사용할 수 있음
- compileOnly : 이름에서 알 수 있듯이 compile 시에만 빌드하고 빌드 결과물에는 포함하지 않는다.
runtime 시 필요없는 라이브러리인 경우 (runtime 환경에 이미 라이브러리가 제공되고 있는가 하는 등의 경우)
- runtimeOnly : runtime 시에만 필요한 라이브러리인 경우
- annotationProcessor : annotation processor 명시 (ex:lombok)
- testImplementation : 테스트 코드를 수행할 때만 적용.