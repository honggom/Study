# SQL-Injection
프로그램의 보안 취약점을 이용해, 악의적인 SQL문을 실행시켜 데이터베이스를 비정상적으로 조작하는 해킹 방법이다.

## 예시
```sql
SELECT * FROM user WHERE ID = '' AND PWD = ''
```
에를 들어 위와 같은 쿼리를 통해 사용자의 로그인을 처리하고 있고,   

해당 파라미터들을 아래와 같이 요청 받을 떄,
```
http://something.com/login?id=some-id&pwd=some-pwd
```
악의적인 사용자가   
- id : 'admin'
- pwd : 'OR 1=1--'   

위와 같은 파라미터로 요청하게 되면 아래와 같은 쿼리로 요청이 가게 될 것이고,
```sql
SELECT * FROM user WHERE ID = 'admin' AND PWD = '' OR 1 = 1 --
```
'--' 뒤로부터는 주석처리가 되고,   
where 결과가 무조건 참이 되므로 `로그인`이 성공 될 것이다.

## 예방책
### 입력값 검증
- 입력값을 검사하여 SQLI를 예방하는 방법이다. SQLI에 쓰이는 특수문자나, 
SQL 명령어들이 있는지 검사한다. 하지만 이 방법은, 정교하게 입력값을 검사하지 
않는다면 검증을 우회하는 방법들이 존재하므로 사용에 주의해야 한다.

### Prepared Statement
- Prepared Statement란, 미리 쿼리에 대한 컴파일을 수행하고, 입력값을 나중에 넣는 방식이다. 
그렇게 함으로써 비정상적인 입력값이 들어와도, 이미 쿼리 플랜(Query Plan)이 세워져 있으므로 SQLI를 막을 수 있게 된다.