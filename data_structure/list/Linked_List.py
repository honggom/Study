'''
연결 리스트 

    -장점 
        - 데이터를 동적으로 할당하기 때문에 공간을 미리 할당하지 않아도 됨

    -단점
        - 노드를 활용하고 노드가 포인터를 가지고 있기 때문에 불필요한 공간을 차지함
        - 노드를 다음으로 넘겨가며 데이터를 찾기 때문에 데이터 검색이 오래 걸림
'''


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    # '__'를 변수나 함수 앞에 붙여서 네이밍하면 private 효과
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, data):
        node = Node(data)
        if self.__head == None:
            self.__head = node
            self.__tail = node
        self.__tail.next = node
        self.__tail = node

    # 데이터 삭제
    # 단 데이터가 중복이여도 head에 가까운 값 하나만 지움
    def remove(self, data):
        if data == self.__head.data:
            tmp = self.__head
            self.__head = self.__head.next

            # 메모리 지우기
            del tmp
        else:
            node = self.__head
            while node.next != None:
                if data == node.next.data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                    return
                else:
                    node = node.next
            print("해당 값이 존재하지 않습니다.")

    def printAll(self):
        node = self.__head
        while node != None:
            print(node.data)
            node = node.next


l = LinkedList()

l.add(1)
l.add(2)  # 1
l.add(2)  # 2
l.add(3)
l.add(3)

l.printAll()
l.remove(2)
l.printAll()
l.remove(2)
l.printAll()
l.remove(4)
l.printAll()
