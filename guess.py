from random import randint
while True:
    lowest = input("請輸入最低數值")
    highest = input("請輸入最高數值")
    # 檢查輸入的內容是否為數字
    try:  # 把字串轉換成整數
        lowest = int(lowest)
        highest = int(highest)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('格式錯誤，請輸入數字\n')
        continue
computer = randint(lowest, highest)
# 重複猜數字，直到猜對為止
while True:
    play = input("密碼%d~%d:" % (lowest, highest))
    # 檢查輸入的內容是否為數字
    try:
        play = int(play)  # 把字串轉換成整數
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('格式錯誤，請輸入數字\n')
        continue
    # 檢查輸入的數字是否介於規定範圍內
    if play <= lowest or play >= highest:
        print("請輸入%d~%d之間的整數\n" % (lowest, highest))
        continue
    # 判斷有沒有猜中密碼
    if play == computer:
        print('答對了！')
        break  # 猜對才跳脫迴圈
    elif play < computer:
        lowest = play
    else:
        highest = play
