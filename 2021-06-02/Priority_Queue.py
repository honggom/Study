'''
우선순위 큐
    - 데이터 삽입 순서와 별개로 우선 순위에 따라 데이터가 출력됨

'''

import queue
q = queue.PriorityQueue()

q.put((1, "1등"))
q.put((3, "3등"))
q.put((2, "2등"))

print(q.get())
print(q.get())
print(q.get())
