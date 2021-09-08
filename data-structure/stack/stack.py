'''
Stack

    작동 방식
    - LIFO -> Last In First Out 방식으로 작동

    함수
    - push() : 데이터 삽입
    - pop() : 데이터 출력
'''


class Stack():

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data


stc = Stack()

stc.push(1)
stc.push(3)
stc.push(123)

print(stc.pop())
print(stc.pop())
print(stc.pop())
