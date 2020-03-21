while True:
    age = input("請輸入年齡:")
    try:
        age = int(age)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('年齡請輸入阿拉伯數字\n')
        continue
while True:
    county = input("結束請輸入exit\n請輸入國家:")
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
    elif county == "exit":
        print("程式已結束")
        break
    else:
        print("尚未支援此國家判定")
        continue
