pd_01 = "a123456"
i = 3
while i > 0:
	i -= 1
    pd = input("請輸入密碼:")
    if pd == pd_01:
        print("密碼正確登入中")
        break
    else:
        print("密碼錯誤")
        if i > 0:
        	print("剩餘嘗試%d次" % (i))
        else
        	print("密碼連續錯誤請15分後再試")
