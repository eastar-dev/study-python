import sys

string = "Hello, World"
print(string[-10000:-1])

print(type(string))
# string[2] = 's'

print(string[3:-1])

print('=' * 10)
print(10 * '=')

string2 = string.split()
print(string2)

print(list)
lst = [1, 2, 3, 4, 5, ]
print(lst)
print(len(lst))  # 마지막에 , 로 끝나도 갯수는 5개이다
a, b, c, d, e = lst  # 이거를 사용할때는 항목의 갯수만큼 변수를넣어야 한다.
a, b, c, d, e = lst  # 튜플 말고 리트트도 된다.
print(a, b, c)

print(len(lst))
# print(lst.index(4))
lst.append(9)
lst.extend([9, 7])
lst2 = lst + [9, 7]
print(lst)

tupl = 1,
print(type(tupl))

myTuple = 1, 2, 'number'
print(myTuple)

a, b, c = myTuple
print(a, b, c)
print(type(a), type(b), type(c))

myTuple = ('p', 'y', 's', 'o')
print(myTuple)

myTuple = ('p', 'y', 's', 'o')
myTuple = ('p', 'y', 's', 'o', 'o', 'o', 'o')
print('+' * 20)
print('+' * 20)
print('+' * 20)
print(myTuple[1:-2])
print(myTuple.index('p'))
print('p' in myTuple)
print('t' in myTuple)

print(myTuple * 2)

mySet = {1, 2, 3, 4}
print(mySet)

mySet.add(5)
print(mySet)

mySet.update([3, 7])
print(mySet)

print(mySet.pop())  # 팝하고 삭제
mySet.discard(2)  # 없어도 오류안남.
print(mySet)

# mySet.remove(2)  # 없으면 오류
mySet.clear()
print(mySet)

# print(list(string))


print('+' * 20)
print('set')
mySet1 = {1, 2, 3, 4}
mySet2 = {2, 3, 4, 5}
print(mySet1 - mySet2)
