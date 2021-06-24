# Spring REST Controller

## GET 
- @PathVariable 활용 
    - 요청 : http://localhost:8080/api/get/path-var/hong
    - 결과 : hong
    - 내용 : header에 'hong' 요청 및 반환
    - 코드 :   
        ```java
        @GetMapping("/path-var/{name}")
        public String pathVar(@PathVariable String name){
            return name;
        }
        ```
      <br>
- @RequestParam 활용 (1/2)
    - 요청 : http://localhost:8080/api/get/query-param?name=hong&age=10&email=dev
    - 결과 :
      ```
      name = hong      
      age = 10   
      email = dev
      ```
    - 내용 : 컨트롤러에 파라미터로 Map과 @RequestParam을 명시하여 header의 요청을 받음
    - 코드 :   
        ```java
        @GetMapping("/query-param")
        public String queryParam(@RequestParam Map<String, String> queryParam){
    
            StringBuilder sb = new StringBuilder();
    
            queryParam.entrySet().forEach(entry -> {
                sb.append(entry.getKey()+" = "+ entry.getValue()+"\n");
            });
            return sb.toString();
        }
        ```
      <br>
- @RequestParam 활용 (2/2)      
    - 요청 : http://localhost:8080/api/get/query-param02?name=hong&age=10&email=dev
    - 결과 : hong dev 10
    - 내용 : @RequestParam 명시적으로 활용
    - 코드 :
        ```java
        @GetMapping("/query-param02")
        public String queryParam02(@RequestParam String name, 
                                   @RequestParam String email, 
                                   @RequestParam int age){
            return name+" "+email+" "+age;
        }
        ```
      <br>
- DTO 활용
    - 요청 : http://localhost:8080/api/get/query-param03?name=hong&price=1000&etc=saa
    - 결과 : Product{name='hong', price=1000, etc='saa'}
    - 내용 : dto 활용 get 요청이기 때문에 header에 내용이 포함되어 있음, 고로 @RequestBody는 사용안함
    - 코드 : 
        ```java
        @GetMapping("/query-param03")
        public String queryParam03(Product product){
            return product.toString();
        }
        ```
    
- Product 클래스
    ```java
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
## POST
- @RequestBody 활용
    - 요청 : http://localhost:8080/api/post/test
      - body : 
        ```
        {
            "name" : "stv",
            "price" : 100,
            "etc " : "s"
        }
        ```
    - 결과 : 
        ```
        key : name
        value : stv
        key : price
        value : 100
        key : etc
        value : s
        ```
    - 내용 : post 요청에 parameter는 body에 메세지와 같이 요청하기 때문에 @RequestBody 활용
    - 코드 : 
        ```java
        @PostMapping("/test")
        public void post(@RequestBody Map<String ,Object> param) {
            param.forEach((key, value) -> {
                System.out.println("key : "+key);
                System.out.println("value : "+value);
            });
        }
        ```
    
- dto 활용
    - 요청 : http://localhost:8080/api/post/dto
      - body : 
        ```
        {
            "name" : "stv",
            "price" : 100,
            "etc " : "s"
        }
        ```
    - 결과 : Product{name='stv', price=100, etc='s'}
    - 내용 : post 요청 dto도 마찬가지로 @RequestBody 활용
    - 코드 :
        ```java
        @PostMapping("/dto")
        public void dto(@RequestBody Product product){
            System.out.println(product.toString());
        }
       ```
    