"""
강의 너무 재밌게 잘듣고 있어요! 
수업때문에 새벽에 일어나져요! 질문이 있어요.
"{}".format(52)  
그리고 .upper 코드에서 .의 앞을 뭐라고 하나요?  
print()의 함수의 괄호 안에 들어가는 자료가 
매개변수라고 하는 것처럼 이것을 부르는 용어가 
궁금합니다.
윤인성
4개월 전
영어로 표현하면 dot이고
한국어로는 그냥 "점"이라고 부릅니다 'ㅁ'
영어의 소유격을 나타내는 's와 비슷한 것이라고 
보면 좋은데요.
『문자열's format → 문자열이 가진 format, 
문자열의 format』
이라고 생각해주시면 됩니다!
"""

# .format() 함수

a = '{}{}{}'.format(1,2,3,4,"안녕")
print(a)

"""
중괄호의 갯수가 뒤의 
매개변수보다 많다면 에러 발생
 "주어".동사(목적어)
"""

# .upper()
# .lower()

a = "hello"
a.upper()

b = "hello"
b .lower()

#.strip()
"  뀨   ".strip()
#.lstrip() , .rstrip()

# .find()
# .rfind() 같은 문자가 주어에 있더라도 
#  오른쪽부터 우선해서 찾아줍니다.
#  문자열의 몇번째에 있는지 찾아줍니다.

"가나다라마바사".find("라")

# .find() 와 비슷한 연산자 in !
"가" in "가나다라마"
#true
"가나다라마" in "가"
#false

#.split("") 자른당!
#아래 예시는 띄어쓰기로 잘라서 리스트로 만들어줍니다.

"10 20 30 40 50".split(" ")

a = input(">first number: ")
b = input(">second number: ")
print()
print("{}+{}={}".format(a,b,int(a)+int(b))