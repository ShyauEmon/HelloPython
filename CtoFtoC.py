f = float(input("請輸入華氏溫度:"))
c = float(input("請輸入攝氏溫度:"))

print("攝氏溫度為:%.2f" % ((f - 32) * 5 / 9))
print("華氏溫度為:%.2f" % (c * 1.8 + 32))