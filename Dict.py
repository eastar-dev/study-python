import sys

myDict = {}
print(myDict)

myDict = {1: '수소', 2: '핼륨', 2: '리튬', 3: '리튬'}
print(myDict)

myDict = dict([(1, '수소'), (2, '핼륨'), (2, '리튬'), (3, '리튬')])
print(myDict)
print(type(myDict))

print(myDict.get(4))  # 없어도 에러안남 None 리턴
#print(myDict[4])  # 없으면 애러남

print(myDict.pop(4, 6))  # 4해당 값을 가져오고 없으면 6을 리턴
print(myDict)

print(myDict.pop(1, 6))  # 4해당 값을 가져오고 없으면 6을 리턴
print(myDict)

del myDict[2]
print(myDict)

del myDict
# print(myDict)  # 자체가 삭제됨 오류남


myDict = {1: '수소', 2: '핼륨', 2: '리튬', 3: '리튬'}
myDict.clear()
print(myDict)

myDict = {1: '수소', 2: '핼륨', 2: '리튬', 3: '리튬'}
print(myDict.items())

myDict = {1: '수소', 2: '핼륨', 2: '리튬', 3: '리튬'}
print(myDict.keys())

myDict = {1: '수소', 2: '핼륨', 2: '리튬', 3: '리튬'}
print(myDict.values())
#print(myDict.values()[1:3]) # 안된다

# myDict1 = myDict.values()[0]  # 안된다.
# print(myDict1)

print(list(myDict.values())[0])
