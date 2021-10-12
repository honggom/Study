import sys

n, s = map(int, input().split())
nums = list(map(int, input().split()))

head, tail = 0, 0
_sum = 0
result = sys.maxsize

while True:
   if _sum >= s:
       result = min(result, tail - head)
       _sum -= nums[head]
       head += 1

   elif tail == n:
       break

   else:
       _sum += nums[tail]
       tail += 1

if result == sys.maxsize:
   print(0)
else:
   print(result)