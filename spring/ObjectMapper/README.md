# Object Mapper 
    Object를 Text형식 Json으로 변환,
    Text형식의 Json을 Object로 변환.
    - 주의 : 
        1. Object의 get 메서드를 참조하므로 get 메서드를 작성해놔야 됨.
        2. Text -> Object의 경우에 디폴트 생성자가 필요함.
- Object -> Text
    - 결과 : {"name":"hong","price":1000,"etc":"hi"}
```java
// Object -> Text
String text = om.writeValueAsString(product);
System.out.println(text);
```

- Text -> Object
    - 결과 : Product{name='hong', price=1000, etc='hi'}
```java
// Text -> Object
Product product2 = om.readValue(text, Product.class);
System.out.println(product2.toString());
```
- 전체 코드
```java
@Test
void contextLoads() throws JsonProcessingException {
	System.out.println("-----TEST-----");

	ObjectMapper om = new ObjectMapper();

	Product product = new Product();

	product.setName("hong");
	product.setPrice(1000);
	product.setEtc("hi");

	// Object -> Text
	String text = om.writeValueAsString(product);
	System.out.println(text);

	// Text -> Object
	Product product2 = om.readValue(text, Product.class);
	System.out.println(product2.toString());
}
---------------------------------------------------
public class Product {

    private String name;
    private int price;
    private String etc;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getEtc() {
        return etc;
    }

    public void setEtc(String etc) {
        this.etc = etc;
    }

    @Override
    public String toString() {
        return "Product{" +
                "name='" + name + '\'' +
                ", price=" + price +
                ", etc='" + etc + '\'' +
                '}';
    }
}
```