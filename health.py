#個人資料輸入
name = input("請輸入姓名:")
age = float(input("請輸入年齡:"))
hight = float(input("請輸入身高/公分:"))
kg = float(input("請輸入體重/kg:"))
bmi = kg / ((hight/100) ** 2)

name_name = "姓名:"
age_age = "年齡:"
hight_hight = "身高:"
kg_kg = "體重:"
bmi_bmi = "BMI:"

print("%s%s"%(name_name,name))
print("%s%.0f歲"%(age_age,age))
print("%s%.0f公分"%(hight_hight,hight))
print("%s%.2f公斤"%(kg_kg,kg))
print("%s%.2f"%(bmi_bmi,bmi))

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
