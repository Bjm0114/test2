#표현식과 자료형

# 17, 3.14, '안녕하세요' 등은 변수에 할당하거나 연산자 또는 함수의 인자로 활용가능
num = 17
num + 2
print(num)

#함수의 인자에서 활용
max_value = max(num+2, num//2)
print(max_value) #최댓값인 num+2를 출력

min_value = min(num*2, num/2)
print(min_value)

#이처럼 특정 값을 표현하는 식을 표현식이라고 한다.

#문자열 리스트 등도 값, 문자열 인덱싱과 리스트 인덱싱 등도 특정 값을 표현하는 표현식이다.

hello = "파이썬" + "안녕?"
print(hello)

languages = ["파이썬", "C", "자바", "Rust"]
print("파이썬" in languages)

python = (languages[0])
print("인기가 가장 높은 프로그램",python)

#주석

#speed는 시속을 가리키는 변수이다.

speed = 90 #속도 단위는 km이다.
print("스피드:", speed, "km")

#여러줄 주석

#speed는 시속을 가리키는 변수이다.
#테스트

speed = 90 #속도 단위는 km이다.
print("스피드:", speed, "km")

'''안녕하세요
여러줄 주석 테스트합니다'''
speed = 90 #속도 단위는 km이다.
print("스피드:", speed, "km")


#자료형
#값과 변수의 자료형
print(type(6)) #해당 자료가 어떤 형태인지 출력해준다
b=6
print(type(b)) #b에 할당된 값이 6이기에 b의 타입도 int로 판명된다.

b= "Hello, world!"

b= 'Hello, world!'

print(type(b)) #b에 할당된 값마다 다른점 유의


#표현식의 자료형
print(type(num+2))


print(type(max(num+2, num//2)))

print(type(min(num*2, num/2)))

print(type("파이썬" + "안녕?"))

print(type(["파이썬","자바"][0]))


#파이썬 기초 자료형

#정수형 int
a=4
print(type(a))

#부동소수점 float
c=2.1
print(type(c))

#문자열 str
like_python = "파이썬 좋아"
print(type(like_python))

#부울 bool
print(type(True))



#형변환
print(2.3 + float(3))
print(2.3 + 3)

print(int('5'))
#print(int('5.1')) # 정수 문자가 아님

print(int(4.8)) #부동소수점에서 정수로 형변환

print(int(True))
print(int(False))

#float 함수

print(float(7)) #정수를 부동소수점으로 표시
print(float(True))
print(float(False))

#str 함수
print(str(6))
print(str(False)) #임의의 값을 문자열로 변환한다.

#bool 함수
print(bool(0))
print(bool(2))
print(bool("Hello"))

#float은 부동소수점 또는 형변환을 가리킴 따라서 자료형과 형변환을 구분하기 위해서 str(), int() 처럼 괄호로 구분해야한다.

#예제 정수 두 개를 각각 입력받을 수 있도록 input() 함수를 두 번 사용한다. 
#첫째 입력값은 정수로 변환해서 a에 할당, 둘째 입력값은 b에 할당한다. 지정된 형식으로의 출력은 print() 함수를 이용한다.
#print() 함수에 쉼표를 이용하여 여러 개의 인자를 지정하면 각각의 인자가 공백으로 구분되어 한 줄에 출력되는 성질을 이용한다.

# a = input("입력하세요 1 : ") ------------------------------- 테스트 필요시 주석 제거
# b = input("입력하세요 2 : ")
# print(a, "+", b,"=", a+b)

#예제 3
#우유 가격은 820원이고, 아이스크림 가격은 1500원이다. 아이스크림은 3개 이상 구입하면 5% 할인해준다. 
# 우유 2개와 아이스크림 3개를 구입할 때 지불해야 하는 가격을 다양한 변수를 활용하여 계산하는 코드를 작성한다.

#힌트: 할인율이 5%이면 할인을 적용할 때 구입 가격에 (1 - 0.05)를 곱한다.

milk_price = 820
icecream_price = 1500
milk = 2
icecream = 3
discount = 0.05


if icecream >=3:
    total_price = (milk * milk_price + icecream * icecream_price*(1-discount))
else:
    total_price = (milk * milk_price + icecream * icecream_price)

print("우유", milk, "개", "아이스크림", icecream, "개", "총구입비용",int(total_price))


#예제 4
#두 개의 부동소수점x와 y를 입력받아 두 수의 평균값을 아래 형식으로 출력하는 코드를 작성하여라.
#2.4 와 5.7 의 평균값: 4.05
a = 2.4
b = 5.7

answer = (a+b)/2

print(a,"와",b,"의 평균값:", answer)

print(round(3.141592, 3))

#예제 +
#사용자가 정수가 아닌 유한소수를 입력할 것을 예상해야 하기에 input() 함수의 결과에 바로 float() 함수를 적용한다. 
#그 다음에 평균값을 계산하여 지정된 방식으로 출력한다. 단, round() 함수를 이용하여 소수점 이하의 자릿수를 2로 지정한다.

# x = float(input("입력하세요 1 : "))
# y = float(input("입력하세요 2 : ")) --------------------------------- 테스트 필요시 주석 제거

# answer = round((x+y)/2, 2)
# print(answer)   

#예제5
# user_input = int(input("입력하세요 : ")) -------------------------------------- 테스트 필요시 주석 제거
# print("입력값이 짝수인가요?",user_input%2 == 0)

#예제6 
#사용자로부터 하나의 정수를 입력받은 후 입력값이 17보다 크면 입력값과 17의 차이의 제곱을,
#  아니면 입력된 정수를 출력하는 코드를 작성한다.

# 힌트: input() 함수와 int() 함수 활용

# user = int(input("정수를 입력하세요 : ")) ------------------------------- 주석제거
# if user>17:
#     print((user-17)**2)
# else:
#     print(user)

#예제7
#사용자로부터 0이 아닌 한자리 정수 n 을 입력받아 n + nn + nnn 을 계산하는 코드를 작성한다. 
# 단, nn과 nnn은 곱셈이 아니고 문자열 n을 각각 두 번과 세 번 반복한 결과로 생성된 정수를 가리킨다. 
# 예를 들어 5가 입력되면 아래 값이 계산되어야 한다.

# 5 + 55 + 555 = 615
# 힌트: input() 함수와 int() 함수 활용. 문자열 이어붙이기 연산자 + 또는 복제 후 이어붙이기 연산자 * 활용.

# 주의사항: int(input()) 형식은 사용하지 않음.

# user = input("입력하세요 : ")-------------------------------------------주석제거

# test = int(user)
# test2 = int(user*2)
# test3 = int(user*3)

# print(test ,"+",test2, "+",test3, "=",test + test2 + test3)

# #또다른 방법
# n = input("정수를 입력하세요 : ") ------------------------------------------------주석제거
# nn = n+n
# nnn = nn+n

# print(int(n) + int(nn) + int(nnn))

# 예제 8
# 다음 모양을 출력하는 코드를 작성한다. 두 개의 별 기호 사이에 공백(space)이 사용됨에 주의한다. 
# 공백도 하나의 기호로 취급된다. 단, print() 함수와 while 반복문은 한 번씩만 활용한다.

shape = 0
while shape < 10:
    if shape < 5:
        stars = 5-shape
    else:
        stars = shape - 4
    print("*" * stars)
    shape+=1

#예제 4

even_num = 666

print(even_num%2==0)

print(type(even_num))

print(type(even_num%2 == 0))
print(even_num % 2==0 and even_num%3==0)