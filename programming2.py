#값과 변수
#추가사항 : in 연산자와 인덱싱관련 예제와 연습문제 추가 필요

#값은 컴퓨터에 저장해서 활용할 수 있는 대상이다. 정수, 부동소수점, 문자열 이 대표적인 값
#부동소수점 : 유한소수의 자료형
#문자열 : 임의의 문자, 숫자, 기호 등등
#부울값 : True , False

#리스트 : 여러개의 값을 항목으로 갖는 목록
one2five = [1,2,3,4,5]
name_list =  ['김강현', '황현', '남세원']
# 리스트는 서로 다른 종류의 값이 사용될 수도 있다.
kgh = ['김강현', '010-1234-5678', 20, 172.8, '제주']

#조건문

love_python = True
if love_python:
    print("안녕")
    print("파이썬 좋아요")
#콜론기호 사용되고 이후 두 명령문은 들여쓰기 이후에 작성되었음에 주의한다.

love_python = False
if love_python:
    print("안녕")
    print("파이썬 좋아요")
else:
    print("파이썬을 사랑해주세요!")
    print("행복해집니다")

#연산자와 값
#연산자 : 사칙연산에 사용되는 기호
#등식 부등식 처럼 부울값으로 계산되는 수식을 '논리식'이라고 부른다.

print(3 > 4)
print(3>=4-1)
print(5/3 +1.2 < 3/2)
print(2.3<= 2.3 +3.0)
print(1==4.0/4)
print(1!=2)

# = : 변수 할당에 사용
# == : 두개의 값이 동일한지

#리스트 연산
first_languages = ['파이썬', 'C', '자바']
Second_languages = ['C++', 'C#', '자바스크립트', 'Node.js']

languages = first_languages + Second_languages
print(languages)

# *를 리스에 사용하면 복제의 의미로 받아들임
print(languages*2)

#문자열 연산
first = '파이썬, '
second = '안녕!'

greetings  = first + second
print(greetings)
print(greetings*2)

#리스트 in 연산자
print('파이썬' in first_languages)
print('자바' in Second_languages)

#문자열 in 연산자
print('!' in greetings)
print('?' in greetings)
print('파이썬 안녕' in greetings)

#리스트 인덱싱
#리스트에 포함되는 각 항목은 인덱스를 가진다 차례대로 0,1,2,3,4 .....
print(name_list[0])
print(name_list[2])
print(name_list[-1])

scores = [92, 87, 100]
mean = (scores[0] + scores[1] + scores[2])/3
print(mean)
#참고로 정수의 나눗셈은 항상 부동소수점으로 처리된다는 점

#문자열 인덱싱
kgh = name_list[0]
print(kgh)
print(kgh[0])
print(kgh[2])

#연산자 우선순위
print(2*(3-1)) 
print((1+1)**(5-2)) #괄호안에 있는게 우선

#거듭제곱이 사칙연산보다 우선순위가 높다 
print(3**2*2)
print(3*2**2)

#곱셈과 나눗셈은 동등한위치기에 먼저쓴거 기준
print(60/2*3)
print(60 / (2*3))

#거듭제곱이 연속해서 나오면 오른쪽 거듭제곱부터 실행된다.
print(2**3**2)
print((2**3)**2)

#연산 결과값
onePtwo = 1+2
whether_even = onePtwo % 2 ==0
if whether_even:
    print("짝수")
else:
    print("홀수")

twoPtwo = 2+2
whether_even = twoPtwo % 2 ==0
if whether_even:
    print("짝수")
else:
    print("홀수")



#예제

#파이썬에서 0은 False로, 다른값은 True로 출력된다. 27.1은 부동소수점이면서 0이 아니기에 True로 인식되어 프린트 값이 출력된다.
if 27.1:
    print("참인 경우라서 출력됨")

#예제2
p1 = 3!=4
print(p1)

#예제3
p2 = "hello" == "hi"
print(p2)

#예제4
print("15는 짝수인가요?", 15%2==0)
print("28은 짝수인가요?", 28%2==0)
#다른방법
even15 = 15%2 == 0
even28 = 28%2 == 0
print("15는 짝수인가요?", even15)
print("28은 짝수인가요?", even28)

#예제5
#우유가격은 820원, 아이스크림 가격 1500원. 아이스크림은 3개 이상 구입하면 5% 할인해준다. 우유2개와 아이스크림 3개를
#구입할때 지불해야하는 가격을 다양한 변수를 사용하여 계산하는 코드 작성

milk_price = 820
ice_price = 1500
discount = 0.05 #아이스크림 3개 이상 구매시 할인율

milk = 2
ice = 3
if ice < 3:
    total_price = milk_price * milk + ice_price * ice  #할인없음
else:
    total_price = milk_price * milk + ice_price * ice * (1-discount) #할인적용

print("우유", milk, "개", "아이스크림",ice,"개", "가격:", int(total_price), "원" )


#예제6
#연이자 5%인 정기예금에 1천만원을 10년간 은행에 맡겼을 때 10년 후에 수령할 금액을 계산하는 코드를 다양한 변수를 활용하여 
#구현한다. 단, 다음 형식으로 출력하라

#10년 후 받을 원금 + 이자는 000 원입니다.
#원리합계 = 원금*(1+연금리*기간)

principal = 10000000
rate = 0.05
period = 10

savings = principal*(1+rate*period)

print("10년 후 받는 원금 + 이자는", savings, "원입니다")