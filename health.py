# 個人資料輸入
name = input("請輸入姓名:")
while True:
    age = input("請輸入年齡:")
    height = input("請輸入身高/公分:")
    kg = input("請輸入體重/kg:")
    try:
        age = float(age)
        height = float(height)
        kg = float(kg)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('年齡,身高,體重,請輸入阿拉伯數字\n')
        continue
bmi = kg / ((height/100) ** 2)
print("姓名:%s" % name)
print("年齡:%.0f歲" % age)
print("身高:%.0f公分" % height)
print("體重:%.2f公斤" % kg)
print("BMI:%.2f" % bmi)
if 18.5 <= bmi < 24:
    print("你的身體很健康")
elif 24 <= bmi < 27:
    print("有肥胖傾向")
elif 27 <= bmi < 30:
    print("輕度肥胖")
elif 30 <= bmi < 35:
    print("中度肥胖")
elif bmi >= 35:
    print("重度肥胖")
else:
    print("體重過輕")
