# 정규표현식의 .(dot) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치된다는 것을 의미한다.
#(정규식 작성할 때 re.DOTALL 옵션을 주면 .(dot)문자와 \n 문자도 매치된다.)


# 8-2 정규표현식 시작

# [abc]
# [] 사이에 있는 문자와 매치
# "before" 는 "b" 가 있으므로 매치
# From - to 사용 가능 
# [a-c] , [1-10]


# Dot(.)
#[a.b]
# 줄바꿈을 제외한 모든 문자와 매치
# "aab" 는 가운데 "a"가 모든 문자 .과 매치
# "abc" 는 a와 b 가운데 아무것도 존재 X -> 따라서 매치 불가능

#반복 (*)
#[ca*t]
#"ct" a가 0번 반복되어 매치
#"cat" a가 0번 이상 반복되어 1번 반복으로 매치

#반복 (+)
#[ca+t]
#"ct"는 a가 0번 반복되어 매치 불가
#"cat"는 a가 1번 이상 반복되어 1번 반복으로 매치

#반복{m(최소), n(최대)},? ?:0번 또는 1번반복
#[ca{2}t]
#"caat" a가 2번 반복되어 매치

#[ca{2,5}t]
#"caaaaat"는 5번 반복되어 매치  

#[ab?c]
#"abc" 매치
#"ac" 매치


# 파이썬에서 정규 표현식을 지원하는 re 모듈
import re
p = re.compile("ab*")

#컴파일된 패턴 객체는 4가지 메서드 사용 가능
# 1. match()
# 2. serch()
# 3. findall()
# 4. finditer()

import re
p = re.compile('[a-z]*')
m = p.match("python")
print(m)

import re
p = re.compile('ca*t')
m = p.search("3 cat")
print(m)