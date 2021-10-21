# 빗물 트래핑 문제
# 왼쪽, 오른쪽 중 제일 큰 값에서 더 작은 값이 현재 블록보다 크다면 그 차이가 빗물이 쌓이는 양

class Solution:
    def trap(self, h):
        result = 0

        for i in range(1, len(h)):

            left = max(h[:i])
            right = max(h[i:])

            m = min(left, right)

            if m > h[i]:
                result += m - h[i]

        return result
