import os 
os.system("cls") # 콘솔창 정리
while True:
    print ("예시: 123456-1234567")
    jm = input("주민등록번호 입력: ")
    if len(jm) == 14:
        break

    else:
        os.system("cls") 
        print("주민등록번호를 다시 입력해 주세요\n")

os.system("cls") 

j = jm[0:6]+jm[7:14]
ad = [2,3,4,5,6,7,8,9,2,3,4,5]
a = 0
de = 11
for i in ad:
    a += int(j[de]) * i
    de -= 1

if a%11 == int(j[len(j)-1]):
    print("검증된 주민등록번호 입니다.")
else:
    print("검증되지 않은 주민등록번호 입니다.")