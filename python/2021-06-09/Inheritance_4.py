class Father:
    def say_hi(self):
        print("hi")


class Mother:
    def say_something(self):
        print("plz")


class Son(Father, Mother):
    def say_bye(self):
        print("bye")


s = Son()
s.say_bye()
s.say_hi()
s.say_something()

'''
결과 :
bye
hi
plz
'''


'''
다중 상속이 가능
'''
