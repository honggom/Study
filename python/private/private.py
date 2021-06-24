class Person():

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def changeName(self, name):
        self.__name = name

    def printInfo(self):
        print(self.__name, self.__age)


p = Person("hong", 100)
p.name = "wrongName"
p.__age = 1
p.printInfo()

'''
클래스 작성시 
변수나 함수 앞에 '__' 언더스코어를 앞에 붙여서 네이밍 해주면
자바 private 효과를 가져옴
'''
