Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 1, in <module>
    d
NameError: name 'd' is not defined
a=1
type(a)
<class 'int'>
a=input()
a
type(a)
<class 'str'>
a=input(1)
1
type(a)
<class 'str'>
a=int(input())
a
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a=int(input())
ValueError: invalid literal for int() with base 10: 'a'
a=1
a='1'
ord(a)
49
a
'1'
chr(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    chr(a)
TypeError: 'str' object cannot be interpreted as an integer
chr(49)
'1'
a=49
chr(a)
'1'
a='49'
ord(49)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    ord(49)
TypeError: ord() expected string of length 1, but int found
ord(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
a
'49'
ord(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
chr(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    chr(a)
TypeError: 'str' object cannot be interpreted as an integer
a=input()
a
type(a)
<class 'str'>
a=type(int)
a
<class 'type'>
a
<class 'type'>
ord(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    ord(a)
TypeError: ord() expected string of length 1, but type found
a=type(str)
a
<class 'type'>
a=type
a
<class 'type'>
a=str
a
<class 'str'>
a=int
a
<class 'int'>
a+1
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a+1
TypeError: unsupported operand type(s) for +: 'type' and 'int'
a
<class 'int'>
a='49'
chr(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    chr(a)
TypeError: 'str' object cannot be interpreted as an integer
a
'49'
a=int
chr(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    chr(a)
TypeError: 'type' object cannot be interpreted as an integer
a
<class 'int'>
a=input()
49
ord(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
a
'49'
ord(49)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ord(49)
TypeError: ord() expected string of length 1, but int found
chr(49)
'1'
a
'49'
type(a)
<class 'str'>
a=input()
b
int(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'b'
'int({})'.format(a)
'int(b)'
b
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b
NameError: name 'b' is not defined
int('{}').format(a)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    int('{}').format(a)
ValueError: invalid literal for int() with base 10: '{}'
b
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b
NameError: name 'b' is not defined
a
'b'
ord(a)
98
a=49
ord(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    ord(a)
TypeError: ord() expected string of length 1, but int found
a='49'
ord(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
a='49'
type(a)=input()
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
a=type(input())
49
a
<class 'str'>
type
<class 'type'>
help
Type help() for interactive help, or help(object) for help about object.
help(type)
Help on class type in module builtins:

class type(object)
 |  type(object) -> the object's type
 |  type(name, bases, dict, **kwds) -> a new type
 |
 |  Methods defined here:
 |
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |
 |  __dir__(self, /)
 |      Specialized __dir__ implementation for types.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __instancecheck__(self, instance, /)
 |      Check if an object is an instance.
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |
 |  __sizeof__(self, /)
 |      Return memory consumption of the type object.
 |
 |  __subclasscheck__(self, subclass, /)
 |      Check if a class is a subclass.
 |
 |  __subclasses__(self, /)
 |      Return a list of immediate subclasses.
 |
 |  mro(self, /)
 |      Return a type's method resolution order.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __prepare__(name, bases, /, **kwds)
 |      Create the namespace for the class statement
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __abstractmethods__
 |
 |  __annotations__
 |
 |  __dict__
 |
 |  __text_signature__
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __base__ = <class 'object'>
 |      The base class of the class hierarchy.
 |
 |      When called, it accepts no arguments and returns a new featureless
 |      instance that has no instance attributes and cannot be given any.
 |
 |
 |  __bases__ = (<class 'object'>,)
 |
 |  __basicsize__ = 928
 |
 |  __dictoffset__ = 264
 |
 |  __flags__ = 2155896066
 |
 |  __itemsize__ = 40
 |
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |
 |  __type_params__ = ()
 |
 |  __weakrefoffset__ = 368

mro
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    mro
NameError: name 'mro' is not defined
_mro_
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    _mro_
NameError: name '_mro_' is not defined
bases
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    bases
NameError: name 'bases' is not defined. Did you mean: 'bytes'?

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
49
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 3, in <module>
    print(ord(a))
TypeError: ord() expected a character, but string of length 2 found
a=['49']
a=map(int.a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=map(int.a)
AttributeError: type object 'int' has no attribute 'a'
a=map(int,a)
a
<map object at 0x000002353C6C91E0>
a=list(a)
a
[49]
a=list(a)[0:1]
a
[49]
a['A']
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a['A']
TypeError: list indices must be integers or slices, not str
a=['A']
a=map(int,a)
a
<map object at 0x000002353C6C9330>
a=list(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    a=list(a)
ValueError: invalid literal for int() with base 10: 'A'
a

a=[100]
a=['100']
a=map(int,a)
a
<map object at 0x000002353C6C99F0>


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
49
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 7, in <module>
    print(ord(a))
TypeError: ord() expected a character, but string of length 2 found
a
'49'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
49
a
'49'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
49
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 7, in <module>
    print(ord(a))
TypeError: ord() expected a character, but string of length 2 found

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
1


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
80
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 7, in <module>
    print(ord(a))
TypeError: ord() expected a character, but string of length 2 found

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
80.
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 2, in <module>
    if int(a)!=True:
ValueError: invalid literal for int() with base 10: '80.'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
80
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 7, in <module>
    print(ord(int(a)))
TypeError: ord() expected string of length 1, but int found

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
80
ghfghfh
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 7, in <module>
    print(ord(int(a)))
TypeError: ord() expected string of length 1, but int found

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
p
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 2, in <module>
    if int(a)!=True:
ValueError: invalid literal for int() with base 10: 'p'
a=input(type(a))
<class 'str'>a


a
'a'
a,b=type(a)=input().split()
SyntaxError: cannot assign to function call
a='p'
int(a)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'p'
a='11
SyntaxError: unterminated string literal (detected at line 1)
a='11'
str(a)
'11'
int(a)
11
a
'11'
if str(a)==int('{}').format(a):
    print('d')

    
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    if str(a)==int('{}').format(a):
ValueError: invalid literal for int() with base 10: '{}'
a
'11'
str(a)
'11'
int(a)
11
int('{}').format(a)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    int('{}').format(a)
ValueError: invalid literal for int() with base 10: '{}'

int({}).format(a)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    int({}).format(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
'{}'.format(a)
'11'
('{}').format(a)
'11'
int('{}').format(a)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    int('{}').format(a)
ValueError: invalid literal for int() with base 10: '{}'
a=11
str('{}').format(a)
'11'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
5
48
53

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
1
48 57
49

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
1234
48 57 97
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py", line 13, in <module>
    print(ord(a))
TypeError: ord() expected a character, but string of length 4 found

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
1213
48 57 97

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
12h53
48 57 97
문자가 아님을 감지

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
123j56
48 57 97
j 문자가 아님을 감지
ord(A)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    ord(A)
NameError: name 'A' is not defined
ord(a)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 6 found
a
'123j56'
a=a
A
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    A
NameError: name 'A' is not defined
A=A
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    A=A
NameError: name 'A' is not defined
ord(a)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 6 found
ord('a')
97
ord('0')
48
a=input()
49
ord(a)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
a
'49'
ord('a')
97
ord(49)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    ord(49)
TypeError: ord() expected string of length 1, but int found
ord(10)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    ord(10)
TypeError: ord() expected string of length 1, but int found
ord('49')
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    ord('49')
TypeError: ord() expected a character, but string of length 2 found
ord('a')
97
ord('0')
48
ord('b')
98
ord('46')
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    ord('46')
TypeError: ord() expected a character, but string of length 2 found
ord('4')
52
ord('6')
54
46
46
chr(1)
'\x01'
chr(52,54)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    chr(52,54)
TypeError: chr() takes exactly one argument (2 given)
chr(52)
'4'
chr(56)
'8'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
h
48 57 97
h 문자가 아님을 감지
a=input()
h
a
'h'
ord(a)
104
ord(h)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    ord(h)
NameError: name 'h' is not defined

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
5
48 57 97

chr(5)
'\x05'
ord(5)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    ord(5)
TypeError: ord() expected string of length 1, but int found
ord('5')
53
chr(53)
'5'
print(\x05)
SyntaxError: unexpected character after line continuation character

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
5
48 57 97


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
1
48 57 97


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
a
48 57 97
a 문자가 아님을 감지
97

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
h
48 57 97
h 문자가 아님을 감지
104

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
12





= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
81
Q
Q

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
81
48 57 97
Q
Q
chr(81)
'Q'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
12
48 57 97


a
'12'
ord(a)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 2 found
for i in a:
    print(i)

    
1
2
chr(12)
'\x0c'
ord('12')
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    ord('12')
TypeError: ord() expected a character, but string of length 2 found
chr(2)
'\x02'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
a
48 57 97
a 문자가 아님을 감지
97

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
g
48 57 97
g 문자가 아님을 감지
103

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
d
d 문자가 아님을 감지
100

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
5


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
33
!
chr(ord('w')-1)
'v'
ord('w')
119
chr(118)
'v'
chr(ord('J')-1)
'I'
chr(ord("!")-1)
' '
ord('!')
33
chr(32)
' '
chr(ord('m')-1)
'l'
ord(m)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    ord(m)
NameError: name 'm' is not defined
ord('m')
109
chr(108)
'l'
chr(ord('p')-1)
'o'
chr(ord('f')-1)
'e'
chr(ord
KeyboardInterrupt
chr(ord(z)-1)
    
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    chr(ord(z)-1)
NameError: name 'z' is not defined
chr(ord('z')-1)
    
'y'
chr(ord('p')-1)
    
'o'

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
2*1=2
2*2=4
2*3=6
2*4=8
2*5=10
2*6=12
2*7=14
2*8=16
2*9=18

3*1=3
3*2=6
3*3=9
3*4=12
3*5=15
3*6=18
3*7=21
3*8=24
3*9=27

4*1=4
4*2=8
4*3=12
4*4=16
4*5=20
4*6=24
4*7=28
4*8=32
4*9=36

5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
5*6=30
5*7=35
5*8=40
5*9=45

6*1=6
6*2=12
6*3=18
6*4=24
6*5=30
6*6=36
6*7=42
6*8=48
6*9=54

7*1=7
7*2=14
7*3=21
7*4=28
7*5=35
7*6=42
7*7=49
7*8=56
7*9=63

8*1=8
8*2=16
8*3=24
8*4=32
8*5=40
8*6=48
8*7=56
8*8=64
8*9=72

9*1=9
9*2=18
9*3=27
9*4=36
9*5=45
9*6=54
9*7=63
9*8=72
9*9=81


= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
2단
2 4 6 8 10 12 14 16 18 
3단
3 6 9 12 15 18 21 24 27 
4단
4 8 12 16 20 24 28 32 36 
5단
5 10 15 20 25 30 35 40 45 

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
10
10
10
10

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
2
4
6
8

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
2
4
6
8
10

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
a*i 2
a*i 4
a*i 6
a*i 8
a*i 10

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
2 * 1 2
2 * 2 4
2 * 3 6
2 * 4 8
2 * 5 10

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
2 * 1 = 22 * 2 = 42 * 3 = 62 * 4 = 82 * 5 = 10

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
2*1 = 20
2*2 = 20
2*3 = 20
2*4 = 20
2*5 = 20

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?2
숫자 몇까지 곱할까요?5
2*1 = 2
2*2 = 4
2*3 = 6
2*4 = 8
2*5 = 10

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
몇 단을 출력할까요?5
숫자 몇까지 곱할까요?4
5*1 = 5
5*2 = 10
5*3 = 15
5*4 = 20

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
2
4
6
8
10
12
14
16
18
3
6
9
12
15
18
21
24
27
4
8
12
16
20
24
28
32
36
5
10
15
20
25
30
35
40
45
6
12
18
24
30
36
42
48
54
7
14
21
28
35
42
49
56
63
8
16
24
32
40
48
56
64
72
9
18
27
36
45
54
63
72
81

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
3 9 15 21 27 5 15 25 35 45 7 21 35 49 63 9 27 45 63 81 

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
[3, 9, 15, 21, 27, 5, 15, 25, 35, 45, 7, 21, 35, 49, 63, 9, 27, 45, 63, 81]

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py

* 
* * 
* * * 
* * * * 
* * * * * 

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
'{:>10}'.format('code')
    
'      code'
range(3,0,-1)
    
range(3, 0, -1)
print(range(3,0,-1))
    
range(3, 0, -1)
for i in range(3,0,-1):
    print(i)

    
3
2
1

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
3
***
**
*
*
**
***

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
3
***
**
*
*
**
***

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
5
*****
****
***
**
*
*
**
>>> ***
****
*****

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
*****
*****
>>> *****
*****
*****

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
*****
*****
>>> *****
*****
*****

= RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python313/test.py
*****
****
