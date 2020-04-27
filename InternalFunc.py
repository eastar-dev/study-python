# 내장함수

pos = 10
neg = -10

print(abs(pos))
print(abs(neg))

if neg > 0:
    print("neg > 0")
if abs(neg) > 0:
    print("abs(neg) > 0")

print(bool(''))  # False
print(bool(0))  # False
print(bool(()))  # False
print(bool({}))  # False

color = input('좋아 하는 색?')  # 좋아 하는 색?보라
if not bool(color):
    print('색을 입력하세요~')
else:
    print('좋아 하는색은 ' + color + "입니다.")  # 좋아 하는색은 보라입니다.


