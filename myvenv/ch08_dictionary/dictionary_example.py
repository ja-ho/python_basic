stock_a = {"삼성전자": 82000, "엘지전자": 150000}

stock_b = {
    "삼성전자": [82000, 70000, 60000],
    "엘지전자": [150000, 140000, 120000]
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81000
    }
}

# print(stock_a)
# print(stock_b)
# print(stock_c)

# dictionary 개념
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a["삼성전자"])

# 딕셔너리 삭제하기
del stock_a["엘지전자"]
print(stock_a)

stock_d = {
    "samsung" : 8200,
    "hinyx" : 1203,
    "naver": 500,
    "kakao": 70
}

#items() : 키와 데이터 상
print(stock_d.items())

for item in stock_d.items():
    print(item) # tuple 형태로 되어 있음 item[0]은 key, item[1] 은 value

# keys() : 키
for key in stock_d.keys():
    print(key)

for value in stock_d.values():
    print(data)

# values() : value