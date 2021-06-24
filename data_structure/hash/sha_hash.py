'''
sha 적용한 hash_table
'''

import hashlib

hash_table = [0 for i in range(8)]


def change_to_hash(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()

    #16 진수를 정수로 바꾸는 방법
    return int(hex_dig, 16)

def hash_func(key):
    return key % 8


def save_data(key, value):
    index_key = change_to_hash(key)
    hash_addr = hash_func(index_key)

    #0이 아니라면 데이터가 존재 한다는 뜻
    if hash_table[hash_addr] != 0:
        for index in range(hash_addr, len(hash_table)):
            if hash_table[index] == None:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value
                return
    else:
        hash_table[hash_addr] = [index_key, value]


def read_data(key):
    index_key = change_to_hash(key)
    hash_addr = hash_func(index_key)

    if hash_table[hash_addr] != 0:
        for index in range(hash_addr, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


'''
시간 복잡도 

삽입
    1. 일반적인 경우 (충돌이 없는 경우) : O(1)
    2. 최악의 경우 (충돌이 모드 발생하는 경우) : O(n)
        - 해쉬 테이블의 경우 일반적인 경우를 기대하고 만들기 때문에, 시간 복잡도는 O(1)이라고 말할 수 있다.
        
검색 
    배열은 O(n)
    해쉬는 O(1)

'''