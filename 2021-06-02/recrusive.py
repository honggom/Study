# 재귀 함수
def re(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        re(data-1)
        print("returned", data)


re(4)

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
