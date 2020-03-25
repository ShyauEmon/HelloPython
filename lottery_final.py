import random
lottery = []
i = 0
while True:
    groups = input("請輸入要抽幾組號碼:")  # 此為你想要幾組電腦選號
    quantity = input("請輸入總球數:")  # 此為你想玩哪總例如:大樂透為為49個號碼就輸入"49"
    ball = input("請輸入抽出幾球:")  # 此為你玩的彩卷頭獎號碼為幾組中例如大樂透為"6"個號碼就輸入6
    try:
        groups = int(groups)
        quantity = int(quantity)
        ball = int(ball)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print("抽獎號碼及組數要輸入阿拉伯數字")
        continue
while i < groups:
    lottery = (random.sample(range(1, quantity), k=ball))
    num = sorted(lottery)
    print("發財號碼為:", lottery, end="")
    print("由小到大排列為:", num)
    i += 1
