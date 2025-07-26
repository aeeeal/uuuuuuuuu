# 1.화면에 Hello World 문자열을 출력하세요.
print('Hello Wolrd')
#2 화면에 Mary's cosmetics을 출력하세요(중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")
#3 화면에 아래 문장을 출력하세요 (중간에 "가 있음에 주의하세요.)
#신씨가 소리질렀다. "도둑이야".
print('신씨가 소리질렀다. "도둑이야".')
# 4 화면에 "C:\Windows"를 출력하세요 .
print('"C:\Windows"')
# 5 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요
print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n은 줄을 나누고 \t는 공백 네개를 생성한다
# 6 print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
#print("오늘은","일요일")
#예상:오늘은 일요일
# 7 print() 함수를 사용하여 다음과 같이 출력하세요.
#naver;kakao;sk;samsung
print('naver;kakao;sk;samsung')
# 8 print()함수를 사용하여 다음과 같이 출력하세요.
#naver/kakao/sk/samsung
print('naver/kakao/sk/samsung')
# 9 다음 코드를 수정하여 줄바꿈 없이 출력하세요.(힌트: end=' ')
#단, print 함수는 두 번 사용합니다.
#세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
#print("first");print("second")
print("first",end='');print('second')
# 10 5/3의 결과를 화면에 출력하세요.
print(5/3)
# 11 삼성전자라는 변수에 50,000원을 할당(저장)해보세요.
#삼성전자 주식 10주를 보유하고 있을 때 총 평가금액(삼성전자*10)을 출력하세요.
삼성전자=50000
print('총 평가금액',삼성전자*10)
# 12 변수 s와 t에는 각각 문자열이 저장되어있습니다.
#s='hello'
#t='python'
#두 변스를 이용하여 아래와 같이 출력해보세요.
#실행 예: hello! python
s='hello'
t='python'
print(s+'!',t)
# 13 type() 함수는 데이터 타입을 판별합니다.
#변수 a에는 128숫자가 할당돼 있어 type 함수가 int (정수)형임을 알려줍니다.
#>>a=128
#>>print(type(a))
#<class 'int'>
#아래 변수에 저장된 값의 타입을 판별해보세요
#>>a="132"
a="132"
print(type(a))
# 14 문자열 '720'를 정수형으로 변환해보세요.
#>> num_str='720'
num_str='720'
num_str=int(num_str)
print(type(num_str))
# 15 정수 100을 문자열 '100'으로 변환해보세요.
# num=100
num=100
num=str(num)
print(type(num))
# 16 문자열 '15.79'를 실수(float) 타입으로 변환해보세요.
print(float('15.79'))
# 17 year라는 변수가 문자열 타입의 연도를 할당(저장)하고 있습니다.
#이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
#year="2020"
year="2020"
year=int(year)
print(2024,2023,2022)
# 18 에어컨이 월 48584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다.
#총 금액을 계한한 후 이를 화면에 출력해보세요. (변수 사용하기)
a=48584
b=36
print(a*b)
# 19 letters가 바인딩하는 문자열에서 첫 번째와 세 번째 문자를 출력하세요.
#>>letters='python'
#실행 예:p t
letters='python'
print(letters[0],letters[2])
# 20 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
#>>license_plate="24가2210"
#실행 예:2210
license_plate='24가 2210'
print(license_plate[4:9])
# 21 아래의 문자열에서 '홀'만 출력하세요.
#>>string = '홀짝홀짝홀짝'
#실행 예: 홀홀홀
string='홀짝홀짝홀짝'
print(string[0::2])
# 22 문자열을 거꾸로 뒤집어 출력하세요.
#>>string="PYTHON"
#실행 예:NOHTYP
string='PYTHON'
print(string[::-1])
# 23 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
#>> phone_number='010-1111-2222'
# 실행 예:010 1111 2222
phone_number='010-1111-2222'
print(phone_number.replace('-',' '))
# 24 위 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
#실행 예:01011112222
print(phone_number.replace('-',''))
# 25 url에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
#>>url="http://sharebook.kr
#실행 예:kr
url='https://sharebook.kr'
print(url[18:20])
# 26 아래 코드의 실행 결과를 예상해보세요.
#>>lang='python'
#>>lang[0]='P'
#>>print(lang)
#예상:같이 쓰면 에러 따로 쓰면 두번째 줄에서 에러뜨고 세번째 줄은 python 출력

# 27 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
#>>string='abcdfe2a354a32a'
#실행 예:Abcdfe2A354A32A
string='abcdfe2a354a32a'
print(string.replace('a','A'))
# 28 아래 코드의 실행 결과를 예상해보세요.
#>>string='abcd'
#>>string.replace('b','B')
#>>print(string)
#예상:aBcd

# 29 아래 코드의 실행 결과를 예상해보세요.
#>>a='3'
#>>b='4'
#>>print(a+b)
#예상:34

# 30 아래 코드의 실행 결과를 예상해보세요.
#>>print("Hi"*3)
#예상:HiHiHi

# 31 화면에 '-'를 80개 출력하세요
#실행 예: --------------------------------------------------------------------------------
print('-'*80)
# 32 변수에 다음과 같은 문자열이 할당(저장)되어 있습니다.
#>>>t1='python'
#>>>t2='java'
#변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
#실행 예:python java python java python java python java
t1='python'
t2='java'
print((t1+' '+t2+' ')*4)
# 33 변수에 다음과 같이 문자열과 정수가 변수에 저장되어 있을 때
# % formatting을 사용해서 다음과 같이 출력해보세요.
#name1='김민수'
#age1=10
#name2='이철희'
#age2='13'
#실행 예: 이름: 김민수 나이: 10
#이름: 이철희 나이: 13
name1='김민수'
age1=10
name2='이철희'
age2='13'
print('{},{},{},{}'.format('이름:',name1,'나이:',age1))
print('{},{},{},{}'.format('이름:',name2,'나이:',age2))
# 34 삼성전자의 상장주식수가 다음과 같습니다.
#콤마(,)를 제거한 후 이를 정수 타입으로 변환 해보세요.
#상장주식수='5,969,782,550'
상장주식수='5,969,782,550'
상장주식수=상장주식수.replace(',','')
상장주식수=int(상장주식수)
print(상장주식수)
# 35 다음과 같은 문자열에서 '2020/03'만 출력하세요.
#분기="2020/03(E) (IFRS연결)"
분기="2020/03(E) (IFRS연결)"
print(분기[0:7])
# 36 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
#data="      삼성전자      "
data="      삼성전자      "
data=data.strip()
print(data)
