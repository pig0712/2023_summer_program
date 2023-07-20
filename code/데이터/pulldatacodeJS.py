# 국가철도공단_수도권5호선_화장실 데이터를 기준으로 만들었습니다.
# https://www.data.go.kr/data/15041258/fileData.do
# 활용 신청 하시고 해보세요. 

import pandas as pd # 판다스를 사용하기 위해 불러오고 pandas. 으로 쓰기 귀찮으니 as pd 라고 뒤에 적어줌 그럼 pd. 으로 판다스 사용 가능 
import requests as rq 
import json as js # json 형태로 
import csv  


# 내 key : 디코딩 키로 사용해야함
Decoding_key = "sU1jMjDNWShKrOPsKYN09F+8fHfYjRseeXvD6I2WIU9UDh2A5bAKHQjLoVhnpCmwu4aE+QlQ0Zzkc/AqisS8yA=="
# Decoding_key = "내 api 키"

# url 적기 : url 개수가 데이터마다 다름 
Base_url = "api.odcloud.kr/api"
url = "	http://infuser.odcloud.kr/oas/docs?namespace=15041258/v1"

# data type : 내가 불러올 데이터 타입 
data = "JSON"


# 데이터마다 넣어야 할 항목이 다름 
params = {

}

# 어어 언젠가 할게요 