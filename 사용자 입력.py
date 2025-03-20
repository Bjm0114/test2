#사용자 입력

#5.1 input() 함수 

# x = 100
# y = 100

# print(x is y)

# x= 7

# print(x is y) #가리키고 있는 값이 다르기 때문에 False 출력

# print("숫자맞히기 게임입니다")

# secret = 13
# guess_str = int(input("10 부터 19숫자 중 고르시오 :")) #안내 문자열도 생략 가능하다

# if guess_str == secret:
#     print("맞았습니다")

# else:
#     print("틀렸습니다")

# a= input()
# print(a) ##-----------------------------------------------필요시 출석 제거


guess_str = '13'
print(type(guess_str))

# 5.2 숫자 입력값 처리

# print(13 == '13')#정수와 문자열 비교 시 무조건 False 출력
# secret = 13
# guess = int(guess_str)
# print(guess == secret)

# guess_str = input("10부터 19사이의 숫자 하나를 입력하세요 : ")
# guess = int(guess_str)
# print(guess)

# guess = int(input("10부터 19사이의 숫자를 입력하세요 : "))
# print(guess)

# print("숫자 맞히기 게임에 오신걸 환영합니다")

# secret = 13
# user = int(input("숫자를 입력하세요 : "))

# if user == secret:
#     print("정답입니다 !")
# else:
#     print("틀린답입니다")



# print("나눗셈 질문입니다")

# user = float(input("7나누기2? : ")) #int할시 부동소수점 표현이 불가하여 오류가 뜬다

# if user == 3.5:
#     print("정답")
# else:
#     print("오답")

# #5.3
# 예제 1

# a = int(input("입력하세요 1 : "))
# b = int(input("입력하세요 2 : "))
# print(a,"+",b,"=",a+b)

#예제 2

# a = float(input("입력하세요 1 : "))
# b = float(input("입력하세요 2 : "))
# print(a,"와",b,"의 평균값:",round((a+b)/2, 1))


#예제 3
# user_input = int(input("원하는 정수를 입력하세요: "))
# if user_input%2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# user_input = int(input("원하는 정수를 입력하세요: "))
# print("입력한값은 짝수입니다", user_input%2 == 0)

#예제 4

# user_input = int(input("입력 : "))

# if user_input > 17:
#     print("17보다 큰 값이네요", (user_input - 17)**2)
# else:
#     print(user_input,"은 17보다 작은 값이네요")

#예제 5

# user = input("중복할 숫자 입력")
# user2 = int(user*2)
# user3 = int(user*3)
# user = int(user)

# user4 = user + user2 + user3

# print(user,"+",user2,"+",user3, "=", user4 )

# n = input("정수 입력 : ")
# nn= n+n
# nnn=nn+n
# print(n+" + "+nn+" + "+nnn+" =",int(n)+int(nn)+int(nnn))

print(True + True)
print(True * 10)