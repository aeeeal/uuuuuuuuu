# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
def print_5xn(string):
    string=list(string)
    for i in range(0,len(string)):
        print(string[i],end='')
        if i==4:
            print('')
        if i%5==0 and i!=0 and i!=5:
            print('')
print_5xn("아이엠어보이유알어걸")

