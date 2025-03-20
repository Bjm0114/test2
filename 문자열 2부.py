#문자열은 포함된 문자와 기호의 순서를 중요하게 여기는 순차 자료형이다. 따라서 문자열의 항목으로
#포함된 문자와 기호의 순서가 다르거나 사용된 문자열의 길이가 다르면 서로 다른 문자열로 인식
print('ab' == 'ba')
print('aaa' == 'aa')
print('python' == 'Python')

#7.1 문자열 인덱싱
colors = 'red, blue, yellow'
print(colors[0]) #문자열 왼편부터 0번째
print(colors[3])

print(colors[-1]) #오른쪽부터 지정

print(len(colors)) # 길이가 17이므로 0부터 16 또는 -1부터 -17까지의 정수를 인덱스로 사용할 수 있다.

# print(colors[50]) #오류가 난다 (인덱스 범위를 벗어났기 때문이다)

#7.2 문자열 슬라이싱

#문자열[시작인덱스:끝인덱스:보폭] #끝인덱스 : 끝인덱스 이전까지의 문자 확인
colors = 'red, blue, yellow'
print(colors[0:3]) #보폭 1로 설정해도 똑같은 출력값 나온다

print(colors[5:len(colors):2])
print(colors[5:-1:2]) #양의 정수와 음의 정수 섞어서 인덱스를 사용해도 된다

#슬라이싱 인덱스의 기본값

#시작 인덱스의 기본값 : 0
#끝 인덱스의 기본값 : 문자열의 길이
#보폭의 기본값 : 1

print(colors[:3:])
print(colors[5::2])
print(colors[:3])

#슬라이싱 인덱스의 범위
print(colors[-30:100]) #오류 발생 X
print(colors[5:100:3])

#역순 슬라이싱
print(colors[-2:-8:-3]) #역순으로 할때는 시작인덱스가 끝인덱스보다 크면된다.
print(colors[::-1]) #보폭 -1로 해놓고, 시작인덱스와 끝인덱스를 생략하면 문자열 전체를 역순으로 확인한다.

#7.3 불변자료형: 문자열

# word = 'hello'
# word[0] = 'H' #문자열은 불변자료형이다. 즉, 한번 생성된 문자열은 다시 수정할 수 없다. 인덱싱 또는 슬라이싱을 사용할 경우 type error 발생

#소문자를 대문자로 교체하는 일이 허용되지는 않지만 주어진 문자열을 이용하여 다음과 같이 표현 가능

word ='hello'
print("H"+word[1:])


#7.4 문자열 메서드 (특정 자료형에서만 사용하는 함수를 메서드라고 한다.)
# 메서드는 일반적인 함수와는 달리 특정 자료형의 값을 먼저 언급하고 바로 이어서 점(.)을 찍은 다음 호출한다.
# 문자열 자료형은 다양한 메서드 사용

# 탐색 기능

# count() 지정된 문자열이 등장한 횟수 반환
# find() 지정된 문자열이 시작하는 인덱스의 반환 지정된 문자열이 없다면 -1반환
# index() 지정된 문자열이 시작하는 인덱스 반환 지정된 문자열이 없다면 오류
# startswith() 지정된 문자열로 시작하는지 여부 판단 
# endswith() 지정된 문자열로 끝나는지 여부 판단   

# 소문자 대문자
# lower() 모든 영어 알파벳을 소문자로 바꾼 문자열 반환
# upper() 모든 영어 알파벳을 대문자로 바꾼 문자열 반환

# 교체 삭제
# replace() 지정된 문자열이 다른 문자열로 교체된 문자열 반환
# strip() 양끝에서 지정된 모든 문자가 최대한 많이 삭제된 문자열 반환

# 쪼개기 결합
# split() 문자열을 쪼개서 생성된 부분 문자열들로 구성된 리스트 반환
# join() 여러 개의 문자열을 결합해서 생성한 문자열 반환


words = ' \tMy life is so so cool! \n'
print(words.count('so'))
print(words.count('soo')) #등장 X
print(words.find('cool'))
print(words.index('life'))
print(words.startswith(' \tMy')) #지정된 문자열로 시작하는지
print(words.endswith('\n')) #지정된 문자열로 끝나는지

print(words.lower())
print(words.upper())

print(words.replace('cool','nice'))
print(words.strip()) #양끝에 있던 화이트 스페이스들이 삭제됨.
print(words.strip().startswith('My'))
print(words.strip(' \t\n!lMy')) #인자 문자열을 지정하면 인자에 포함된 모든 기호를 문자열 양끝에서 최대한 많이 삭제한 문자열을
#반환한다.

print(words.split()) #이 과정에서 문자열 양끝에 있는 화이트 스페이스들은 제거된다

hyphen_words = 'My-life-is-so-so-cool!'
print(hyphen_words.split('-'))

print('*'.join('hello'))

words_splitted = hyphen_words.split('-')
print(' '.join(words_splitted))
print(' '.join(hyphen_words.split('-')))


#예제
lyrics = "\t When you're smiling, the whole worlds smiles with you.\n\t"
# #질문 1
# 문자열 양 끝에 있는 화이트 스페이스를 모두 삭제하고, 모든 문자는 소문자로 변환된 문자열을 생성하는 한 줄 코드를
# 작성하라 또한 "you're" 대신에 "you are" 가 사용되도록 해야한다.

print(lyrics.strip('\t \n').lower().replace('you\'re','you are'))

#질문 2
#lyrics가 가리키는 문자열이 대문자 W로 시작하는지 여부를 판단하는 한 줄 코드를 작성하라. 단, 화이트 스페이스는 무시한다.
print(lyrics.strip().startswith('W'))

#질문3
# 위 문자열이 you. 로 끝나는지 여부를 판단하는 한줄 코드 , 단 화이트 스페이는 무시한다.
print(lyrics.strip().endswith('you.'))

# #예제 ? 
# 다음 세개의 함수는 모두 입력된 문자열이 소문자를 포함하고 있는지 여부를 조사하도록 구현되었지만 하나만 제대로 작동한다.
# 어느 함수가 제대로 작동하는지 확인한 다음 그 이유를 설명하라. 또한 다른 두 함수가 적절하게 구현되지 않은 이유를 설명하라.



def any_lowercase1(text):
    for c in text:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(text):
    for c in text:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(text):
    flag = False
    for c in text:
        flag = flag or c.islower()
    return flag

print(any_lowercase1('ABcDE'))
print(any_lowercase2('ABcDE'))
print(any_lowercase3('ABcDE'))   
#flag 변수는 소문자를 찾았는지 여부를 기억한다. for c in text 반복문에서 c가 text에 포함된 문자하나 
#하나를 가리킬 때 소문자를 만나는 순간 c.islower()가 True가 되고 따라서 or 연산자에 의해 flag이 계속해서
#True를 가리키게 된다. 즉, 소문자가 하나라도 포함되면 True를 반환한다.

#예제 ?
# 문자열 a:b:c:d을 이용하여 문자열 a#b#c#d 생성하는 코드를 작성
# 힌트 : split()과 join () 메서드 활용

munja = 'a:b:c:d'
print('#'.join(munja.split(':')))

#예제 ?
#변수와 함수의 이름을 지정할 떄 낙타표깃법 또는 팟홀 표기법을 사용한다.

# 낙타 표기법 : 소문자로 시작하고, 이어지는 단어의 시작은 대문자로 작성하는 표기법.
   #예제: userName, printMassage, countA
# 팟홀 표기법 : 모두 소문자, 띄어쓰기는 언더바
   #예제: user_name, print_massage, count_a

#낙타 표기법을 팟홀 표기법으로 변환하는 camel2pothole() 함수 구현
#힌트 : isupper() 메서드 사용

def camel2pothole(word):
    pothole_word = ""
    for char in word:
        if char.isupper():
            pothole_word+="_" + char.lower()
        else:
            pothole_word+=char
    return pothole_word
print(camel2pothole("userName"))

#예제 ?
# 문자열의 find() 메서드가 작동하는 방식을 이해하기 위해 find() 함수를 직접 정의하려 한다.

# 질문 1
# 문자열 find() 메서드에 대응하는 find() 함수를 직접 정의하라.
print('banana'[1:1+3]=='ana')

def find(word1, word2):
    for idx in range(len(word1)):
        if word2 == word1[idx:idx+len(word2)]:
            return idx
        
    return -1

print(find('banana', 'ana'))

#질문 2
#부분 문자열의 포함 여부를 지정된 인덱스로부터 확인할 수 있도록 위 함수를 수정하라. 이를 위해 다음 position
#매개변수를 셋째 매개변수로 추가한다.


def find(word1, word2, position=0):
    for idx in range(position,len(word1)):
        if word2 == word1[idx:idx+len(word2)]:
            return idx
        
    return -1

print(find('banana', 'ana',2))

# 예제 ?
# 어구진철은 주어진 단어에 사용된 철자의 순서를 변경해서 생성되는 단어를 가리킨다. 예를 들어 "python"과 "thpyon" 서로 어구진철
# 관계이다. 주어진 두 단어의 어구진철 여부를 판정하는 is_anagram() 함수를 다음과 같이 구현할 수 있다.

# 질문 1
# 주어진 두 단어의 어구진철 관계여부를 판단하는 is_anagram() 함수를 선언
# 힌트 sorted() 함수 사용
def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)

print(is_anagram("banana","naanba"))

#질문 1
#위함수는 공백이 포함되는 경우 정확하게 작동하지 않는다. 이를 고쳐라
def is_anagram(word1, word2):
        return sorted(word1.replace(' ','')) == sorted(word2.replace(' ',''))

print(is_anagram("bana          na","naanb    a"))

# 예제 ?
# 단어 뿐만아니라 문장이 주어졌을 때 회문인지 여부를 판단하는 함수 구현
#질문 1
#하나의 문자열과 함께 호출되면 공백 문자뿐만 아니라 문자열에 포함된 모든 기호가 제거된 문자열을 반환
#하는 no_nonWord()

nonWord_chr = ' .,!?'
word = "여보게, 저게 저게 보여?"

for chr in nonWord_chr:
    word = word.replace(chr, "")

print(word)

def no_nonWord(word):
    nonWord_chr = ' .,!?'
    for word in nonWord_chr:
        word = word.replace(nonWord_chr,"")
    
    return word

#질문 2
#하나의 문자열과 함께 호출되었을 때 회문 여부를 True/False로 반환하는 palindrome()을 작성하라. 단, 공백은 무시되고 대소문자도
#구분되지 않는다.

def palindrome(word):
    word_ = word.lower().replace(" ","")
    return word_ == word_[::-1]

print(palindrome("다시 합창합시다"))

#질문 3
#추가로 점, 쉼표, 느낌표, 물음표, 하이픈 등도 무시한다.
def palindrome(word):
    word_ = word.lower()
    word_ = no_nonWord(word_)
    return word_ == word_[::-1]
print(palindrome("다시 합창합시다 !!!!!!!!"))