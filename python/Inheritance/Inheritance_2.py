class Father:
    def __init__(self):
        self.name = "bob"

    def my_name_is(self):
        print(self.name)


class Son(Father):
    def __init__(self):
        super().__init__()


s = Son()
s.my_name_is()

'''
오버라이딩 (Over riding):
상속관계에서 부모 클래스의 메서드를 자식 클래스에서 재정의 하는 것
'''
