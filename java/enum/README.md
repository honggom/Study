## Enum
    Enum이란 Enumeration의 앞 글자로 열거라는 의미를 갖는다. 
    관련이 있는 상수들의 집합이다. 자바에서는 final로 String과 같은 
    문자열이나 숫자들을 나타내는 기본 자료형의 값을 고정할 수 있다. 
    이렇게 고정된 값을 상수라고 하고, 영어로는 constant라고 한다. 
    어떤 클래스가 상수만으로 작성되어 있으면 반드시 class로 선언할 필요는 없다. 
    이럴 때 class로 선언된 부분에 enum이라고 선언하면 이 객체는 상수의 집합이다. 
    라는 것을 명시적으로 나타낸다.

### 특징
1. 클래스를 상수처럼 사용 할 수 있다.
    - Enum 클래스에서 선언한 상수들은 클래스가 로드될 때 하나의 인스턴스로 생성되어 싱글톤 
      형태로 어플리케이션 전체에서 사용된다. 싱글톤 으로 사용되기 때문에 각각의 Enum 인스턴스에 
      변수를 추가하여 사용하는 것은 Multi Thread 환경에서 위험할 수 있다. 아래의 예시를 보면 각각의 
      인스턴스에 count 라는 변수가 추가되어 있는데 외부에서 각 등수에 맞게 plusCount() 를 호출 할 수 있다. 
      하지만 멀티 쓰레드 환경에서는 각 인스턴스의 count가 공유되고 있기 때문에 조심해야 한다
      ```java
      public enum Rank {
    	    THREE(3, 4_000),
    	    FOUR(4, 10_000),
    	    FIVE(5, 30_000);
    	
    	    private final int match;
    	    private final int money;
    	    private int count;
    	
    	    Rank(int match, int money) {
    		    this.match = match;
    		    this.money = money;
    	    }
    
    	    public void plusCount() {
    		    this.count++;
    	    }
      }
      ```
2. Enum 클래스를 구현하는 경우 상수 값과 같이 유일하게 하나의 인스턴스가 생성되어 사용된다.
3. 서로 관련 있는 상수 값들을 모아 enum으로 구현하는 경우 유용하다.
4. 클래스와 같은 문법 체계를 따른다.
5. 상속을 지원하지 않는다.

### Enum의 내부 Api
1. values()
    - values() 는 Enum 클래스가 가지고 있는 모든 상수 값을 배열의 형태로 리턴 한다. 
      참고로 단순히 String 의 형태로 단순 반환하는 것이 아니라 인스턴스를 반환하는 것이다. 
      즉 Enum 클래스가 가지고 있는 모든 인스턴스를 배열에 담아 반환하는 것이다.
      ```java
      public static void main(String[] args) {
    		    Rank[] values = Rank.values();
    		    for(int i = 0; i< values.length; i++) {
    			    System.out.println(values[i]);
    		    }
      }
      // 실행 결과 : THREE, FOUR, FIVE
      ```
2. valueOf()
    - valueOf() 메서드는 String 을 파라미터로 받는데 인자로 들어온 String과 
      일치하는 상수 인스턴스가 존재하면 그 인스턴스를 반환한다. 
      이 또한 마찬가지로 단순히 문자열을 반환하는 것이 아니라 인자로 
      들어온 문자열과 일치하는 인스턴스를 반환하는 것이다.
      ```java
      public static void main(String[] args) {
          System.out.println(Rank.valueOf("THREE"));
      }
      // 실행 결과 : THREE
      ```
3. ordinal()
    - Enum 클래스 내부에 있는 상수들의 Index 를 리턴하는 메소드이다. 
      배열과 마찬가지로 0부터 인덱스가 시작하며 인덱스의 length 는 상수의 수 - 1 이다.
      ```java
      public static void main(String[] args) {
            Rank[] values = Rank.values();
            for(int i = 0; i< values.length; i++) {
    			    System.out.println(values[i] + "인덱스는 : " + values[i].ordinal());
            }
      }
      // 실행 결과
      THREE인덱스는 : 0
      FOUR인덱스는 : 1
      FIVE인덱스는 : 2
      ```
### 사용 및 활용
- 데이터의 그룹화 및 관리에 용이
    - 관련되어 있지만 관련성을 표시하기 힘든 형태의 데이터를 한 곳에서 관리할 수 있다. 
      예를 들어 경기 이 후 승리한 사람과 패배한 사람을 리스트로 관리한다고 생각해보자. 
      이 경우 리스트의 변수명을 통해 관리하거나 Player 라는 클래스를 각기 상속 받는 형태로 
      관리하는 등의 방법으로 관리 될 수 있다. 하지만 Enum을 사용한다면 보다 명확한 방법으로 
      이들의 관계를 가시적으로 표현 할 수 있다.
      ```java
      public enum  Winner {
            WINNER("승리", Arrays.asList("kyle","pobi","hello","world")),
            LOSER("패배", Arrays.asList("hodol","dunddoung","rutgo");
    
            private final String winner;
            private final List<String> list;
    
            Winner(String winner, List<String> list) {
                this.winner = winner;
                this.list = list;
            }
      }  
      ```
    - 단순히 관련 있는 데이터를 모아서 관리할 뿐만 아니라 자바에서 Enum은 완전한 클래스의 형태를 
      보이고 있기 때문에 관련 로직을 같은 Enum 클래스 내에서 관리할 수 있기 때문에 상태와 행위를 
      한 곳에서 관리 할 수 있다. 아래의 예들을 통해 승리자가 누구인지, 승리자가 몇 명인지 
      등 승리와 관련된 로직을 한 곳에서 관리할 수 있는 장점이 있다.
      ```java
      public boolean isWinner(String name) {
            return WINNER.list.contains(name);
      }
        
      public int getWinnerSize() {
            return WINNER.list.size();
      }
      ```
    - 비슷한 예로 구매한 로또와 당첨번호가 같은 갯수, 그리고 각 갯수에 대응하는 상금 등과 같이 
      관련된 데이터도 하나의 Enum으로 관리 할 수 있다. 로또의 당첨 개수와 당첨 금액을 관리하는 
      하나의 클래스로 클래스를 분리하지 않고도 두 데이터(일치한 갯수와 당첨 금액)의 연관성을 명확하게 
      보여준다. 뿐 아니라 일치한 수를 입력하면 그 수와 일치하는 인스턴스를 반환하는 메소드 등 상태와 
      연관있는 행위 또한 한 곳에서 관리 할 수 있는 장점이 있다.
      ```java
      public enum Statistic {
            THREE(3, 5000),
            FOUR(4, 50_000),
            FIVE(5, 1_500_000),
            BONUS(5, 3_000_000),
            SIX(6, 2_000_000_000);
    
            private final int matchingNumbers;
            private final int prize;
        
            Statistic(int matchingNumbers, int prize) {
                  this.matchingNumbers = matchingNumbers;
                  this.prize = prize;
            }
    
      public static Statistic getRank(int numberOfMatch) {
            return Arrays.stream(values())
                  .filter(statistic -> statistic.matchingNumbers == numberOfMatch)
                  .findFirst()
                  .orElseThrow(new IllegalArgumentException("일치하는 번호가 3미만입니다."))
            }
      ```