import csv

def getProfit(target_price, purchase_price, quantity):
    return (target_price - purchase_price) * quantity
def getProfitRate(target_price, purchase_price):
    if(purchase_price == 0):
        return
    return ((target_price / purchase_price) - 1) * 100

file = open("./myvenv/ch10_file_io/file_io_test/mystock.csv", "r", encoding="utf-8-sig")
reader = list(csv .reader(file))
for row in reader[1:]:
    print(f"{row[0]} {getProfit(int(row[3]), int(row[1]), int(row[2])):.2f}% {getProfitRate(int(row[3]), int(row[1])):.2f}%")


file.close()