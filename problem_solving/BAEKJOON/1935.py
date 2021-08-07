n = int(input())
question = input()
nums = {}
stack = []
cal = ["+", "-", "*", "/"]

for unicode_num in range(65, 65+n):
    nums[chr(unicode_num)] = int(input())

for q in question:
    if q in cal:
        num1, num2 = stack.pop(), stack.pop()
        if q == "+":
            stack.append(num1 + num2)
        elif q == "-":
            stack.append(num2 - num1)
        elif q == "*":
            stack.append(num1 * num2)
        elif q == "/":
            stack.append(num2 / num1)
    else:
        stack.append(nums[q])

print('%.2f' % stack.pop())

