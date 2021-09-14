### Junit Assert Methods
1. assertEquals(x, y) : 객체 x와 y가 일치함을 확인한다. x(예상 값)와 y(실제 값)가 같으면 테스트 통과
2. assertArrayEquals(a, b) : 배열 A와 B가 일치함을 확인한다.
3. assertFalse(x) :  x가 false 인지 확인한다.
4. assertTrue(x) : x가 true 인지 확인한다.
5. assertTrue(message, condition) : condition이 true이면 message를 표시한다.
6. assertNull(o) : 객체o가 null인지 확인한다.
7. assertNotNull(o) : 객체o가 null이 아닌지 확인한다.
8. assertSame(ox, oy) :  ox와 oy가 같은 객체를 참조하고 있으면 테스트 통과, 
assertEquals()메서드는 두 객체의 값이 같은지 확인하고, assertSame()메서드는 두 객체의 레퍼런스가 동일한가를 확인한다. (== 연산자)
9. assertNotSame(ox, oy) : ox와 oy가 같은 객체를 참조하고 있지 않으면 통과.
10. assertfail() : 테스트를 바로 실패처리