Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    t
NameError: name 't' is not defined
b=[]
b.append(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b.append(a)
NameError: name 'a' is not defined
b.append('a')
b
['a']
b='abab'
b[1]
'b'
A=input().split
a b c
A
<built-in method split of str object at 0x00000160B5E296F0>
print(A)
<built-in method split of str object at 0x00000160B5E296F0>
a=input().split()
a b c
a
['a', 'b', 'c']
10>=1
True
10=>
SyntaxError: cannot assign to literal
10=>1
SyntaxError: cannot assign to literal
10>=1
True

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 5, in <module>
    for i in a:
TypeError: 'int' object is not iterable

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
for i in a:
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'for i in a:'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec419 62.4 Platinum
comkiwer 52.3 Platinum
eva 60.7 Silver
ohjtgood 49.7 Gold
teriusu 65.1 Bronze
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 8, in <module>
    for i in a:
TypeError: 'int' object is not iterable

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec419 62.4 Platinum
comkiwer 52.3 Platinum
eva 60.7 Silver
ohjtgood 49.7 Gold
teriusu 65.1 Bronze
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 9, in <module>
    if int(b[c])>=60 and b[c+1]!=Bronze:
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
b=['a','b','c']
b[3]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b[3]
IndexError: list index out of range
b[2]
'c'
int(b[2])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int(b[2])
ValueError: invalid literal for int() with base 10: 'c'
b=[1,2,3,4,5]
b=['1','2','3','4']
b[1]==2
False
b[1]
'2'
b[1]>1
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b[1]>1
TypeError: '>' not supported between instances of 'str' and 'int'
int(b[1])>1
True

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohjt 49.7 Gold
ter 65.1 Bronze
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 9, in <module>
    if int(b[c])>=60 and b[c+1]!='Bronze':
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
b
[['hec', '62.4', 'Platinum'], ['com', '52.3', 'Platinum'], ['eva', '60.7', 'Silver'], ['ohjt', '49.7', 'Gold'], ['ter', '65.1', 'Bronze']]
b[1]
['com', '52.3', 'Platinum']
a=input().split()
co 60.1 Gold
a
['co', '60.1', 'Gold']
b
[['hec', '62.4', 'Platinum'], ['com', '52.3', 'Platinum'], ['eva', '60.7', 'Silver'], ['ohjt', '49.7', 'Gold'], ['ter', '65.1', 'Bronze']]
c=[]
c
[]
c.append('co','60','gold')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c.append('co','60','gold')
TypeError: list.append() takes exactly one argument (3 given)

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 11, in <module>
    if int(b[c])>=60 and b[c+1]!='Bronze':
ValueError: invalid literal for int() with base 10: '62.4'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
[Gosu]hec
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 14, in <module>
    if b[d]==Platinum and float(b[d]-1)<60:
NameError: name 'Platinum' is not defined

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
[Gosu]hec
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 14, in <module>
    if b[d]=='Platinum' and float(b[d]-1)<60:
TypeError: unsupported operand type(s) for -: 'str' and 'int'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Gold
[Gosu]hec
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 14, in <module>
    if b[d]=='Platinum' and float(b[d])-1<60:
ValueError: could not convert string to float: 'Platinum'
b
['hec', '62.4', 'Platinum', 'com', '52.3', 'Platinum', 'eva', '60.7', 'Silver', 'ohj', '49.7', 'Gold', 'ter', '65.1', 'Gold']
d
2
b[d]
'Platinum'
b[d]-1
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b[d]-1
TypeError: unsupported operand type(s) for -: 'str' and 'int'
float(b[d-1])
62.4

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
[Gosu]hec
[Gosu]eva

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
[Gosu]hec
[Gosu]eva
for i in range(5):
    if 1==1:
        print('a')
    if 2==2:
        print('b')

        
a
b
a
b
a
b
a
b
a
b
b
['hec', '62.4', 'Platinum', 'com', '52.3', 'Platinum', 'eva', '60.7', 'Silver', 'ohj', '49.7', 'Gold', 'ter', '65.1', 'Bronze']
float(b[d-1])
62.4
float(b[d-1])<60
False
d+=3
float(b[d-1])
52.3
float(b[d-1])
52.3
float(b[d-1])<60
True
b[d]=='Platinum'
True
if b[d]=='Platinum' and float(b[d-1])<60:
    print('[Gosu]'+b[d-2])

    
[Gosu]com

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
[Gosu]hec
[Gosu]eva
a
5
for i in range(0,a):
    print('a')

    
a
a
a
a
a
for i in range(0,a):
    if float(b[c])>=60 and b[c+1]!='Bronze':
        print('[Gosu]'+b[c-1])
    c+=3
    if b[d]=='Platinum' and float(b[d-1])<60:
        print('[Gosu]'+b[d-2])
        d+=3
    

Traceback (most recent call last):
  File "<pyshell#61>", line 2, in <module>
    if float(b[c])>=60 and b[c+1]!='Bronze':
IndexError: list index out of range
d
2
c
16

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
hec 62.4 Platinum
com 52.3 Platinum
eva 60.7 Silver
ohj 49.7 Gold
ter 65.1 Bronze
[Gosu]hec
[Gosu]com
[Gosu]eva
print('i don't know')
      
SyntaxError: unterminated string literal (detected at line 1)

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
Pokemon
Pokemon
b
      
'Pokemon'
a[b]
      
'Pikachu'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
Pokemon
Pikachu

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
ad
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 3, in <module>
    print(a[b])
KeyError: 'ad'
print("I don't know')
      
SyntaxError: unterminated string literal (detected at line 1)

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
Pokemon
Pikachu

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
adad
I don't know

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
Digimon
Agumon

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
Yugioh
I don't know

d
      
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
a=[1,2,3,4]
      
1in a
      
True
a=['a','b','c','d']
      
a[]a
      
SyntaxError: invalid syntax
a[a]
      
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a[a]
TypeError: list indices must be integers or slices, not list
a['a']
      
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a['a']
TypeError: list indices must be integers or slices, not str
a.find('a')
      
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.find('a')
AttributeError: 'list' object has no attribute 'find'
list
      
<class 'list'>
union
      
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    union
NameError: name 'union' is not defined
a.union('a')
      
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.union('a')
AttributeError: 'list' object has no attribute 'union'
index
      
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    index
NameError: name 'index' is not defined
>>> a.index('a')
...       
0
>>> a
...       
['a', 'b', 'c', 'd']
>>> 
= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py
5
Korea Seul
Russia Moscow
USA Washington
Britain London
Germany Berlin
USA
Washington
