c=0
def print_score(a):
    c=0
    for i in a:
        c+=i
    print(c/len(a))
print_score([1,2,3])