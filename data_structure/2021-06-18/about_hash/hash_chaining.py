"""
hash_basic 에서 간단히 만들어 본 hash_table 은
해쉬 충돌(해쉬 함수로 만든 key 값이 중복 되는 현상)에 무방비 상태
따라서 이것을 방지할 방법이 필요함

방법 1.
    hash chaining : 슬롯의 데이터 공간을 유동적으로 확보
        데이터가 없을시 공간이 0의 데이터를 가지고 있지만 같은 key로 중복 시
        해당 key의 데이터의 공간을 링크드 리스트로 확장 각 리스트의 인덱스 마다 [key, value] 형태의 데이터가
        삽입됨 따라서 해당 hash 값마다 데이터가 중복시 list in list 형태로 데이터가 저장됨

"""
hash_table = [0 for i in range(8)]


def change_to_hash(data):
    return hash(data)


def hash_func(key):
    return key % 8


def save_data(key, value):
    index_key = change_to_hash(key)
    hash_addr = hash_func(index_key)

    #0이 아니라면 데이터가 존재 한다는 뜻
    if hash_table[hash_addr] != 0:
        for index in range(len(hash_table[hash_addr])):
            if hash_table[hash_addr][index][0] == index_key:
                hash_table[hash_addr][index][1] = value
                return
        hash_table[hash_addr].append([index_key, value])
    else:
        hash_table[hash_addr] = [[index_key, value]]


def read_data(key):
    index_key = change_to_hash(key)
    hash_addr = hash_func(index_key)
    if hash_table[hash_addr] != 0:
        for index in range(len(hash_table[hash_addr])):
            if hash_table[hash_addr][index][0] == index_key:
                return hash_table[hash_addr][index][1]
        return None
    else:
        return None


save_data('Dd', '4132312')
save_data('Data', '1231233')
print(hash_table)
print(read_data('Dd'))
