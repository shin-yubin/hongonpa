리스트 = []
리스트 = [1, 2, 3, 4, 5]
리스트 = [
    1,
    2,
    3
]

#딕셔너리 선언
딕셔너리 = {
    "문자열": "값a",
    273: [1, 2, 3, 4],
    True: False 
}

print(딕셔너리["문자열"])
print(딕셔너리[273])
print(딕셔너리[True])

딕셔너리["문자열"] = "값값"
#문자열의 내용을 바꾸는것
print(딕셔너리["문자열"])

#반복문
for key in 딕셔너리:
    key
    딕셔너리[key]
    print("{} : {}".format(key,딕셔너리[key]))
    
#딕셔너리의 값을 추가, 제거
딕셔너리["키"] = "값"
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))
    
del 딕셔너리["키"]
print()
for key in 딕셔너리:
    print("{} : {}".format(key, 딕셔너리[key]))
    
    
"""for ~ in 에서는 iteration은 in 뒤에 있는 범위의 것으로 
자동적으로 결정 되는 것이군요.  "key" 라는게 딕셔너리 안에 
있는 키가 아닌데 왜 되는건지 라고 생각했었습니다. 
다음 강의의 pet pets 에서도 pet이라는게 대체 어디서 
나온것인가 했는데 이제 이해가 된거 같습니다"""