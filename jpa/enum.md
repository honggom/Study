##### @Enumerated 
> EnumType.ORDINAL은 enum에 저장된 순서대로 값이 데이터베이스에 저장된다.
- 장점 : 데이터베이스에 저장되는 크기가 작다.
- 단점 : 이미 저장된 enum의 순서를 변경할 수 없다.

> EnumType.STRING은 enum의 이름 그대로 문자로 저장된다.
- 장점 : 저장된 enum의 순서가 바뀌거나 enum이 추가되어도 안전하다.
- 단점 : 데이터베이스에 저장되는 데이터 크기가 ORDINAL에 비해서 크다.