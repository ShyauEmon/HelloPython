f = float(input("請輸入華氏溫度°F:"))
c = float(input("請輸入攝氏溫度°C:"))

print("%.2f°F等於%.2f°C" % (f, ((f - 32) * 5 / 9)))
print("%.2f°C等於%.2f°F" % (c, (c * 1.8 + 32)))