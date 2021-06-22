#1. sorted()
l = [2, 5, 1, 7, 9]
print(sorted(l))
#[1, 2, 5, 7, 9]
print(l)
#[2, 5, 1, 7, 9]

#2. sorted(), key
chars = ['aaa', 'bb', 'c']
print(sorted(chars, key=len))

#3. sotred(), function
def fn(s):
    return s[0], s[-1]

chars2 = ['cde', 'cfc', 'abc']
print(sorted(chars2, key=fn))

#4. sotred(), lambda
chars2 = ['cde', 'cfc', 'abc']
print(sorted(chars2, key=lambda s: (s[0], s[-1])))
#['abc', 'cfc', 'cde']


#5. sort()
l2 = [2, 5, 1, 7, 9]
print(l2.sort())
#None
print(l2)
#[1, 2, 5, 7, 9]

