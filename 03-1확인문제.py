x = 2
if x > 4:
    print("X참")

y = 1
if y > 4:
    print("y참")

z = 10
if z > 4:
    print("z참")

# 연산자 적용 이후에 대상이 많아졌다 >> or
# 대상이 적어졌다 >> and

a = int(input("> 1번째 숫자:"))
b = int(input("> 2번째 숫자:"))
print()
if a > b:
    print("처음 입력한 {}가 {}보다 큽니다.".format(a,b))
if a < b:
    print("두번째 입력한 {}가 {}보다 큽니다.".format(b,a))