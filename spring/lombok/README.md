## 롬복
- @Data : @Getter, @Setter, @ToString, @EqualsAndHashCode, @RequiredArgsConstructor를 한 번에 생성
- @Getter : getter를 자동으로 생성
- @Setter : setter를 자동으로 생성
- @ToString : 필드를 기반으로 toString() 메서드를 자동 생성
- @NoArgsConstructor : 파라미터가 없는 기본 생성자를 생성
- @AllArgsConstructor : 모든 필드를 파라미터로 받는 생성자를 생성
- @RequiredArgsConstructor : final 또는 @NonNull인 필드에 대한 생성자를 생성
- @NonNull : 해당 변수가 null이면 널포인터 예외를 일으킴