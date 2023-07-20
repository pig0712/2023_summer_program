import requests
import xml
import pandas as pd
from bs4 import BeautifulSoup as BS
import pprint

# url 생성
base_url = "http://apis.data.go.kr/1360000/WthrWrnInfoService"
my_key = "sU1jMjDNWShKrOPsKYN09F+8fHfYjRseeXvD6I2WIU9UDh2A5bAKHQjLoVhnpCmwu4aE+QlQ0Zzkc/AqisS8yA=="

page_no = 0
rows_no = 1

lst_rows = []

# 페이지 범위 지정
for i in range(1, 2):
  page_no = i
  params = {
    'ServiceKey' : my_key,
    'pageNo': i,
    'numOfRows': 20,
    'dataType' : 'XML',
    "stnId" : 184,
    "fromTmFc" : 	20170601,
    "toTmFc" : 	20170630

  }

  # 서버에 응답 요청하기
  response = requests.get(base_url, params=params)
  contents = response.text

  # 데이터 파싱하기
  soup = BS(contents,'lxml-xml')
  rows = soup.findAll('list')

  # 행 단위 파싱
  for row in rows:
    dict_row = dict()
    # 행의 콘텐츠 파싱
    for rows_c in row.contents:
      if rows_c.name is not None:
        dict_row[rows_c.name] = rows_c.text
      else:
        break

    # 콘텐츠를 행 단위로 저장(dict 형식)
    lst_rows.append(pd.Series(dict_row))
  print(i)

# 파싱 데이터를 판다스 데이터프레임 형식으로 바꾸기
df = pd.concat(lst_rows, axis=1)
df = df.T

# 저장하기
df.to_csv('noungsuri.csv')
