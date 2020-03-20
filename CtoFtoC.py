f = float(input("請輸入°F:"))
c = float(input("請輸入°C:"))

print("°C為:%.2f" % ((f - 32) * 5 / 9))
print("°F為:%.2f" % (c * 1.8 + 32))