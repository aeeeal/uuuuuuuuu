A=[]
def pickup_even(a):
    for i in a:
        if i%2==0:
            A.append(i)
    return A
print(pickup_even([3,4,5,6,7,8]))