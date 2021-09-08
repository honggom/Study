class max_heap:
    def __init__(self, data):
        self.heap_array = []
        self.heap_array.append(None) # 0번 인덱스는 편의를 위해 사용 안 함
        self.heap_array.append(data)

    def should_up(self, inserted_index):
        if inserted_index <= 1:
            return False

        parent_index = inserted_index // 2
        if self.heap_array[inserted_index] > self.heap_array[parent_index]:
            return True
        else:
            return False

    def insert(self, data):
        self.heap_array.append(data)

        inserted_index = len(self.heap_array) - 1

        while self.should_up(inserted_index):
            parent_index = inserted_index // 2
            self.heap_array[inserted_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[inserted_index]
            inserted_index = parent_index

    def should_down(self, popped_index):
        left_child_popped_index = popped_index * 2
        right_child_popped_index = popped_index * 2 + 1

        # Case 1. : 왼쪽 자식 노드도 없을 때
        if left_child_popped_index >= len(self.heap_array):
            return False

        # Case 2. : 오른쪽 자식 노드만 없을 때
        elif right_child_popped_index >= len(self.heap_array):
            if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                return True
            else:
                return False

        # Case 3. : 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_index] > self.heap_array[right_child_popped_index]:
                if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_index] < self.heap_array[right_child_popped_index]:
                    return True
                else:
                    return False

    def pop(self):
        returned_data = self.heap_array[1]

        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        popped_index = 1
        while self.should_down(popped_index):
            left_child_popped_index = popped_index * 2
            right_child_popped_index = popped_index * 2 + 1

            # Case 2. : 오른쪽 자식 노드만 없을 때
            if right_child_popped_index >= len(self.heap_array):
                if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                    self.heap_array[popped_index], self.heap_array[left_child_popped_index] = self.heap_array[left_child_popped_index], self.heap_array[popped_index]
                    popped_index = left_child_popped_index

            # Case 3. : 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_index] > self.heap_array[right_child_popped_index]:
                    if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                        self.heap_array[popped_index], self.heap_array[left_child_popped_index] = self.heap_array[left_child_popped_index], self.heap_array[popped_index]
                        popped_index = left_child_popped_index
                else:
                    if self.heap_array[popped_index] < self.heap_array[right_child_popped_index]:
                        self.heap_array[popped_index], self.heap_array[right_child_popped_index] = self.heap_array[right_child_popped_index], self.heap_array[popped_index]
                        popped_index = right_child_popped_index

        return returned_data


hp = max_heap(1)
hp.insert(2)
hp.insert(10)
hp.insert(100)

print(hp.pop())
print(hp.heap_array)
print(hp.pop())
print(hp.heap_array)
print(hp.pop())
print(hp.heap_array)
print(hp.pop())























