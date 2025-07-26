Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
1

1= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 1, in <module>
    n=int(input('숫자 10개').split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 2, in <module>
    print(int(n)/10)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int(n)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(n)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 2, in <module>
    print(sum(n))
TypeError: unsupported operand type(s) for +: 'int' and 'str'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 3, in <module>
    print(sum(n))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
map(int,n)
<map object at 0x00000250723386A0>
list=n
n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
n=list(map(int,n))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    n=list(map(int,n))
TypeError: 'list' object is not callable
n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
n=list(map(int,n))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    n=list(map(int,n))
TypeError: 'list' object is not callable
list
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
list=0
n
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
n=list(map(int,n))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    n=list(map(int,n))
TypeError: 'int' object is not callable
list
0
list=None
list
n=list(map(int,n))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    n=list(map(int,n))
TypeError: 'NoneType' object is not callable
n=list(map(float,n))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    n=list(map(float,n))
TypeError: 'NoneType' object is not callable
n=map(int,n)
n
<map object at 0x0000025072339E40>
n=list(map(int,n))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    n=list(map(int,n))
TypeError: 'NoneType' object is not callable
n
<map object at 0x0000025072339E40>
n=[1,2,3,4,5]
n=list(map(float,n))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    n=list(map(float,n))
TypeError: 'NoneType' object is not callable

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
55

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
55

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
숫자 10개1 2 3 4 5 6 7 8 9 10
5.5
n=[1,2,3,4,5]
n=map(int,n)
n
<map object at 0x0000016F57168E20>
n=list(n)]
SyntaxError: unmatched ']'
n=list(n)
n
[1, 2, 3, 4, 5]
a='1'
b='2'
a,b=map(int,a,b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a,b=map(int,a,b)
TypeError: 'str' object cannot be interpreted as an integer
a=map(int,a)
a
<map object at 0x0000016F57120B20>
a=list(a)
a
[1]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
3 4
3 4

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
12345
n
'12345'
n=list(n)
n
['1', '2', '3', '4', '5']
n='12345'
list(n)_
SyntaxError: invalid syntax
list(n)
['1', '2', '3', '4', '5']

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
12345
<map object at 0x000001FED4D88AC0>

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
12345
[1.0, 2.0, 3.0, 4.0, 5.0]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 4, in <module>
    print(list(A)*B)
TypeError: 'int' object is not iterable
A
55
list(A)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list(A)
TypeError: 'int' object is not iterable
list(a)
['5', '5']
a
'55'
b
'3'
list(b)
['3']
list(B)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    list(B)
TypeError: 'int' object is not iterable
g=[1,2]
h
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    h
NameError: name 'h' is not defined
g
[1, 2]
list(A)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    list(A)
TypeError: 'int' object is not iterable
A=list(A)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    A=list(A)
TypeError: 'int' object is not iterable
g*3
[1, 2, 1, 2, 1, 2]
A
55














list(A)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list(A)
TypeError: 'int' object is not iterable
n=[]
n=n.append(A)
n
n
n=[ ]
n
[]
n=[]
n
[]
n=n.append(A)
n
A
55
n=[]
n=n.insert(0,A)
n
n
n[0]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    n[0]
TypeError: 'NoneType' object is not subscriptable
g=[1,2,3]
g[1]
2

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
['5', '5', '5', '5', '5', '5']
a
'55'
list(a)
['5', '5']
a=int(a)
list(a)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
a
55

5= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 4, in <module>
    a=list(a)
TypeError: 'int' object is not iterable
a=1
list(a)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
list1
165

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 5, in <module>
    list1=list(a)*B
TypeError: 'int' object is not iterable
a='55'
list(a)
['5', '5']
g=[]
g.append(a)
g
['55']
a=int(a)
g.append(a)
g
['55', 55]
h=[]
h.append(a)
a
55
a=list(a)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a=list(a)
TypeError: 'int' object is not iterable
h.append(a)
hg
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    hg
NameError: name 'hg' is not defined
h
[55, 55]












= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
3333333333333333333333333333333333333333333333333333333
a
55
b
'3'
a
55
a
55
n
[55]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 6, in <module>
    print(n*b)
TypeError: can't multiply sequence by non-int of type 'str'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
[55, 55, 55]

7 10
SyntaxError: invalid syntax


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
7 10
[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 4, in <module>
    list1=list(value)*count
TypeError: 'int' object is not iterable
list(value)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    list(value)
TypeError: 'int' object is not iterable

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
list1
[165]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
55 3
[55, 55, 55]
a='1'
a=int(a)
a=list(a)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a=list(a)
TypeError: 'int' object is not iterable
a=100
a=str(a)
a=list(a)
a
['1', '0', '0']
a=5
h=[]
h.append(a)
a
5
h
[5]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
['Salad', 'Pizza', 'Chicken', 'Soup']

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
Python is exciting

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
[1, 2, 3] [3, 6, 9] [3, 6, 9] [3, 6, 9] [2, 4, 6]
_1+_2
[1, 2, 3, 2, 4, 6]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
[1, 2, 3, 3, 6, 9, 3, 6, 9, 3, 6, 9, 2, 4, 6]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
-3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 4, in <module>
    print(a[2]);print(a[1]);print(a[0])
TypeError: 'NoneType' object is not subscriptable

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 4, in <module>
    print(a[2]);print(a[1]);print(a[0])
TypeError: 'NoneType' object is not subscriptable
a
a
a=[1,2]

a
a
[1, 2]
c=-3
a.append(c)
a
[1, 2, -3]
a=a.append(c)
a
a
print(a)
None
a=a.insert(2,c)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a=a.insert(2,c)
AttributeError: 'NoneType' object has no attribute 'insert'
a=[1,2]
a=a.insert(2,c)
a
a=[1,2]
c=-3
a=a.append(c)
a
a.append(c)
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a.append(c)
AttributeError: 'NoneType' object has no attribute 'append'
a=[1,2]
a.append(c)
a
[1, 2, -3]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
-3
-3
2
1

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
Eagle
E
g
len.a
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    len.a
AttributeError: 'builtin_function_or_method' object has no attribute 'a'
a
['E', 'a', 'g', 'l', 'e']
a.len
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    a.len
AttributeError: 'list' object has no attribute 'len'
]
a
['E', 'a', 'g', 'l', 'e']
a.len
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    a.len
AttributeError: 'list' object has no attribute 'len'
len(a)
5

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
Element?Seoul
Element?New York City
Element?Tokyo
Element?Beijing
Element?London
Element?Paris
Index?3
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 9, in <module>
    print(x[q:])
TypeError: slice indices must be integers or None or have an __index__ method
x
['Seoul', 'New York City', 'Tokyo', 'Beijing', 'London', 'Paris']
x[1:3]
['New York City', 'Tokyo']
x[1:]
['New York City', 'Tokyo', 'Beijing', 'London', 'Paris']

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
Element?Seoul
Element?New York City
Element?Tokyo
Element?Beijing
Element?London
Element?Paris
Index?3
['Beijing', 'London', 'Paris']

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
Element?seoul
Element?newyork
Element?tokyo
Element?beij
Element?london
Element?praris
seoultokyolondonnewyorkbeijpraris

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
Element?Seoul
Element?New York City
Element?Tokyo
Element?Beijing
Element?London
Element?Paris
['Seoul', 'Tokyo', 'London', 'New York City', 'Beijing', 'Paris']

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
3
[3, 6, 9, 12, 15]


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
4
[4, 8, 12]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
2
[2, 4, 6, 8, 10, 12, 14]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
I My Me Mine
['Mine', 'Me', 'My', 'I']


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
a b c d
['d', 'c', 'b', 'a']
a=1
if a=1:print('b')
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if a==1:print('b')
a
SyntaxError: invalid syntax
a
1
if a==1:print('b')
a
SyntaxError: invalid syntax
if a==1:print('b'))
SyntaxError: unmatched ')'
if a==1:
    print('b')

    
b
if a==1:print('b')

b

if a==2:print('b')
else:print('c')

c
0=0.0=
SyntaxError: cannot assign to literal
SyntaxError: cannot assign to literal
SyntaxError: invalid syntax
0==0.0
True
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError:
    
SyntaxError: invalid syntax
a='bool'
a
'bool'
b=bool
b
<class 'bool'>
bool=b
b
<class 'bool'>
bool(1>2)
False
bool(2>)
SyntaxError: invalid syntax
bool(2>1)
True
b(2>1)
True
a(2>1)
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    a(2>1)
TypeError: 'str' object is not callable
bool("723")>bool("327")
False
bool(723)>bool(327)
False
bool(723)
True
bool(327)
True
bool(723>327)
True
bool(723)>bool(327)
False
A=True
B=False
((A or B) and (not A))
False
a=7
b=50
print(a**2<b)
True
print(not a!=b)
False
not(a!=b)
False
a=10
b=20
print(a>b or a<20)
True
b=1
print(not b<0)
True

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
a b c97 10 6
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 1, in <module>
    a,b,c=int(input('a b c').split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    a
NameError: name 'a' is not defined
a,b,c=input().split()
1 2 3
>>> a
'1'
>>> b
'2'
c
>>> 
>>> c
'3'
>>> a,b,c=int(input().split())
1 2 3
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    a,b,c=int(input().split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> 
= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
a b c97 10 6
True
False
