class Father:
    def say_hi(self):
        print("hi")


class Son(Father):
    def say_bye(self):
        print("bye")


s = Son()
s.say_bye()
s.say_hi()

'''
결과 :
bye
hi
'''


'''
Son 클래스 작성 시 Father을 상속받아 
say_hi를 사용한 코드
기본적으로 __init__ 은 생략해도 됨
'''
