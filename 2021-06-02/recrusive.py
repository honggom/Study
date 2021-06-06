# 재귀 함수
def recrusive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recrusive(data-1)
        print("returned", data)


recrusive(4)

'''
결과 : 
4
3
2
1
0
ended     
returned 0
returned 1
returned 2
returned 3
returned 4
'''
