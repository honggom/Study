# Controller로 Response 조작하기

- 요청 URI : http://localhost:8080/response/put
- 요청 Method : PUT
- 요청 Body (JSON) :
  ```
        {
            "name" : "hong",
            "price" : 100,
            "etc" : "hi"
        }
  ```
- 결과 
    - Status 201
    - Body :
    ```
        {
            "name" : "hong",
            "price" : 100,
            "etc" : "hi"
        }
    ```
- 컨트롤러 
```java
@RestController
@RequestMapping("/response")
public class ResponseController {

    @PutMapping("/put")
    public ResponseEntity<Product> res(@RequestBody Product product){
        return ResponseEntity.status(HttpStatus.CREATED).body(product);
    }
}
```
- Dto
```java
package com.example.demo.dto;

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

---
# @ResponseBody
- 일반 HTML Response Controller
```java
    @RequestMapping("/main")
    public String main(){
        return "main.html";
    }
```

- JSON Response Controlleer
```java
    @ResponseBody
    @GetMapping("/product")
    public Product product(){
        Product product = new Product();
        product.setName("hong");
        product.setPrice(100);
        product.setEtc("hi");
        return product;
    }
```
