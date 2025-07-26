def print_mxn(a,b):
    d=len(a)//b
    for i in range(d+1):
        print(a[i*b:b*i+b])
    return ''
print(print_mxn('아이엠어보이유알어걸',))