import pandas as pd # 판다스를 사용하기 위한 
import requests as rq
import xml
import csv  


# 내 key : 디코딩 키로 사용해야함
Decoding_key = "sU1jMjDNWShKrOPsKYN09F+8fHfYjRseeXvD6I2WIU9UDh2A5bAKHQjLoVhnpCmwu4aE+QlQ0Zzkc/AqisS8yA=="

# url 적기 : url 개수가 데이터마다 다름 
Base_url = "api.odcloud.kr/api"
url = "	http://infuser.odcloud.kr/oas/docs?namespace=15041258/v1"

# data type : 내가 불러올 데이터 타입 
data = "XML"

# 어어 언젠가 할게요 