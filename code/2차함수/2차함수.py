import math
import os

os.system("cls")

def f(x):
    x = a
    if (pow(x[1],2) - 4 * x[0] * x[2]) < 0:
        print("\n허근")

    elif (pow(x[1],2) - 4 * x[0] * x[2]) >= 0:
        print(- x[1] + math.sqrt(pow(x[1], 2) - 4 * x[0] * x[2]) / 2 * x[0], -x[1] + math.sqrt(pow(x[1], 2) - 4 * x[0] * x[2]) / 2 * x[0])


try:
    a = [int(input("%s차항 계수를 입력해 주세요.\n"%i)) for i in range(2,0,-1)] + [int(input("상수를 입력해 주세요\n"))]
    f(a)
except ValueError :
    print("정수만 입력해 주세요.")

