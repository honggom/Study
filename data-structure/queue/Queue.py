'''
배열을 활용한 큐 구현
'''


class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data


qq = Queue()

qq.enqueue(1)
qq.enqueue(2)
qq.enqueue(3)

print(qq.dequeue())
print(qq.dequeue())
print(qq.dequeue())
