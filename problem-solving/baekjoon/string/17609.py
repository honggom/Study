# 실버 1
# 17609. 회문

import sys
input = sys.stdin.readline

def first_check(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            result_1 = second_check(word, left + 1, right)
            result_2 = second_check(word, left, right - 1)

            if result_1 or result_2:
                return 1
            else:
                return 2
    return 0

def second_check(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

for _ in range(int(input())):
    s = input().rstrip()
    print(first_check(s, 0, len(s) - 1))