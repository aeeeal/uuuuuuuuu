print('fruit=["사과","포도","홍시"]')
a=input('>> 좋아하는 과일은?')
if a=='사과' or a=='포도' or a=='홍시':
    print('정답입니다.')
else:
    print('오답입니다.')
    
    
# 다른 방법
fruit = ['사과','포도','홍시']
flagVariable = False # flag 변수란, 보통 반복문에서 특정 "조건"이 만족하는 지 확인하기 위해 사용되는 변수이다. 마치 달리기를 하면서 1등이 들어왔을 때 심판이 깃발을 드는 행위와 비슷하다. 사람이 도착했음을 알리기
# 위해 깃발을 든 것(False->True 변경)
for f in fruit:
    if f==a:
        flagVariable=True
        break
if flagVariable:
    print("정답입니다")
else:
    print("오답입니다")
    