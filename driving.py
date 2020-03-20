county = input("請輸入國家")
age = int(input("請輸入年齡"))

if county == "台灣":
    if age < 18:
        print("不能考駕照")
    else:
        print("妳可以考駕照")

elif county == "美國":
    if age < 16:
        print("不能考駕照")
    else:
        print("妳可以考駕照")
else:
    print("目前不支援此國家判定")
