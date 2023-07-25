# 랜덤 모듈을 사용해서 정렬할 샘플 만들기
import random as rd
sp = [i for i in range(10)] # 중복 x
# sp = [1,1,2,2,3,3,4,4,5,5] # 중복 o
rd.shuffle(sp)

# 선택 정렬 알고리즘 (중복 x)
print("선택 정렬 알고리즘 : %s\n"%(sp))

for i in range(len(sp)-1): # 리스트 범위 밖을 탐색하는 에러 방지를 위해 0 ~ 8 까지만 탐색 / i+1 으로 index 9까지 탐색 가능
    st = None
    if sp[i] < sp[i+1]:


print(sp)

# st = 1