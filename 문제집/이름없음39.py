a=0
my_list=[100,200,400,800]
for i in my_list:
    if i==100:
        a=i
        continue
    print(i-a)
    a=i