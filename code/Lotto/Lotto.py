import numpy as np
import random as rd
import os 


class Lotto:
    sg = []
    def __init__(self):
        os.system("cls")
        pass

    def Lotto_1(self):
        for i in range(6):
            self.sg.append(np.random.randint(1,46))
        self.sg.sort()
        print(self.sg)
        

l = Lotto()
l.Lotto_1()

