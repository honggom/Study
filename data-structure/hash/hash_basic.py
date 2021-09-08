hash_table = [0 for i in range(8)]
#[0, 0, 0, 0, 0, 0, 0, 0]

'''
1. 해쉬 함수 : key % 8
2. 해쉬 키 생성 : hash(data)
'''


def change_to_hash(key):
    return hash(key)


def hash_function(key):
    return key % 8


def save_data(key, value):
    hash_address = hash_function(change_to_hash(key))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(change_to_hash(data))
    return hash_table[hash_address]


save_data("dave", 2123132)
save_data("hong", 112312)
print(read_data("hong"))

# 결과
# >>> 112312

print(change_to_hash("abvasd"))