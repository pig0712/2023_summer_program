# 완벽하지 않은 코드입니다.
import math
import os
import numpy as np

os.system("cls")

def f(x):
    x = a
    x[2] -= x[3]
    if (pow(x[1],2) - 4 * x[0] * x[2]) < 0:
        print("\n허근")

    elif (pow(x[1],2) - 4 * x[0] * x[2]) >= 0:
        print(- x[1] + math.sqrt(pow(x[1], 2) - 4 * x[0] * x[2]) / 2 * x[0], -x[1] + math.sqrt(pow(x[1], 2) - 4 * x[0] * x[2]) / 2 * x[0])

try:
    print("이 프로그램은 aX^2 + bX + C 의 근을 구하는 프로그램 입니다.")
    a = [int(input("%s차항 계수를 입력해 주세요.\n"%i)) for i in range(2,0,-1)] + [int(input("상수를 입력해 주세요\n"))] + [int(input("함수와 만나는 x절편을 적어주세요.\n"))]
    f(a)
except ValueError :
    print("잘못 입력하셨습니다.")