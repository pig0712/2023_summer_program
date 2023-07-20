import requests
import bs4
import pandas as pd
from lxml import html


url = "http://apis.data.go.kr/1360000/WthrWrnInfoService"
my_key = "sU1jMjDNWShKrOPsKYN09F+8fHfYjRseeXvD6I2WIU9UDh2A5bAKHQjLoVhnpCmwu4aE+QlQ0Zzkc/AqisS8yA=="

params = {
'ServiceKey' : my_key,
'pageNo': "",
'numOfRows': 20,
'dataType' : 'XML',
"stnId" : 184,
"fromTmFc" : 20170601,
"toTmFc" : 	20170630

}

lst_rows = []

for i in range(1, 10):
    params['pageNo'] = i

    response = requests.get(url, params=params, verify=False) # verify설정 추가
    content = response.text
    xml_obj = bs4.BeautifulSoup(content, 'lxml-xml')

    if len(lst_rows) != 0:
        resultCode = int(xml_obj.findAll('resultCode').pop().text)
        resultMsg = (xml_obj.findAll('resultMsg').pop().text)

    if resultCode != 0:
        print('Error')
        print(f'resultMsg : {resultMsg}')
        break
        

    rows = xml_obj.findAll('list')
    if len(rows) <= 0:
        break

    for r in rows:
        dict_row = dict()
        for t in r:
            if t.name is not None:
                dict_row[t.name] = t.string

        lst_rows.append(pd.Series(dict_row))
    print(i)
    
df = pd.concat(lst_rows, axis=1)
# df = pd.DataFrame(lst_rows)
df = df.T
df.to_csv('JeonJuParking1.csv')