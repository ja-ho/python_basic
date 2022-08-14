# 시퀀스 자료형

# 키와 데이터를 가지고 있는 사전형 자료형

# 키와 밸류값으로 데이터를 다룰 때 필요

# 딕셔너리 = {키1: 데이터, 키2: 데이터}

stock ={"samsung" : 82000, "LG" : 150000}

stocks = {
    "samsung" : [80000, 70000, 60000],
    "LG" : [150000, 140000, 120000]
}

print(stocks["samsung"])

stock["samsung"] = 50000

del stock["LG"]

print(stock)

# 키와 데이터 쌍
print(stock.items())

# 키
print(stock.keys())

# 데이터
print(stock.values())

