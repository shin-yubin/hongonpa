"""if <조건>:
    조건이 참일때 실행될 문장
    조건이 참일때 실행될 문장
    조건이 참일때 실행될 문장
    조건이 참일때 실행될 문장
    #백스페이스, shift+tab: 조건에서 빠져나올수 있음
    """
"""
if True:
    print("True 입니다.")
if False:
    print("False 입니다.")
"""
"""
number = input("정수입력")
number = int(number)

if number > 0:
    print("양수입니다")
if number == 0:
    print("0입니다")
if number < 0:
    print("음수입니다")
"""
import datetime
now = datetime.datetime.now()
if now.hour < 12 :
    print("현재 시간은 {}시 {}분으로 오전입니다.".format(now.hour,now.minute))
if now.hour > 12 :
    print("현재 시간은 {}시 {}분으로 오후입니다.".format(now.hour,now.minute))
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# 계절

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
if now.month == 12 or 1 < now.month <= 2 :
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

# 121p 인간의 조건과 컴퓨터의 조건
# 홀수와 짝수
"""
number = input("정수를 입력해주세요 >")

last_character = number[-1] #number 변수가 문자열이라서 마지막 문자를 선택하라는 뜻입니다.
last_character = int(last_character)
if last_character == 0 or last_character == 2 or last_character == 4 \
    or last_character == 6 or last_character == 8:
    print("짝수입니다.")
else: print("홀수입니다.")
"""

number = input("정수를 입력해주세요 >")
number = int(number)
if number % 2 == 0:
    print("짝수입니다.")
if number % 2 == 1:
    print("홀수입니다.")