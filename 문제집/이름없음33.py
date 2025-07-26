# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
a=0
for i in range(11):
    if i%2==1:
        a+=i
print(a)