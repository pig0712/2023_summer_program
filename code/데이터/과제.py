import requests
import json
import pandas as pd
import os 

global i
global j

def save_csv():
  df = pd.concat(lst_rows, axis=1)
  df = df.T #행렬바꾸기
  df.to_csv('result.csv')

os.system("cls")

lst_rows = []

page_no = 1
page_size = 366 

my_url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
api_key = 'sU1jMjDNWShKrOPsKYN09F+8fHfYjRseeXvD6I2WIU9UDh2A5bAKHQjLoVhnpCmwu4aE+QlQ0Zzkc/AqisS8yA=='

try:
  stD = [str(i)+"0101" for i in range(1920, 2020)]
  enD = [str(i)+"0101" for i in range(1921, 2021)]

  for j in range(100):

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

      resultCode = html['response']['header']['resultCode']
      if resultCode != '00':
        break

      items = html['response']['body']['items']['item']
      for item in items:
        lst_rows.append(pd.Series(item))

      print("%s.%s"%(j,i))

    print("[%s]"%j)
  list(set(lst_rows))
  if enD[j] == "20200101":
    save_csv()

except:
  save_csv()