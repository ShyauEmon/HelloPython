while True:
    f = input("請輸入華氏溫度°F:")
    c = input("請輸入攝氏溫度°C:")
    try:
        f = float(f)
        c = float(c)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('請輸入阿拉伯數字\n')
        continue
print("%.2f°F等於%.2f°C" % (f, ((f - 32) * 5 / 9)))
print("%.2f°C等於%.2f°F" % (c, (c * 1.8 + 32)))
