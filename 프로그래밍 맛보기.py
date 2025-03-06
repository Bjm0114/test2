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

f = 8//b + 3//2
print(f)