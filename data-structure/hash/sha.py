'''
hash의 충돌 빈도가 높아지면
검색과 삽입 효율이 느려질 수밖에 없음
따라서 충돌 빈도를 줄이는게 보다 hash table을 효과적으로 만드는 키 포인트

방법
1. 저장 공간을 확대
2. 유일한 해쉬 키를 만드는 해쉬 함수를 사용하는 법
    : SHA(secure hash algorithm) 안전한 해시 알고리즘 사용
        - 어떤 데이터도 유일한 고정되 크기의 고정 값을 리턴해줌
        - 자세한 방법 아래 코드 #SHA 참고

'''

#SHA
import hashlib
data = 'junit'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
# hexdigest() : 16진수로 변환한 값 리턴
print(hex_dig)
# 16진수로 변환된 값을 역으로 해석하기는 매우 어려움
# 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 -> junit : 매우 어렵다..
