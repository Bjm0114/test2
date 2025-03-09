print("Hello, World!") #"", '' 둘다 사용가능
#문자와 기호의 나열로 구성된 문장을 문자열이라고 한다.
a=3
print(a)

b=2*a
print(b)

print(a,b)

a빼기b = a-b
b곱하기a = b*a
print(a빼기b, b곱하기a)

print("a빼기b :", a빼기b)
print("b곱하기a :", b곱하기a)

#변수작성시에는 보다 관련성있게
A_score = 72
B_score = 80

#변수 작성 규칙
# ., !, +, -, *, /, %, @, ~ 를 사용할 수 없다. 추가로 공백 안되고 숫자로 시작하는것 안된다


# 3dogs = "강아지 3마리"
# print(3dogs) ----------------구문오류가 난다 이유는 변수명 첫번째 자리에 숫자가 들어갔기 때문이다

# first.second = "1, 2"  ---------------------- 마침표로 인한 구문오류 first가 지정되지 않음 

# big number = 10000000000000 -------------------------공백으로인한 구문오류 

v = 'v'
V = 'V'

print("소문자 v", v)
print("대문자 V", V) # 소문자 브이와 대문자브이는 엄연히 다른것

x=5
x=7
print(x) #변수재할당으로 인하여 7이 출력

x= x+1
print(x) #변수 업데이트

x= x-1
print(x)

x+=1 #x= x+1을 간단하게 나타낸것이다
print(x) 

x/=2
print(x)

#여기서부터는 사칙연산
a=7
b=3
c= b+4
print(a+b)

d= a+b
print(d)

e=b-a
print(e)

d= a*b
print(d)

e= b/a
print(e)

#거듭제곱
f=a**2 +1
print(f)

#나눗셈의 몫
f = 8//b + 3//2
print(f)

#정수 나눗셈의 나머지: %는 나머지 계산
g = c%b + f
print(g)

#몫 연산 vs 나눗셈 연산:정수 vs 부동소수점
print(c/b)

#나눗셈을 제외하고 정수를 이용한 다른 연산은 기본적으로 정수로 계산된다. 하지만 점(.)을 찍으면 유리수 , 즉 부동소수점으로
#취급된다. 따라서 모든 연산의 결과가 부동소수점으로 계산된다.
print(a + 3.)
print(a - 3.)
print(a * 3.)
print(a / 3.)

#단 정수를 가리키는 변수에 점을 찍는것은 허용되지 않는다.
# d=7
# a = d. 이런식으로 하면 syntax error 즉 구문 오류가 뜬다.








#여기서부터는 예제
# print("Hello World" -- >  괄호가 하나 빠짐 (닫는 괄호)
# print('Hello World") -- > 작은 따옴표로 열때는 작은 따옴표로 닫아야함

print(+2) #----> 오류가 발생하지 않음 +2는 그냥 2로 본다.

# print(023) --> 부동소수점이나 정수 등은 0으로 시작할 수 없다.
print('023') #--> 이와같이 ''를 이용하여 '023'을 나타낼 수 있다.

#예제 2 변수할당 명령문과 관련한 주의사항
#23 = n ----> 변수 할당 명령문의 등호 기호 왼쪽에 변수가 와야한다.

x=y=1
# ---> 오류발생하지 않음 하지만 줄바꿔쓰는거 추천

# y= k+1
# print(y) # 변수 k가 지정되지 않음

k=2
y= k+1
print(y) #이런식으로 해야 정상적으로 출력됨

#예제 3
number = 17
print(number + 2)
print(number - 2.0)
print(number / 7)
print(number //7)
print(number % 7)
print(number**3 / (2+3))
print(number**3 / 2+3)

#예제 4

print(3 + 3.0)
#print(3 + '3.0') --- > 따옴표 씌우면 오류발생
print(3 * '3.0')

#예제 5
#1m**2은 0.3025평이다. 84m**2은 몇평인가? 반대로 30평은 몇 m**2인지 계산하는 코드를 다양한 변수를 이용하여 구한다.

#one_squaremeter: 1제곱미터에 해당하는 평수
#eightyfour_squaremeter: 84제곱미터에 해당하는 평수
##one_pyeong: 1평에 해당하는 제곱미터
#thirty_pyeong: 30평에 해당하는 제곱미터

one_squaremeter = 0.3025
eightyfour_squaremeter =  84 * one_squaremeter
one_pyeong = 1 / one_squaremeter
thirty_pyeong = 30 * one_pyeong

print(eightyfour_squaremeter, "평")
print(thirty_pyeong, "제곱미터")
