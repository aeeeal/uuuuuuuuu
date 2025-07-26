Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
1

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 2, in <module>
    print(list_a(1))
TypeError: 'list' object is not callable

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
list_A
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    list_A
NameError: name 'list_A' is not defined. Did you mean: 'list_a'?
list_a
['a', 'b', 'c', 'd', 'e']
list_a.pop(1)
'b'
list_a
['a', 'c', 'd', 'e']
list_a.remove
<built-in method remove of list object at 0x000001BFF0225980>
list_a
['a', 'c', 'd', 'e']
list_a.insert(1,'b')
list_A
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list_A
NameError: name 'list_A' is not defined. Did you mean: 'list_a'?
list_a
['a', 'b', 'c', 'd', 'e']
list_a(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list_a(1)
TypeError: 'list' object is not callable
list_a[1]
'b'
list_a
['a', 'b', 'c', 'd', 'e']
list_a[3.4]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list_a[3.4]
TypeError: list indices must be integers or slices, not float
list_a[3,4]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list_a[3,4]
TypeError: list indices must be integers or slices, not tuple
list_a[3]
'd'
list_a[1][2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list_a[1][2]
IndexError: string index out of range
list_a[1],[2]
('b', [2])
list_a
['a', 'b', 'c', 'd', 'e']
list_a[1],[2]
('b', [2])
[2]
[2]
{}.format(1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    {}.format(1)
AttributeError: 'dict' object has no attribute 'format'
'{}'.format(1)
'1'
a=list('a','b')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a=list('a','b')
TypeError: list expected at most 1 argument, got 2
a
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a
NameError: name 'a' is not defined
a=list(1,2)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a=list(1,2)
TypeError: list expected at most 1 argument, got 2
a=list('a','b')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a=list('a','b')
TypeError: list expected at most 1 argument, got 2

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=list('a','b')
TypeError: list expected at most 1 argument, got 2
a=list('abcd')
a
['a', 'b', 'c', 'd']
a=('defg')
a
'defg'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
abcd
n
['a', 'b', 'c', 'd']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
'abcd'
n
["'", 'a', 'b', 'c', 'd', "'"]
a=[None]*5
a
[None, None, None, None, None]
a.append(1)
a
[None, None, None, None, None, 1]
a.append(2)
a.append(3)
a.appenda
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.appenda
AttributeError: 'list' object has no attribute 'appenda'. Did you mean: 'append'?
a
[None, None, None, None, None, 1, 2, 3]
a.append(4)
a.append(5)
a
[None, None, None, None, None, 1, 2, 3, 4, 5]
a=list()
a
[]
a=.append(1)
SyntaxError: invalid syntax
a
[]
a.append(1)
a
[1]
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a
[1, 2, 3, 4, 5]
a=[]
a
[]
a.append(1)
a.append(2)
a.append(3)
a.append(1)
a
[1, 2, 3, 1]
a.pop(3)
1
a.append(1)

a
[1, 2, 3, 1]
a.remove(1)
a
[2, 3, 1]
a.remove(1)
a
[2, 3]
a.insert(0,1)
a
[1, 2, 3]
a.append(4)
a.append(5)
a
[1, 2, 3, 4, 5]
a=list[]
SyntaxError: invalid syntax
a=list('12345')
a
['1', '2', '3', '4', '5']
a=[1,2,3,4,5]
a
[1, 2, 3, 4, 5]
n=list('12345')
print(n)
['1', '2', '3', '4', '5']
n.remove('1')
n
['2', '3', '4', '5']
n=list('12345')
print(n)
['1', '2', '3', '4', '5']
n.remove(1)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    n.remove(1)
ValueError: list.remove(x): x not in list
n=list('12345')
print(n)
['1', '2', '3', '4', '5']
n.pop(1)
'2'
print(n)
['1', '3', '4', '5']
listn[123,'hello',' ',True,0.1,'!']
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    listn[123,'hello',' ',True,0.1,'!']
NameError: name 'listn' is not defined. Did you mean: 'list'?
list_n[123,'hello',' ',True,0.1,'!']
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list_n[123,'hello',' ',True,0.1,'!']
NameError: name 'list_n' is not defined. Did you mean: 'list'?
listn=[123,'hello',' ',True,0.1,'!']
listn
[123, 'hello', ' ', True, 0.1, '!']
[123,'hello',' ',True,0.1,'!'][1]
'hello'
[123,'hello',' ',True,0.1,'!'][1][2]
'l'
listn[1,2]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    listn[1,2]
TypeError: list indices must be integers or slices, not tuple
listn[1]
'hello'
listn[0:6:1]
[123, 'hello', ' ', True, 0.1, '!']
listn[0:6:2]
[123, ' ', 0.1]
listn[1:5]
['hello', ' ', True, 0.1]
li=list('coding haru!')
li
['c', 'o', 'd', 'i', 'n', 'g', ' ', 'h', 'a', 'r', 'u', '!']
li[6]
' '
li[-4]
'a'
li[1]
'o'
li=[0,1,2,3,4,5,6,7]
li[2]
2
li[2]=3
li[2]
3
li
[0, 1, 3, 3, 4, 5, 6, 7]
print(li)
[0, 1, 3, 3, 4, 5, 6, 7]
li[li[2]]=5
li
[0, 1, 3, 5, 4, 5, 6, 7]
li[3]=3
li
[0, 1, 3, 3, 4, 5, 6, 7]
li[2]=5
li
[0, 1, 5, 3, 4, 5, 6, 7]
li[li[2]]=5
li
[0, 1, 5, 3, 4, 5, 6, 7]
li[2]=3
li
[0, 1, 3, 3, 4, 5, 6, 7]
li[li[2]]=5
li
[0, 1, 3, 5, 4, 5, 6, 7]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
['popo', None, None]
poo popo
coding[None]*3
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    coding[None]*3
TypeError: list indices must be integers or slices, not NoneType
coding=[None]*3
k=0
coding[k]='popo'
coding
['popo', None, None]
k+=1
coding[k]='poo'
print(coding)
['popo', 'poo', None]
k+=1
coding[k]='dd'
print(coding)
['popo', 'poo', 'dd']
k-=1
print(coding[k],coding[k-1])
poo popo
n=[1,0,22,'haru',67,'coding','>0<',True]
n[:-3]
[1, 0, 22, 'haru', 67]
n[5:]
['coding', '>0<', True]
n[1:7:2]
[0, 'haru', 'coding']
n[::-1]
[True, '>0<', 'coding', 67, 'haru', 22, 0, 1]
name=haru
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    name=haru
NameError: name 'haru' is not defined
name='haru'
a1,a2,a3,a4=name
a
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'a1'?
a1
'h'
a2
'a'
a3
3
a4
'u'
a3
'r'
a3
'r'
33
a5,a6,a7=name
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    a5,a6,a7=name
ValueError: too many values to unpack (expected 3)
a5,a6,a7,a8=name
li
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    li
NameError: name 'li' is not defined
print(li)
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    print(li)
NameError: name 'li' is not defined
li[0,1,2,3,4,5,6,7]
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    li[0,1,2,3,4,5,6,7]
NameError: name 'li' is not defined
li[2]=3
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    li[2]=3
NameError: name 'li' is not defined
li=[0,1,2,3,4,5,6,7]
li[2]=3
li[li[2]]=5
li
[0, 1, 3, 5, 4, 5, 6, 7]
li[2[2]]
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    li[2[2]]
TypeError: 'int' object is not subscriptable
li[a[2]]
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    li[a[2]]
NameError: name 'a' is not defined. Did you mean: 'a1'?
li[a1[2]
   li
   
SyntaxError: '[' was never closed
li[a1[2]]
   
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    li[a1[2]]
IndexError: string index out of range
li[a1[0]]
   
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    li[a1[0]]
TypeError: list indices must be integers or slices, not str
li[a1[1]]
   
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    li[a1[1]]
IndexError: string index out of range
li
   
[0, 1, 3, 5, 4, 5, 6, 7]
li[li[2]]=5
   
li
   
[0, 1, 3, 5, 4, 5, 6, 7]
li[a1[1]]=5
   
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    li[a1[1]]=5
IndexError: string index out of range
li[a1[0]]=5
   
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    li[a1[0]]=5
TypeError: list indices must be integers or slices, not str
li
   
[0, 1, 3, 5, 4, 5, 6, 7]
a1
   
'h'
a=['a','b','c','d']
   
li[a[2]]=5
   
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    li[a[2]]=5
TypeError: list indices must be integers or slices, not str
li[li[2]]=5
   
a[a[2]]=5
   
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    a[a[2]]=5
TypeError: list indices must be integers or slices, not str
a
   
['a', 'b', 'c', 'd']
a.remove[a]
   
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    a.remove[a]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.remove(a)
   
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    a.remove(a)
ValueError: list.remove(x): x not in list
a.remove('a')
   
a
   
['b', 'c', 'd']
a[a[2]]=5
   
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    a[a[2]]=5
TypeError: list indices must be integers or slices, not str
li[li[2]]
   
5
li[li]
   
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    li[li]
TypeError: list indices must be integers or slices, not list
li[2]
   
3
li[li[1]]
   
1
li
   
[0, 1, 3, 5, 4, 5, 6, 7]
li[li[0]]
   
0
li[li[2]]
   
5
li[li[3]]
   
5
li.pop[5]
   
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    li.pop[5]
TypeError: 'builtin_function_or_method' object is not subscriptable
li.pop(5)
   
5
li
   
[0, 1, 3, 5, 4, 6, 7]
li.inser(5,9)
   
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    li.inser(5,9)
AttributeError: 'list' object has no attribute 'inser'. Did you mean: 'insert'?
li.insert(5,9)
   
li
   
[0, 1, 3, 5, 4, 9, 6, 7]
li[li[3]]
   
9
li[li[4]]
   
4
li[li[5]]
   
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    li[li[5]]
IndexError: list index out of range
li[li[4]]
   
4
li[li[0]]
   
0
li[li]
   
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    i[li]
NameError: name 'i' is not defined. Did you mean: 'li'?
li[lli]
   
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    li[lli]
NameError: name 'lli' is not defined. Did you mean: 'li'?
li[li]
   
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    li[li]
TypeError: list indices must be integers or slices, not list
li[li[2]]
   
5
li
   
[0, 1, 3, 5, 4, 9, 6, 7]
n=list('python class')
   

n
   
['p', 'y', 't', 'h', 'o', 'n', ' ', 'c', 'l', 'a', 's', 's']
n.index('p'0
        
SyntaxError: '(' was never closed
n.index('p')
        
0
n.index('s')
        
10
n[6]=-
        
SyntaxError: invalid syntax
n[6]='-'
        
n
        
['p', 'y', 't', 'h', 'o', 'n', '-', 'c', 'l', 'a', 's', 's']
n[0],n[7]='P','C'
        
n
        
['P', 'y', 't', 'h', 'o', 'n', '-', 'C', 'l', 'a', 's', 's']
del n[1]
        
n
        
['P', 't', 'h', 'o', 'n', '-', 'C', 'l', 'a', 's', 's']
deln[1]
        
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    deln[1]
NameError: name 'deln' is not defined
n.pop(1)
        
't'
n
        
['P', 'h', 'o', 'n', '-', 'C', 'l', 'a', 's', 's']
n
        
['P', 'h', 'o', 'n', '-', 'C', 'l', 'a', 's', 's']
n.pop(1,2)
        
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    n.pop(1,2)
TypeError: pop expected at most 1 argument, got 2
del n[1],[2]
        
SyntaxError: cannot delete literal
del n[1][2]
        
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    del n[1][2]
TypeError: 'str' object doesn't support item deletion
del n[1,2]
        
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    del n[1,2]
TypeError: list indices must be integers or slices, not tuple
n
        
['P', 'h', 'o', 'n', '-', 'C', 'l', 'a', 's', 's']
del n[1:9]
        
d
        
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
n
        
['P', 's']
n.append('!!!')
        
n
        
['P', 's', '!!!']
n.append([1,2])
        
n
        
['P', 's', '!!!', [1, 2]]
n.inset(11,'!!')
        
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    n.inset(11,'!!')
AttributeError: 'list' object has no attribute 'inset'. Did you mean: 'insert'?
n.insert(11,'!!')
        

n

n
        
['P', 's', '!!!', [1, 2], '!!']
n.insert(12,'!!!')
        
n
        
['P', 's', '!!!', [1, 2], '!!', '!!!']
print(len(n))
        
6
len(n)
        
6

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
aaaa
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 2, in <module>
    lena
NameError: name 'lena' is not defined. Did you mean: 'len'?

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
123123

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
123123123
9
print(a.count(1))
        
0
a
        
['1', '2', '3', '1', '2', '3', '1', '2', '3']
print(a.count('1'))
        
3
a.append(1)
        
a.count(1)
        
1
a
        
['1', '2', '3', '1', '2', '3', '1', '2', '3', 1]
len(a)
        
10
a=[1,2,3]
        
b=[4,5,6]
        
a+b
        
[1, 2, 3, 4, 5, 6]
a=[1,2,3]
        
b=a*3
        

b
        
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a=[1,2,3]
        
a*0
        
[]
c=a*0
        
c
        
[]
a=['a','b','c']
        
a*3
        
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
b
        
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a+b
        
['a', 'b', 'c', 1, 2, 3, 1, 2, 3, 1, 2, 3]
b=['z','y','x']
        
a*b
        
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'list'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
과일바구니
        
['사과', '수박', '바나나']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
['사과', '바나나', '망고', '포도']
포도

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
['수박', '바나나', '망고', '포도']
포도

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
n
        
[1, 3, 5, 7, 9]
sum(n)
        
25
min(n)
        
1
max(n)
        
9
print(sum(n)/len(n))
        
5.0
li[1,3,2,0]
        
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    li[1,3,2,0]
NameError: name 'li' is not defined
li=[1,3,2,0]
        
li[1,3,2,0]
        
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    li[1,3,2,0]
TypeError: list indices must be integers or slices, not tuple
li[1]
        
3
print(li[li[li[li[0]]]]])
   
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(li[li[li[li[0]]]])
   
1
a=[3,6,10,1,4,12,2]
   
a
   
[3, 6, 10, 1, 4, 12, 2]
print(a[-min(a))
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print(a[-min(a)])
      
2
print(max(a[1:4]))
      
10
n[2:6]
      
[5, 7, 9]
n=[2,11,5,7,6,8,20]
      
n[2:6]
      
[5, 7, 6, 8]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
시작 인덱스:2
끝 인덱스:6
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 5, in <module>
    print('최솟값:',min.n[a:a1])
AttributeError: 'builtin_function_or_method' object has no attribute 'n'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
시작 인덱스:2
끝 인덱스:6
최솟값: 5
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 6, in <module>
    print('최댓값:',max(n[a,a1]))
TypeError: list indices must be integers or slices, not tuple

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
시작 인덱스:2
끝 인덱스:6
최솟값: 5
최댓값: 20
합계: 46
평균: 9.2

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
22
44
77
[44]
a
      
22
A
      
[44]
n=[1,0,3,2,5,8,7,11,9]
      
n[::-1]
      
[9, 11, 7, 8, 5, 2, 3, 0, 1]
n.reverse90
      
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    n.reverse90
AttributeError: 'list' object has no attribute 'reverse90'. Did you mean: 'reverse'?
n.reverse()
      
n
      
[9, 11, 7, 8, 5, 2, 3, 0, 1]
n.sort()
      
n
      
[0, 1, 2, 3, 5, 7, 8, 9, 11]
n=sorted(n)
      

n
      
[0, 1, 2, 3, 5, 7, 8, 9, 11]
a=['a','d','b']
      
a.sort()
      
a
      
['a', 'b', 'd']
a=['안','녕','ㄱ','ㅎ']
      
a.sort()
      
a
      
['ㄱ', 'ㅎ', '녕', '안']
a=sorted(n)
      
a
      
[0, 1, 2, 3, 5, 7, 8, 9, 11]
n
      
[0, 1, 2, 3, 5, 7, 8, 9, 11]
b=[1,3,5,2,6,1,6]
      
a=sorted(b)
      
a
      
[1, 1, 2, 3, 5, 6, 6]
b
      
[1, 3, 5, 2, 6, 1, 6]
a
      
[1, 1, 2, 3, 5, 6, 6]
a.sort(reverse=True)
      
a
      
[6, 6, 5, 3, 2, 1, 1]
a=sorted(b,reverse=True)
      
a
      
[6, 6, 5, 3, 2, 1, 1]
b
      
[1, 3, 5, 2, 6, 1, 6]
c=[0,1,2,8,6]
      

a=c.sort
      
a
      
<built-in method sort of list object at 0x000001945AF21800>
c
      
[0, 1, 2, 8, 6]
a=c.sort()
      
a
      
a
      
c
      
[0, 1, 2, 6, 8]
a=sorted(c)
      
a
      
[0, 1, 2, 6, 8]
c
      
[0, 1, 2, 6, 8]
a=sorted(c,reverse=True)
      
a
      
[8, 6, 2, 1, 0]
v
c
      
[0, 1, 2, 6, 8]
n
      
[0, 1, 2, 3, 5, 7, 8, 9, 11]
n.sort(reverse=True)
      
n
      
[11, 9, 8, 7, 5, 3, 2, 1, 0]
n=sorted(n,reverse=True)
      
b
      
[1, 3, 5, 2, 6, 1, 6]
n
      
[11, 9, 8, 7, 5, 3, 2, 1, 0]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
[0, 1, 2, 3, 5, 8]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 3, in <module>
    c=a+b.sort
TypeError: can only concatenate list (not "builtin_function_or_method") to list

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
a
      
[1, 3, 5]
b
      
[2, 8, 0]
c
      
[0, 1, 2, 3, 5, 8]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
[0, 1, 2, 3, 5, 8]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
[11, 8, 5, 4, 3, 2]
a=[1,2,3,4,5]
      
a.remove(min(a))*2
      
Traceback (most recent call last):
  File "<pyshell#351>", line 1, in <module>
    a.remove(min(a))*2
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
(a.remove(min(a)))*2
      
Traceback (most recent call last):
  File "<pyshell#352>", line 1, in <module>
    (a.remove(min(a)))*2
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
첫 번째 숫자:
==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
첫 번째 숫자:17
두 번째 숫자:9
세 번째 숫자:25
네 번째 숫자:21
다섯 번째 숫자:29
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 6, in <module>
    x=sorted(a+b+c+d+e)
TypeError: 'int' object is not iterable

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
첫 번째 숫자:17
두 번째 숫자:9
세 번째 숫자:25
네 번째 숫자:21
다섯 번째 숫자:29
숫자 정렬: [9, 17, 21, 25, 29]
중간값: [21]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
첫 번째 숫자:17
두 번째 숫자:9
세 번째 숫자:21
네 번째 숫자:25
다섯 번째 숫자:29
숫자 정렬: [9, 17, 21, 25, 29]
25

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
첫 번째 숫자:17
두 번째 숫자:9
세 번째 숫자:25
네 번째 숫자:21
다섯 번째 숫자:29
숫자 정렬: [9, 17, 21, 25, 29]
중간값: 25

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
첫 번째 숫자:17
두 번째 숫자:9
세 번째 숫자:25
네 번째 숫자:21
다섯 번째 숫자:29
숫자 정렬: [9, 17, 21, 25, 29]
중간값: 21


==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
111227

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 4, in <module>
    A=int(A)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
[14, 910, 1516, 5678, 12345, 111213]
[111213, 12345, 5678, 1516, 910, 14]
111227

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
['21345']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
['2', '1', '3', '4', '5']
a='12345'.pslit()
      
Traceback (most recent call last):
  File "<pyshell#353>", line 1, in <module>
    a='12345'.pslit()
AttributeError: 'str' object has no attribute 'pslit'. Did you mean: 'rsplit'?
a='12345'.split()
      
a
      
['12345']
b='1 2345'.split()
      
b
      
['1', '2345']
c='123 45'.split()
      
c
      
['123', '45']
n=[1,2,3,4,5]
      
n=map(float,n)
      
n
      
<map object at 0x00000225630C2DA0>
print(n)
      
<map object at 0x00000225630C2DA0>
n
      
<map object at 0x00000225630C2DA0>
n=[1,2,3,4,5]
      
n=list(map(float,n))
      
print(n)
      
[1.0, 2.0, 3.0, 4.0, 5.0]
n=input('숫자 입력>>').split()
      
숫자 입력>>12
n
      
['12']
n=map(int,n)
      
n
      
<map object at 0x00000225630C2F50>
n=list(n)
      
n
      
[12]
n=input('숫자 입력>>').split()
      
숫자 입력>>12
n=list(map(int,n))
      
n
      
[12]
n=list(map(int,input('숫자 입력>>').split()))
      
숫자 입력>>21
n
      
[21]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
Republic
 Republic of Korea
do, Republic of Korea

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=int(input('숫자 10개 입력:')).split()
ValueError: invalid literal for int() with base 10: '1 2 3 4 5 6 7 8 9 10'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=int(input('숫자 10개 입력:')).split()
ValueError: invalid literal for int() with base 10: '1 2 3 4 5 6 7 8 9 10'
c
      
Traceback (most recent call last):
  File "<pyshell#379>", line 1, in <module>
    c
NameError: name 'c' is not defined

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=list(int(input('숫자 10개 입력:')).split())
ValueError: invalid literal for int() with base 10: '1 2 3 4 5 6 7 8 9 10'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=list(int(input('숫자 10개 입력:')))
ValueError: invalid literal for int() with base 10: '1 2 3 4 5 6 7 8 9 10'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
a
      
['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5', ' ', '6', ' ', '7', ' ', '8', ' ', '9', ' ', '1', '0']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
Traceback (most recent call last):
  File "C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py", line 1, in <module>
    a=list(input('숫자 10개 입력:')).split()
AttributeError: 'list' object has no attribute 'split'

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
a
      
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10

a
a
      
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
5.5

==== RESTART: C:/Users/hlabc/AppData/Local/Programs/Python/Python310/test.py ===
숫자 10개 입력:1 2 3 4 5 6 7 8 9 10
5.5
