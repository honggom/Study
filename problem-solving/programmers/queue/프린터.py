def solution(priorities, location):
  answer = 0
  from collections import deque

  q = deque([(v, i) for i, v in enumerate(priorities)])

  while q:
      item = q.popleft()
      if q and max(q)[0] > item[0]:
          q.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer
