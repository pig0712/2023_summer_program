import os

class GD: # grades
    name = None
    kor = None
    eng = None
    mat = None
    tot = None

    def __init__(self):
        self.name = input("이름 입력: ")
        self.kor = int(input("국어 입력: "))
        self.eng = int(input("영어 입력: "))
        self.mat = int(input("수학 입력: "))
        self.ca()

    def ca(self):
        self.tot = self.kor + self.eng + self.mat
os.system("cls")
a = GD()
os.system("cls")
print("총점: %s"%a.tot)
print("평점: %s"%(a.tot/3))