#문제 1
# 코드를 작성한다.
# 오류원인 : 큰따옴표를 붙이지 않음
print("Hello World")

(2)
# 코드를 작성한다.
# 오류원인 : 쉼표가 있어야한다.
print(21,8)

(3)
# 코드를 작성한다.
# 오류원인 : +가 하나만 있어야한다.
print(2+2)

#문제2
# 코드를 작성한다.
# 오류원인 : 없음 , 주로 세미콜론은 한줄에 여러개의 python 명령어를 사용할 때 구분시 사용

(2)
# 코드를 작성한다.
#오류원인 : 공백으로 구분된 두 값은 연산자가 아니므로 잘못된 코드이다.(구문 오류)
x= 10
y= 2
z= x+y

(3)
# 코드를 작성한다.
# print에서 odd인데 oddd로 오타가 났다.
even = 3
odd = 17
print(even + odd)

# 코드를 작성한다.
# 어떤 수를 0으로 나누려고 하면 ZeroDivisionError라는 오류가 뜬다.
# 해결방법은 try - except문을 사용하면된다.

(4)
x = 3
zero = 0

try:
  result = x/zero
except ZeroDivisionError:
  print("0으로 나눌 수 없습니다.")

#또는 0으로 나누지 않도록 조건문을 추가하는 방법도 있다.
x = 3
zero = 0

if zero !=0:
  result = x/zero
else:
  print("0으로 나눌 수 없습니다.")

#문제3
(1)
# 코드를 작성한다.
print(13-19)
(2) 
# 코드를 작성한다.
print(81/3)
(3)
# 코드를 작성한다.
print(100%7)
(4)
# 코드를 작성한다.
print(7.2**3)

#문제4
(1)
# 코드를 작성한다.
width = 17
height = 12.0

print(width//2)

(2)
# 코드를 작성한다.
width = 17
height = 12.0

print(width/2)

(3)
# 코드를 작성한다.
width = 17
height = 12.0

print(width/2.0)

(4)
# 코드를 작성한다.
width = 17
height = 12.0

print(height/3)

(5)
# 코드를 작성한다.
width = 17
height = 12.0

print(2*5+1)

(6)
# 코드를 작성한다.
width = 17
height = 12.0

print(2*5+1.0)

#문제5
# 코드를 작성한다.
A = 60*360 + 60*52 #집을 떠난 시간
B = 60*8 + 15 # 1km
C = 60*21 + 36 #3km
D = 60*8 + 15  # 1km

E= A+B+C+D

F = E//3600
G = E % 3600 //60
H = E % 3600 % 60

print("집에 도착 시간:",F,"시", G,"분", H,"초")