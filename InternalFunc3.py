# 내장함수에 들어 있는 값을 모두 알고 싶다.


print(dir())
internals = dir()
for internal in internals:
    exec("print(" + internal + ")")

# myList = []
# print(dir(myList))
# internals = dir(myList)
# for internal in internals:
#     print("print(myList." + internal + ")")
#     exec("print(myList." + internal + ")")
