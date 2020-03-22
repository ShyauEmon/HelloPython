from random import randint
a = []
# 判斷輸入是否為整數
while True:
    ball = input("請輸入要抽出幾球:")
    quantity = input("請輸入有幾顆球:")
    try:
        ball = int(ball)
        quantity = int(quantity)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print("抽獎號碼及總球數要輸入阿拉伯數字")
        continue
# 抽出發財號碼
while True:
    computer = randint(1, quantity)
    if len(a) < ball:
        if computer not in a:
            a.append(computer)
    elif len(a) == ball:
        break
# sorted為list清單由小到大排序
num = sorted(a)
print("發財號碼為:", a, end="")
print("由小到大排列為:", num)
