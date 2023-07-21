import requests
import bs4
import pandas as pd

# 서비스 키를 직접 입력하거나, 입력받을 수 있도록 코드를 수정해주세요.
ServiceKey = '13CPb3malGQVstiiJS8MLDEjKKWj0Y0Xv3Lg3vL0r0KQ8BRF2PMjbfOtiXnmHAspvoADNHiwd2pogCREd8ERZg=='

pageNo = '1'
numOfRows = '10'
resultType = 'xml'

my_url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params = {
    'ServiceKey': ServiceKey,
    'pageNo': pageNo,
    'numOfRows': numOfRows,
    'resultType': resultType
}

list_rows = []  # 날씨 데이터를 저장할 리스트를 생성합니다.

while True:
    response = requests.get(my_url, params=params, verify=False)
    content = response.text
    xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')
    rows = xml_obj.findAll('item')

    if len(rows) <= 0:
        break
        print('Nan')

    for row in rows:
        d = {}
        for r in row.contents:
            if r.name is not None:
                d[r.name] = r.text
        list_rows.append(pd.Series(d))

   
    pageNo = str(int(pageNo) + 1)
    params['pageNo'] = pageNo


df = pd.concat(list_rows, axis=1).T


df.to_csv('./기상청_지상(종관, ASOS) 일자료 조회서비스.csv', index=False)