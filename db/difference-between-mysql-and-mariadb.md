# MySQL과 MariaDB 공통점 및 차이점

## 공통점
- MariaDB의 실행 프로그램들과 유틸리티는 모두 MySQL과 이름이 동일하며 호환된다.
- MySQL 5.x의 데이터 파일과 테이블 정의 파일(.FRM)은 MariaDB 5.x와 호환한다.
- 모든 클라이언트 API와 통신 프로토콜은 서로 호환한다.
- MySQL Connector(Java 및 C 클라이언트 라이브러러 등)는 모두 MariaDB에서 변경없이 사용 가능하다.
- MySQL 클라이언트 프로그램은 그대로 MariaDB 서버의 연결에 사용할 수 있다.

## 차이점
### 스토리지 엔진 비교
- 메모리 스토리지 엔진
  - mysql : MariaDB의 메모리 스토리지 엔진과 거의 동일하다.
  - maria : MySQL 코드 베이스에 포함된 MEMORY 스토리지 엔진을 기본으로 사용한다.
- 디스크 기반 내부 임시 테이블 스토리지 엔진
  - mysql : MySAM 스토리지 엔진을 사용하는 테이블을 생성하여 작업을 처리한다.
  - maria : 기본적으로 Aria 스토리지 엔진을 사용한다. 이것은 InnoDB와 
  비슷하게 인덱스하며 레코드 데이터까지 모두 메모리 캐시를 이용할 수 있기 때문에 MySAM에 비해서는 빠른 처리를 보장한다.
- 트랜잭션 지원 스토리지 엔진 
  - mysql : InnoDB 스토리지 엔진을 사용한다.
  - maria : PerconaServer에서 나온 XtraDB가 사용되었지만 10.0.7 버전부터는 InnoDB가 기본이 되었다고 한다.
- NoSQL 지원 엔진
  - mysql : Memcached 플러그인을 제공한다.
  - maria : Cassandra의 데이터를 MariaDB 서버를 통해 접근할 수 있다.
### 기능
- 스레드 풀
  - mysql : 엔터프라이즈 버전에서만 지원한다.
  - maria : MariaDB 5.1 버전부터 지원한다.
- 버퍼풀 프리 로드
  - mysql : MySQL 5.6 버전에서부터 InnoDB 버퍼풀의 덤프와 로딩 기능을 지원한다.
  - maria : XtraDB에서 버퍼 풀의 내용을 덤프하고, 
  덤프된 버퍼 풀 정보를 MariaDB 재시작 후 다시 버퍼 풀로 로딩할 수 있는 기능을 제공한다.
- SSD 지원
  - mysql : -
  - maria : XtraDB에서는 SSD 기반의 디스크 IO를 위한 블록 플러시 알고리즘을 지원한다.
- 롤(ROLE) 기반의 권한 관리
  - mysql : -
  - maria : 오라클과 같이 특정 유저 그룹을 위한 롤 생성이 가능하다.
- 반 동기화 레플리케이션
  - mysql : 플러그인 형태로 제공한다.
  - maria : -
- 가상 컬럼
  - mysql : -
  - maria : 1개 이상의 컬럼 값을 미리 별도의 컬럼에 저장하거나 쿼리처리 시점에 가공하여 보여 주는 기능
- 동적 컬럼
  - mysql : -
  - maria : NoSQL 처럼 사용할 수 있는 동적 컬럼 지원 가능
