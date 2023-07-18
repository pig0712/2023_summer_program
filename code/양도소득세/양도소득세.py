import os

class CGT:

    tr = None # 양도가격
    ac = None # 취득가격
    td = None # 양도차액
    aa = None # 과세금액
    cgt = None # 양도소득세
    c = None # 판단 값 저장

    data = {
    "과표" : [
        "1,400만원 이하",
        "5,000만원 이하",
        "8,800만원 이하",
        "1.5억원 이하",
        "3억원 이하",
        "5억원 이하",
        "10억원 이하",
        "10억원 초과"
        ],

    "세율" : [6,15,24,35,38,40,42,45],

    "누진공제" :[
        0,
        126,
        576,
        1544,
        1994,
        2594,
        3594,
        6594
    ]
} 




    def __init__(self): # 입력 메소드
        os.system("cls")
        print("이 프로그램은 23년 기준으로 만들었습니다. \n만원 단위로 입력해주세요.\n")
        self.tr = int(input("양도가격을 입력해 주세요: "))
        self.ac = int(input("취득가격을 입력해 주세요: "))

    def g(self): # 세율 판단 메소드
        self.td = self.tr - self.ac # 양도차액 계산
        self.aa = self.td - 250 # 과세금액 계산

        if self.aa <= 1400:
            self.c = 0

        elif self.aa <= 5000:
            self.c = 1

        elif self.aa <= 8800:
            self.c = 2
        
        elif self.aa <= 15000:
            self.c = 3

        elif self.aa <= 30000:
            self.c = 4

        elif self.aa <= 50000:
            self.c = 5

        elif self.aa <= 100000:
            self.c = 6

        elif self.aa > 100000:
            self.c = 7

    def ct(self): # 계산 메소드
        self.cgt = self.aa * self.data["세율"][self.c]/100 - self.data["누진공제"][self.c]# 양도소득세 계산

a = CGT()
a.g()
a.ct()
os.system("cls")
print("#"*50)
print("\n양도가격: %s만원"%a.tr)
print("취득가격: %s만원"%a.ac)
print("양도차액: %s만원"%a.td)
print("\n과표: %s"%a.data["과표"][a.c])
print("과세금액: %s만원"%a.aa)
print("양도소득세: %s만원"%a.cgt) 
print("\n납부해야할 금액은 %s만원 입니다.\n"%a.cgt)
print("#"*50)
