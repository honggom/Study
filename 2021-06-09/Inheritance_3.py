class Father:
    def __init__(self):
        self.name = "bob"

    def my_name_is(self):
        print(self.name)


class Son(Father):
    def __init__(self):
        super().__init__()

    def my_name_is(self, name):
        print(name)


s = Son()
s.my_name_is("hong")

'''
결과 :
hong
'''

'''
오버라이딩 (Over riding):
상속관계에서 부모 클래스의 메서드를 자식 클래스에서 재정의 하는 것
여기서는 Son이 Father의 my_name_is 함수를 상속 받아 재정의 해서 사용
재정의 하지 않으면 Father의 이름인 bob가 그대로 출력
'''
