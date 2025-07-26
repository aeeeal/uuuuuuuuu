a,b,c=input('휴대전화 번호 입력').split('-')
if a=='011':
    print('당신은 SKT 사용자입니다.')
elif a=='016':
    print('당신은 KT 사용자입니다.')
elif a=='019':
    print('당신은 LGU 사용자입니다.')
else:
    print('알수없음')
    
    