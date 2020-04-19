var = '전역변수'


def scope():
    global var
    var = 'global 명령어의 역할'
    print('함수 안 var: ', var)


scope()
print('함수 밖 var: ', var)
