from sys import stdin

for _ in range(int(stdin.readline())):
     parenthesis = stdin.readline().rstrip()
     lefts = []
     isRight = True
     for p in parenthesis:
          if p == '(':
               lefts.append(p)
          else:
               if len(lefts) == 0 or lefts.pop() != "(":
                    isRight = False
                    break
     if isRight and len(lefts) == 0:
          print("YES")
     else:
          print("NO")
