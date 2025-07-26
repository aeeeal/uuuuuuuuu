a,b=input(">>입력:").split()
if b=='달러':
    print(str(int(a)*1167)+'원')
elif b=='엔':
    print(str(int(a)*1.096)+'원')
elif b=='유로':
    print(str(int(a)*1268)+'원')
elif b=='위안':
    print(str(int(a)*171)+'원')