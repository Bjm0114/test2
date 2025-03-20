# 6.1
'' # 빈 문자열
empty_str1 = '' #길이 0 단, ' '는 길이 1
empty_str2 = ""
empty_str3 = str()

#화이트 스페이스

#' ' 스페이스
#'\t ' 텝
# '\n' 줄바꿈
# \r 캐리지 리턴
# \v 또는 \x0b 수직탭
# \f 도는 \x0c 폼피드


print('1\n2\t3')
print(len('apple'))
print(len('Hello World'))

print(len('\n'))
print(len('\t'))
print(len('\r'))

print(len('\\'))

#6.4 이스케이프 시퀀스

fan_python = "I'am a fan of python"
print(fan_python)


me_too = '나도"그렇다"'
print(me_too)


#오류가 나온다.
# fan_python = 'I'am a fan of python'
# print(fan_python)

# me_too = "나도"그렇다""
# print(me_too)

#위와 같은 오류를 방지하는 방법이 없을 경우가 있다 (작은 따옴표와 큰따옴표가 동시에 사용되었을 경우)
# "I've also said "yes"!"

#이스케이프 활용
# \' #작은 따옴표 기호 자체
# \" #큰 따옴표 기호 자체
# \\ #원화 기호 자체
# \n #줄바꿈
# \t #탭추가

said_yes_1 = "I\'ve also said \"yes\"!"
print(said_yes_1)

said_yes_2 = 'I\'ve also said \"yes\"!'
print(said_yes_2)

#백슬래스 기호
using_backslash = "백슬래시 \\"
print(using_backslash)

#6.5 날 문자열

print(r"Hello\ world") # 특수문자에 대해 백슬래시 기호를 사용할지 여부를 고민하는 대신 날 문자열 (r) 사용
print(r"Hello\n World")
print(r"Hello\t World")
print(r"C:\some\name")

#6.6 포매팅

#f 문자열 
name = "강현"
age = 20

print(f"{name} 입니다 {age} 살입니다 안녕하세요 ")

print(f"{age+1} 입니다 ")

#문자열 좌우 정렬 출력
#왼쪽으로 출력
s1 = 'hi'
s2 = 'hello'
print(f"{s1:<10}")
print(f"{s2:<10}")

#오른쪽으로 정렬
print(f"{s1:>10}")
print(f"{s2:>10}")

#가운데 정렬
print(f"{s1:^10}")
print(f"{s2:^10}")

#남은 칸 기호로 채우기
print(f"{s1:+>10}")

#부동소수점 자릿수 지정
num1 = 17.153742
num2 = 2.778
print(f"소수점 둘째자리에서 반올림 {num1:.1f}")
print(F"소수점 둘째자리에서 반올림 {num2:.1f}")

print(f"실험테스트 : {num1:*>20.3f}")
print(f"실험테스트2 : {num2:%^20.2f}")

#예제 1
#아래 코드의 실행결과를 설명하라
print("\tHello World\n!")

#세종류의 화이트 스페이스 사용 (\t,\n, 공백)
#문자열이 먼저 탭으로 시작하고 이후에 Hello World를 출력한 다음 줄바꿈을 진행한다. 줄이 바뀐 후 느낌표 기호가 출력된다.

#예제 2
#아래 코드의 실행 결과를 설명 

print(len("Hello\tWorld\n!"))

#화이트 스페이들도 각각 문자의 길이는 1 , Hello World 단어에 포함된 알파벳 10개를 포함해서 총 13개의 문자로 구성된 문자열이다.

#예제 3
#아래 두 코드의 실행결과가 다른 이유

print('python\nis\easy\to\learn')

print(r'python\nis\easy\to\learn')

#첫번째는 날 문자열이 없기떄문에 백슬래시의 기능이 발휘된다(화이트 스페이스 기능), 하지만 날 문자열이 사용된
# 아래 코드는 백슬래시를 다 무시하고 그대로 출력한다.

#예제 4
#아래 두개의 부동소수점을 소수점 이하 두자리까지만 출력되도록 f 문자열을 사용하라
num = 23.36778
num2 = -84.99888

print(f"{num:.2f}")
print(f"{num2:.2f}")


#예제 5
#아래 두개의 부동소수점의 소수점을 버리고 정수부문만 출력되도록

num2 = 23.36778
num3 = -274.5789

print(f'{num2:.0f}')
print(f'{num3:.0f}')  #int 함수는 반올림을 고려하지 않는다
print(int(num3))

#예제 6
#아래 두개의 정수를 총 다섯 칸을 차지하도록 f-문자열을 활용하라. 단 모든 정수는 오른쪽으로 정렬되어야하며 앞쪽 빈칸은 0으로 채운다.
num4 = 23
num5 = 833

print(f'{num4:0>5}')
print(f'{num5:0>5}')


