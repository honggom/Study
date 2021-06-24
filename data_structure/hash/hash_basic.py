hash_table = [0 for i in range(8)]
#[0, 0, 0, 0, 0, 0, 0, 0]

'''
1. 해쉬 함수 : key % 8
2. 해쉬 키 생성 : hash(data)
'''


def change_to_hash(data):
    return hash(data)


def hash_func(key):
    return key % 8


def save_data(key, value):
    hash_addr = hash_func(change_to_hash(key))
    print(hash_addr)
    hash_table[hash_addr] = value


def read_data(data):
    hash_addr = hash_func(change_to_hash(data))
    return hash_table[hash_addr]


save_data("dave", 2123132)
save_data("hong", 112312)
print(hash_table)
print(read_data("hong"))