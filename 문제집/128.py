a=input('주민등록번호')
if int(a[8])==0 and int(a[9])<9:
    print('서울 입니다.')
else:
    print('서울이 아닙니다')