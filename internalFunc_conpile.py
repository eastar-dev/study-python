# 내장함수

number = 0
exp = 'number + 1'
code1 = compile(exp, "<string>", "eval")
for h in range(100):
    number = eval(code1)
print('1', number)

number = 0
state1 = 'number = number + 1'
code2 = compile(state1, '<string>', "single")
for h in range(100):
    exec(code2)
print('2', number)

state2 = '''
number = 0
state1 = 'number = number + 1'
code2 = compile(state1, '<string>', "single") 
for h in range(100):
    exec(code2)
print('2', number)
'''

code3 = compile(state2, '<string>', "exec")  # single exec 에 차이가 있는건가? single은 한줄만을 강제한다
exec(code3)
