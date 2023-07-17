# v1.0 (2023-07-17)
# https://github.com/pig0712/2023_summer_program
# 2023_summer_program\code\ISBN

class ISBN:
    isbn = "8956741891"

    def __init__(self):
        pass


    # 2007년 이전 (10자리) ISBN
    def before_ISBN(self):
        add = 0
        mp = 10
        for i in range(10):
            add += int(self.isbn[i]) * mp
            mp -= 1
        
        if add%11 == 0:
            print("올바른 ISBN 입니다.")
        else:
            print("올바르지 않은 ISBN 입니다.")


    def before_ISBN_checkmark(self):
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
            

a = ISBN()
a.before_ISBN()


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