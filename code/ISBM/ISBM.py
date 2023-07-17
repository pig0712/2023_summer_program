# v1.0 (2023-07-17)
# https://github.com/pig0712/2023_summer_program
# 2023_summer_program\code\ISBN

import os
os.system("cls") # 콘솔창 정리

class ISBN:
    ib = None
    isbn = None
    addmark = None
    year = None

    def __init__(self):
        self.year = int(input("출판년도 입력 : "))
        os.system("cls")

        while True:
            if self.year < 2007:
                print("ISBM 입력 예시: 89-7044-350-9 (부가기호 x)")
                print("ISBM 입력 예시: 89-7044-350-9 03400 (부가기호 o)\n")

            elif self.year >= 2007:
                print("ISBM 입력 예시: 978-89-954321-0-5 (부가기호 x)")
                print("ISBM 입력 예시: 978-89-954321-0-5 03810 (부가기호 o)\n")
            self.ib = input("ISBM 입력: ")

            if self.year < 2007:
                if len(self.ib) in [13,19]:
                    if len(self.ib) == 13:
                        self.isbn = self.ib[0:2]+self.ib[3:7]+self.ib[8:11]+self.ib[12]
                        self.addmark = "없음"

                    elif len(self.ib) == 19: 
                        self.isbn = self.ib[0:2]+self.ib[3:7]+self.ib[8:11]+self.ib[12]
                        self.addmark = self.ib[14:20]
                        
                    break
                else:
                    os.system("cls")
                    print("ISBN을 다시 입력해 주세요.\n")

            elif self.year >= 2007:
                if len(self.ib) in [17,23]:
                    if len(self.ib) == 17:
                        self.isbn = self.ib[0:3]+self.ib[4:6]+self.ib[7:13]+self.ib[14]+self.ib[16]
                        self.addmark = "없음"

                    elif len(self.ib) == 23: 
                        self.isbn = self.ib[0:3]+self.ib[4:6]+self.ib[7:13]+self.ib[14]+self.ib[16]
                        self.addmark = self.ib[18:24]
                    break
                else:
                    print("_"*50)
                    print("ISBN을 다시 입력해 주세요.\n")

        self.ISBN_UI()
            
    def ISBN_UI(self):
        os.system("cls")    
        print("#"*50+"\n")
        print("10자리 ISBN"*(self.year < 2007) + "13자리 ISBN"*(self.year >= 2007))
        if self.year < 2007:
            print("ISBN : %s"%self.ib)
        elif self.year >= 2007:
            print("ISBN : %s"%self.ib)

        print("ISBN : %s"%self.isbn)
        print("부가기호 : %s\n"%self.addmark)
        print("1. ISBN 유효성 검사")
        print("2. 체크기호 유효성 검사")
        print("3. 부가기호 분석")
        print("4. ISBN 세부정보")
        print("5. 프로그램 종료\n")
        print("#"*50)

        chs = int(input("선택: "))

        # ISBN 유효성 검사
        if chs == 1:
            if self.year < 2007:
                os.system("cls")
                self.before_ISBN()
            elif self.year >= 2007:
                os.system("cls")
                self.after_ISBN()
            self.ISBN_UI()

        # 체크기호 유효성 검사
        elif chs == 2:
            if self.year < 2007:
                os.system("cls")
                self.before_ISBN_checkmark()
                
            elif self.year >= 2007:
                os.system("cls")
                self.after_ISBN_checkmark()
            self.ISBN_UI()

        # 부가기호 분석
        elif chs == 3:
            self.ISBN_UI()
            pass 

        # ISBN 세부정보        
        elif chs == 4:
            self.ISBN_UI()
            pass

        # 프로그램 종료
        elif chs == 5:
            os.system("cls")
            print("프로그램이 종료 되었습니다.")
            exit()

    # 2007년 이전 (10자리) ISBN (체크기호 10은 소문자x로 표시)
    def before_ISBN(self):
        add = 0
        mp = 10
        if self.isbn[len(self.isbn)-1] == "x":
            for i in range(len(self.isbn)-1):
                add += int(self.isbn[i]) * mp
                mp -= 1
            add += 10 # 마지막 체크기호 x는 10 
            if add%11 == 0:
                os.system("cls")
                print("올바른 ISBN 입니다.")
            else:
                os.system("cls")
                print("올바르지 않은 ISBN 입니다.")

        else:
            for i in range(len(self.isbn)):
                add += int(self.isbn[i]) * mp
                mp -= 1
                        
            if add%11 == 0:
                os.system("cls")
                print("올바른 ISBN 입니다.")
            else:
                os.system("cls")
                print("올바르지 않은 ISBN 입니다.")

        print("")        
         


    # 2007년 이전 (10자리) 체크기호 (체크기호 10은 소문자x로 표시)
    def before_ISBN_checkmark(self):
        add = 0
        mp = 10
        if self.isbn[len(self.isbn)-1] == "x":
            for i in range(len(self.isbn)-1):
                add += int(self.isbn[i]) * mp
                mp -= 1 
            chk = 11 - (add%11)
            if  ("x" == self.isbn[len(self.isbn)-1]) and (10 == chk):
                print("올바른 체크기호 입니다.")
            else:
                print("올바르지 않은 체크기호 입니다.")
        else:
            for i in range(len(self.isbn)-1):
                add += int(self.isbn[i]) * mp
                mp -= 1 

            chk = 11 - (add%11)
            if chk == int(self.isbn[len(self.isbn)-1]):
                print("올바른 체크기호 입니다.")
            else:
                print("올바르지 않은 체크기호 입니다.")

        

    # 2007년 이전 (10자리) 부가기호
    def before_ISBN_addmark(self):
        pass

    # 2007년 이후 (13자리) ISBN
    def after_ISBN(self):
        add = 0
        for i in range(len(self.isbn)):
            if i%2 == 0:
                add += int(self.isbn[i]) * 1
            elif i%2 == 1:
                add += int(self.isbn[i]) * 3
        if add%10 == 0:
            print("올바른 ISBN 입니다.")
        else:
            print("올바르지 않은 ISBN 입니다.")

        

    # 2007년 이후 (13자리) 체크기호
    def after_ISBN_checkmark(self):
        add = 0
        for i in range(len(self.isbn)-1):
            if i%2 == 0:
                add += int(self.isbn[i]) * 1
            elif i%2 == 1:
                add += int(self.isbn[i]) * 3

        chk = 10 - (add%10)
        if chk == int(self.isbn[len(self.isbn)-1]):
            print("올바른 체크기호 입니다.")
        else:
            print("올바르지 않은 체크기호 입니다.")
            
        

    # 2007년 이후 (13자리) 부가기호
    def after_ISBN_addmark(self):
        pass

a = ISBN()

# os.system("cls") # 나중에 ui 만들떄 사용

# 13자리 2가지 차이 000 , 000

# [ISBN 10자리]
# 89 - 5674 - 189 - 1
# 1) 89 -> 출판 국가 또는 언어 번호
# 2) 5674 -> 출판사 고유번호
# 3) 189 -> 출판사에서 책에 붙인 번호(임의로 붙임)
# 4) 1 -> 체크 기호
# --
# 1)  첫 번째 숫자는 10, 두 번째 숫자는 9, 세 번째 숫자는 8, ... 열 번째 숫자는 1을 곱합니다.
# 2)  각 곱셈의 결과를 모두 더합니다.
# 3) 최종 결과가 11의 배수이면 올바른 ISBN 입니다.

# ISBN 코드의 유효성을 검증하는 방법은 ISBN 코드 9자리 숫자에 가중치 10,9,8,7 .. 3,2를 각각 곱해 값을 더하고
# 가중치의 합을 11으로 나누어 나머지를 구하며 11에서 나머지를 뺀 값이 체크기호가 되며, 나머지가 0인 경우
# 체크기호가 0이 된다. 그리고 나머지가 10인 경우 체크기호는 x가 된다.



# [ISBN 13자리]
# 978 - 89 - 94567 - 67 - 9
# 1) 978 -> 접두어 (978 또는 979)
# 2) 89 -> 출판 국가 또는 언어 번호
# 3) 94567 -> 출판사 번호
# 4) 67 -> 항목 번호
# 5) 9 -> 체크 기호
# -- 
# 1) 첫 번째 숫자는 1, 두 번째 숫자는 3, 세 번째 숫자는 1, 네 번째 숫자는 3, ... 마지막 숫자는 1을 곱합니다.
# 2) 각 곱셈의 결과를 모두 더합니다.
# 3) 최종 결과가 10의 배수이면 올바른 ISBN 입니다.

# ISBN 코드의 유효성을 검증하는 방법은 ISBN 코드 12자리 숫자에 가중치 1과 3을 번갈아 곱해 값을 더하고
# 가중치의 합을 10으로 나누어 나머지를 구하며 10에서 나머지를 뺀 값이 체크기호가 되며, 나머지가 0인 경우
# 체크기호가 0이 된다.


# 민교수님 말씀처럼 철두철미하게. #