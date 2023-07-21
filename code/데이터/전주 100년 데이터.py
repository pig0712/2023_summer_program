import requests
import json
import pandas as pd
import os 

# 왜 적어둔거지 이거
global i
global j


# 저장 하는 로직을 함수로 만듬
def save_csv():
  df = pd.concat(lst_rows, axis=1)
  df = df.T #행렬바꾸기
  df.to_csv('result.csv')

# 콘솔창 더러워지는거 보기 싫어서 넣어둠 
os.system("cls")


# 
lst_rows = []

page_no = 1
page_size = 366 

my_url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
api_key = 'sU1jMjDNWShKrOPsKYN09F+8fHfYjRseeXvD6I2WIU9UDh2A5bAKHQjLoVhnpCmwu4aE+QlQ0Zzkc/AqisS8yA=='

try:
  stD = [str(i)+"0101" for i in range(1920, 2020)]
  enD = [str(i)+"0101" for i in range(1921, 2021)]

  for j in range(len(stD)):

    params = {
        'ServiceKey' : api_key ,
        'numOfRows' : page_size,
        'PageNo' : page_no,
        'dataType' : 'JSON',
        'dataCd' : 'ASOS',
        'dateCd' : 'DAY',
        'startDt' : stD[j], 
        'endDt' : enD[j],
        'stnIds' : '146'
    }

    for i in range(1, 2):
      params['pageNo'] = i
      response = requests.get(my_url, params=params) 
      html = json.loads(response.text)

      # 결과 코드가 00 이 아니면 for 문 중지 
      resultCode = html['response']['header']['resultCode']
      if resultCode != '00':
        break
      
      # 불러온 데이터 lst_row에 넣기
      items = html['response']['body']['items']['item']
      for item in items:
        lst_rows.append(pd.Series(item))

      # 얼마나 뽑혔는지 확인
      print("%s.%s"%(j,i))

    # 얼마나 뽑혔는지 확인
    print("[%s]"%j)
  
  # 리스트 중복 제거
  list(set(lst_rows))

  # 2020년 01월 01일 까지 전부 실행 시키면 저장 .
  if enD[j] == "20200101":
    save_csv()

except:
  save_csv()