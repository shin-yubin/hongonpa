#for '반복자' in '반복할수있는것':


#반복자는 리스트를 기준으로 <요소, 변수 이름>이 들어갑니다.
"""
a = [1, 2, 3, 4 ,5 ,6, 7]
for element in a:
    print(element)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for number in numbers:
    print("{}는 {}자리수 입니다".format(number,len(str(number))))    
"""
""" 
   if number >= 100:
        print("100 이상의 수: {}".format(number))
    if number % 2 == 0:
        print("{}는 짝수입니다.".format(number))
    else:
        print("{}는 홀수입니다.".format(number))
"""
#반복문 하나로 리스트 하나를 돌릴 수 있습니다.
# 그러므로 리스트를 뚫으려면 반복문 2개를 써야함    
list_of_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8],
]
for a in list_of_list:
    for b in a:
        print(b)