"""
if 조건:
    조건이 참일 때 실행할 문장
else:
    조건이 거짓일 때 실행할 문장
"""
# 조건을 한번만 비교하면 되기 때문에 효율이 훨씬 좋습니다.\

#조건이 2가지 이상인 경우
#마지막 조건까지 사용하지 않아도 되서
#훨씬 용량이 절약된다.

# elif: 를 사용하면 됩니다.
"""
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))
elif 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))
elif 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
elif now.month == 12 or 1 < now.month <= 2 :
    print("이번 달은 {}월로 겨울입니다.".format(now.month))
"""
"""
credits_question = input("Please enter your credits >")
credits = float(credits_question)
print()
왜 안됐을까?
"""

credits = float(input("Please enter your credits >"))
if credits == 4.5:
    print("신")
elif 4.2 <= credits:
    print("교수님의 사랑")
elif 3.5 <= credits: 
    print("수호자")
elif 2.8 <= credits: 
    print("일반인")
elif 2.5 <= credits: 
    print("소시민")
elif 1.75 <= credits: 
    print("선구자")
elif 1.0 <= credits: 
    print("불가촉천민")
elif 0.5 <= credits: 
    print("자벌레")
elif 0 < credits: 
    print("플랑크톤")
elif 0 == credits: 
    print("혁명의 씨앗")

    # 마지막 부분에 else를 사용하려면 조건 없이
    #그냥 else: 이어야한다.

    