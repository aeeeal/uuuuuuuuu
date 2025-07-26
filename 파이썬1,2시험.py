Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
1
5//7
0
7//5
1
7/5
1.4
if 5>2:     print(1)

1
a=[1,2,3,4,5]
b=3
if a>b:    print('a')

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    if a>b:    print('a')
TypeError: '>' not supported between instances of 'list' and 'int'
a=map(int,a)
a
<map object at 0x0000023DF6C7FB80>
a=list(a)
a
[1, 2, 3, 4, 5]
a=map(int,a)
if a>b:    print('a')

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    if a>b:    print('a')
TypeError: '>' not supported between instances of 'map' and 'int'
a
<map object at 0x0000023DF6C7EBC0>
a=list(a)
a
[1, 2, 3, 4, 5]
q=int(input());a=a[q];if a>b:    print('a')
SyntaxError: invalid syntax
q=int(input());a=a[q]; if a>b:    print('a')
SyntaxError: invalid syntax
q=int(input());a=a[q],if a>b:    print('a')
SyntaxError: invalid syntax
q=int(input());a=a[q]if a>b:    print('a')
SyntaxError: invalid syntax
q=int(input());a=a[q]: if a>b:    print('a')
SyntaxError: invalid syntax
q=int(input());a=a[q];if a>b:    print('a')
SyntaxError: invalid syntax
q=int(input());a=a[q];print(if a>b:    print('a'))
SyntaxError: invalid syntax
if 5>2   print(1)
SyntaxError: invalid syntax

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
1
q=int(input());a=a[q];print(if a>b:    print('a'))
SyntaxError: invalid syntax
q=int(input());a=a[q]
2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    q=int(input());a=a[q]
NameError: name 'a' is not defined
a
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=[1,2,3,4,5]
q=int(input());a=a[q]2
SyntaxError: incomplete input
q=int(input());a=a[q]
2
a
3
q=int(input());a=a[q];if a>b:   print('f')
SyntaxError: invalid syntax

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
4
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 2, in <module>
    a=a[q]
NameError: name 'a' is not defined

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
4
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 4, in <module>
    if a>b:   print('f')
NameError: name 'b' is not defined

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
4
f

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
first
second

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
first,end=5

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 26, in <module>
    print('first',end=5)
TypeError: end must be None or a string, not int

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
first5

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
first second

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello!

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello ! python

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 40, in <module>
    print(s+1,t)
TypeError: can only concatenate str (not "int") to str

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
720

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t



==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t


==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
0가

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t


==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t


==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
1


==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
짝짝짝

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 97, in <module>
    print(phone_number.remove('-'))
AttributeError: 'str' object has no attribute 'remove'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 97, in <module>
    print(phone_number.pop('-'))
AttributeError: 'str' object has no attribute 'pop'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 97, in <module>
    print(phone_number.remove('-'))
AttributeError: 'str' object has no attribute 'remove'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222


==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
lang='python'
lang[0]='P'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lang[0]='P'
TypeError: 'str' object does not support item assignment
print(lang)
python

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 112, in <module>
    lang[0]='P'
TypeError: 'str' object does not support item assignment

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
s='abcd'
s.replace('b','B')
'aBcd'
print(string)
abcdfe2a354a32a
print(s)
abcd

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python javapython javapython javapython java

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
{} {} {} 이름:
{} {} {} 이름:

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
{0} {1} {2} 10
{0} {1} {2} 13

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
{} {} {} 이름:
{} {} {} 이름:

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
이름:,김민수,나이:,10
이름:,이철희,나이:,13

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
이름:,김민수,나이:,10
이름:,이철희,나이:,13
5969782550

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
이름:,김민수,나이:,10
이름:,이철희,나이:,13
5969782550
2020/03
>>> 
==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Hello Wolrd
Mary's cosmetics
신씨가 소리질렀다. "도둑이야".
"C:\Windows"
안녕하세요.
만나서		반갑습니다.
naver;kakao;sk;samsung
naver/kakao/sk/samsung
firstsecond
1.6666666666666667
총 평가금액 500000
hello! python
<class 'str'>
<class 'int'>
<class 'str'>
15.79
2024 2023 2022
1749024
p t
2210
홀홀홀
NOHTYP
010 1111 2222
01011112222
kr
Abcdfe2A354A32A
--------------------------------------------------------------------------------
python java python java python java python java 
이름:,김민수,나이:,10
이름:,이철희,나이:,13
5969782550
2020/03
삼성전자
