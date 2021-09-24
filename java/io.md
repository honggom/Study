## 자바 입력
### System.in과 InputStream의 관계
- System.in은 InputStream 타입이다.
### 가장 기본적인 입력 스트림 InputStream
- 1 Byte만 읽음
### InputStreamReader 
- 문자를 온전하게 받기 위한 중개자 역할을 함
- 바이트 단위 데이터를 문자(character) 단위 데이터로 처리할 수 있도록 변환해준다.
- char 배열로 데이터를 받을 수 있다.
### Scanner
- InputStream (바이트스트림) 을 통해 입력 받음
- 문자로 온전하게 받기 위해 중개자 역할을 하는 InputStreamReader(문자스트림) 을 통해 char 타입으로 데이터를 처리함
- 정규식 문자열을 Pattern.compile() 이라는 메소드를 통해 Pattern 타입으로 변환함
### BufferedReader 
- BufferedReader도 마찬가지로 InputStream (바이트스트림) 을 통해 입력 받는다.
- 또 System.in 은 바이트스트림인 InputStream 타입이고 이 입력방법만으로는 
문자를 온전하게 받기 힘드니 InputStreamReader 로 감싸주면서 바이트 단위 데이터를 
문자 단위로 처리할 수 있도록 한다.
```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```
- Buffer(버퍼)를 통해 입력받은 문자를 쌓아둔 뒤 한 번에 문자열처럼 보낸다.