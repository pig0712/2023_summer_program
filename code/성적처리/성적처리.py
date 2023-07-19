import os
import pprint as pt

class GRADES:
    file = None

    def __init__(self):
        os.system("cls")
        # ft = input("파일 경로를 입력해주세요: \n")
        filet = "C:/Users/koll2/OneDrive/2023_summer_program/code/성적처리/sungjuk3.csv"
        files = open(filet,"r", encoding="utf-8")
        self.file = files.read()

        if self.file[2] == "-":
            self.file = self.file.replace(" ","")
            self.file = self.file.replace("--","-")

        self.file = list(self.file.split("\n"))
        for i in range(1, len(self.file)):

            if self.file[i][-1] == "-":
                self.file[i] = str(list(self.file).pop())   

            if len(self.file[i]) == 15:
                self.file[i] += "-00"

            if len(self.file[i]) != 18:
                print("%s번에 잘못된 데이터값이 있습니다. "%i)
                continue
        
            if self.file[i][3] == "\t":
                self.file[i] = list(self.file[i].split("\t"))

            elif self.file[i][3] == ",":
                self.file[i] = list(self.file[i].split(","))

            elif self.file[i][3] == "-":
                self.file[i] = list(self.file[i].split("-"))


            tot = int(self.file[i][3]) + int(self.file[i][4]) + int(self.file[i][5])
            print ("번호: %s 이름: %s 성별: %s 국어: %s 영어: %s 수학: %s 총 점수: %s 평균: %s"\
                   %(self.file[i][0], self.file[i][1], self.file[i][2], self.file[i][3] , self.file[i][4], self.file[i][5], tot, round(tot/3,2)))
            
a = GRADES()