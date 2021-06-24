"""
hash_basic 에서 간단히 만들어 본 hash_table 은
해쉬 충돌(해쉬 함수로 만든 key 값이 중복 되는 현상)에 무방비 상태
따라서 이것을 방지할 방법이 필요함

방법 2.
    hash linear probing : 해당 key에 대한 hash 값이 겹치면 빈 슬롯을 찾아 빈 슬롯에 데이터를
    저장하는 방식

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


save_data('da', 1234441)
save_data('db', 77565656)
save_data('dc', 33333336)
save_data('do', 4444456)
print(hash('da') % 8)
print(hash('db') % 8)
print(hash('dc') % 8)
print(hash('do') % 8)
print(hash_table)
print(read_data('db'))