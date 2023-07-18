import numpy as np
import random as rd
import os 


class Lotto:
    sg = []
    sg2 = None
    def __init__(self):
        os.system("cls")
        pass

    def Lotto_1(self): # 중복 문제
        for i in range(6):
            self.sg.append(np.random.randint(1,46))
        self.sg.sort()
        print(self.sg) 
        
    def Lotto_2(self): # 중복 문제 
        for i in range(6):
            self.sg.append(rd.randint(1,46))
        self.sg.sort()
        print(self.sg)
    
    def Lotto_3(self): # 중복문제 해결 1
        self.sg = [i for i in range(1,46)]
        self.sg2 = rd.sample(self.sg,6)
        self.sg2.sort()
        print(self.sg2)

    def Lotto_4(self): # 중복문제 해결 2
        self.sg = []
        ct = 0
        while True:
            a = rd.randint(1,46)
            if self.sg.count(a) == 1:
                continue
            else :
                self.sg.append(a)
                ct += 1

            if ct == 6:
                break
                
        self.sg.sort()
        print(self.sg)





l = Lotto()
l.Lotto_4()

