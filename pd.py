pd_01 = "a1234567"
a = 3
while a > 0:
    pd = input("請輸入密碼可輸入%d次:" %a)
    if pd == pd_01:
        print("密碼正確登入中")
        break
    elif pd != pd_01:
        print("密碼錯誤剩餘嘗試%d次" % (a-1))
        a -= 1

if a == 0:
    print("密碼連續錯誤請15分後再試")
