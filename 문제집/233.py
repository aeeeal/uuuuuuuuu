c=-1
A=[]
def make_list(a):
    b=len(a)
    c=-1
    for i in range(b):
        c+=1
        A.append(a[c])
    return A

print(make_list("abcd"))