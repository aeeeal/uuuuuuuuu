Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
tuple
<class 'tuple'>
type(tuple)
<class 'type'>
a=tuple('a','b','c')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a=tuple('a','b','c')
TypeError: tuple expected at most 1 argument, got 3
tu=(1,2,3)'
SyntaxError: unterminated string literal (detected at line 1)
tu=(1,2,3)
tu
(1, 2, 3)
a=()

a
()
n=tuple()
b=tuple(1,2,3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b=tuple(1,2,3)
TypeError: tuple expected at most 1 argument, got 3
b=tuple(1,)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b=tuple(1,)
TypeError: 'int' object is not iterable
b=tuple('a',)
b
('a',)
g=tuple('a')
g
('a',)
a=1,2,3
b=(1,2,3)
print(type(a),type(b))
<class 'tuple'> <class 'tuple'>
c=1
d=1
print(type(c),type(d))
<class 'int'> <class 'int'>
e=(1)
f=(1,)
print(type(e),type(f))
<class 'int'> <class 'tuple'>
d=1,
print(type(c),type(d))
<class 'int'> <class 'tuple'>
g=(1,'a',1>0)

g
(1, 'a', True)
g=tuple(1)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    g=tuple(1)
TypeError: 'int' object is not iterable
g=tuple('a')

g
('a',)
g=('a')
g
'a'
g=('a',)
g
('a',)
tu=(1,'a',1>0)
tu[2]
True
print(tu[2])
True
tu[:]
(1, 'a', True)
tu=[-2,-1]
tu=(1,'a',1>0)
tu[-2:-1]
('a',)
tu[::-1]
(True, 'a', 1)
3
3

tu=tuple('경상도 서울 경기도 충청도'.split())
tu
('경상도', '서울', '경기도', '충청도')
a,b,c,d=tu
tu
('경상도', '서울', '경기도', '충청도')
a
'경상도'
a=[]
append(a,1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    append(a,1)
NameError: name 'append' is not defined
a
[]
a.append(1)
a
[1]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
()
[2]
[2, 4]
[2, 4, 6]
[2, 4, 6, 8]
[2, 4, 6, 8, 10]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
()
[2, 4, 6, 8, 10]
a=()
a
()
a.append(2)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.append(2)
AttributeError: 'tuple' object has no attribute 'append'
a
()
data=tuple(1,2,3,4,5,6,7,8,9,10)
print(data)
mylist=[]
for a in range(1,11):
    if a%2==0:
        mylist.append(a)
print(data)
SyntaxError: multiple statements found while compiling a single statement

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 1, in <module>
    data=tuple(1,2,3,4,5,6,7,8,9,10)
TypeError: tuple expected at most 1 argument, got 10

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
놀랍게도 이 튜플은 동물이름 모음집이다.
댕댕이는 강아지,냥이는 고양이,
꼬부기는 거북이,꿀꿀이는 돼지,삐약이는 병아리를 말한다.
댕댕이 꼬부기 삐약이
댕댕이 냥이 꿀꿀이 삐약이

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
놀랍게도 이 튜플은 동물이름 모음집이다.
댕댕이는 강아지,냥이는 고양이,
꼬부기는 거북이,꿀꿀이는 돼지,삐약이는 병아리를 말한다.
댕댕이 꼬부기 삐약이
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 8, in <module>
    print(list(a,b,d,e))
TypeError: list expected at most 1 argument, got 4
KeyboardInterrupt
list(a,b,c,d)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    list(a,b,c,d)
TypeError: list expected at most 1 argument, got 4

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
놀랍게도 이 튜플은 동물이름 모음집이다.
댕댕이는 강아지,냥이는 고양이,
꼬부기는 거북이,꿀꿀이는 돼지,삐약이는 병아리를 말한다.
댕댕이 꼬부기 삐약이
list['댕댕이', '냥이', '꿀꿀이', '삐약이']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
놀랍게도 이 튜플은 동물이름 모음집이다.
댕댕이는 강아지,냥이는 고양이,
꼬부기는 거북이,꿀꿀이는 돼지,삐약이는 병아리를 말한다.
댕댕이 꼬부기 삐약이
['댕댕이', '냥이', '꿀꿀이', '삐약이']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
놀랍게도 이 튜플은 동물이름 모음집이다.
댕댕이는 강아지,냥이는 고양이,
꼬부기는 거북이,꿀꿀이는 돼지,삐약이는 병아리를 말한다.
댕댕이 꼬부기 삐약이
['댕댕이', '냥이', '꼬부기', '삐약이']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(2, 4, 6, 8)

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(2, 4, 6, 8, 10)
t1=(1,2,'a','b')
t2=(3,4)
print(t1+t2)
(1, 2, 'a', 'b', 3, 4)
t2=(1,2)
print(t2*3)
(1, 2, 1, 2, 1, 2)
len(t10\)
    
SyntaxError: unexpected character after line continuation character
len(t1)
    
4
max(t1)
    
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    max(t1)
TypeError: '>' not supported between instances of 'str' and 'int'
max(t2)
    
2
min(t2)
    
1
sum(t1)
    
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    sum(t1)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
sum(t2)
    
3
sorted(t2)
    
[1, 2]
sorted(t1)
    
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    sorted(t1)
TypeError: '<' not supported between instances of 'str' and 'int'
t3=3,5,4,6,5,7
    
sorted(t3)
    
[3, 4, 5, 5, 6, 7]
reversed(t3)
    
<reversed object at 0x0000020E7D159930>
llist(reversed(t3))
    
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    llist(reversed(t3))
NameError: name 'llist' is not defined. Did you mean: 'list'?
list(reversed(t3))
    
[7, 5, 6, 4, 5, 3]
tuple(reversed(t3))
    
(7, 5, 6, 4, 5, 3)
tuple(sorted(t3,reverse=True))
    
(7, 6, 5, 5, 4, 3)
list(sorted(t3,reverse=True))
    
[7, 6, 5, 5, 4, 3]
t3
    
(3, 5, 4, 6, 5, 7)
tu.count(7)
    
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    tu.count(7)
NameError: name 'tu' is not defined
tu3.count(7)
    
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    tu3.count(7)
NameError: name 'tu3' is not defined. Did you mean: 't3'?
t3.count(7)
    
1
t3.count(3)
    
1
t3.count(5)
    
2
t3.index(1)
    
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    t3.index(1)
ValueError: tuple.index(x): x not in tuple
t3
    
(3, 5, 4, 6, 5, 7)
t3.index(1)
    
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    t3.index(1)
ValueError: tuple.index(x): x not in tuple
t3
    
(3, 5, 4, 6, 5, 7)
t3.index(3)
    
0
t3.index(5)
    
1
t3.index(4)
    
2

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 2, in <module>
    for a in range((0,11)):
TypeError: 'tuple' object cannot be interpreted as an integer

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
[0, 2, 4, 6, 8, 10]
t1=([1,2,0],'하나둘셋',0)
    
t2=('허잇챠')
    
print(t1[1])
    
하나둘셋

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(1, 2, 3, 4, 5, 6)(1, 2, 3, 4, 5, 6)2
(1, 2, 3, 4, 5, 6)(1, 2, 3, 4, 5, 6)4
(1, 2, 3, 4, 5, 6)(1, 2, 3, 4, 5, 6)6

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
2
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
4
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)
6

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)2
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)4
(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6)6

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
첫 번째 값1
두 번째 값2
세 번째 값3
네 번째 값4
몇 번째 값?2
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 10, in <module>
    print(a[n]*n)
IndexError: string index out of range

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
첫 번째 값1
두 번째 값2
세 번째 값3
네 번째 값42
몇 번째 값?2
33

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
첫 번째 값1
두 번째 값2
세 번째 값3
네 번째 값4
몇 번째 값?2
22

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
첫 번째 값a
두 번째 값b
세 번째 값c
네 번째 값d
몇 번째 값?4
dddd
>>> 
==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
첫 번째 값123
두 번째 값456
세 번째 값77
네 번째 값888
몇 번째 값?6
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 10, in <module>
    print(A[n-1]*n)
IndexError: tuple index out of range
>>> 
==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
첫 번째 값123
두 번째 값456
세 번째 값77
네 번째 값888
몇 번째 값?6
input error
