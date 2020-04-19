import sys

iNumber = int("7")
print(type(iNumber), iNumber)

iNumber = int("+7")
print(type(iNumber), iNumber)

fNumber = float("7")
print(type(fNumber), fNumber)

sNumber = str(fNumber)
print(type(sNumber), sNumber)

print('Platform: {0.platform}\nPython version: {0.version}'.format(sys))

# print('{},{},{3}'.format('하나', '둘', '셋')) #중간에 비어도 안됨
print('{},{},{}'.format('하나', '둘', '셋'))  # 비어 있을려면 모두 비어 있어야만 가능합니다.

# weight = int(input('체중?'))
# height = float(input('키?'))
weight = 60
height = 1.8
bmi = weight / (height * height)
comment = "BMI는 {0}/({1}*{1}) 이므로 {2:} 이다"
# comment = "BMI는 {0}/({1}*{1}) 이므로 {2:} 이다" #오류안남 51851851851852
# comment = "BMI는 {0}/({1}*{1}) 이므로 {2:f} 이다" #결과다름 6자리
# comment = "BMI는 {0}/({1}*{1}) 이므로 {2:9f} 이다" #.까지 포함해서 9자리 차지
# comment = "BMI는 {0}/({1}*{1}) 이므로 {2:6.f} 이다" #오류
# comment = "BMI는 {0}/({1}*{1}) 이므로 {2:.2f} 이다" #오류안남
print(comment.format(weight, height, bmi))
