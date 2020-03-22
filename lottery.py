from random import randint
a = 0
while True:
    computer = randint(1, 49)
    # 抽出六組號碼
    if a == 0:
        num_1 = computer
        a += 1
        continue
    elif a == 1:
        num_2 = computer
        a += 1
        continue
    elif a == 2:
        num_3 = computer
        a += 1
        continue
    elif a == 3:
        num_4 = computer
        a += 1
        continue
    elif a == 4:
        num_5 = computer
        a += 1
        continue
    elif a == 5:
        num_6 = computer
        a += 1
        continue
        # 所有號碼都不重複
    elif (num_1 != num_2 and num_1 != num_3 and num_1 != num_4 and num_1 != num_5
          and num_1 != num_6 and num_2 != num_3 and num_2 != num_4
          and num_2 != num_5 and num_2 != num_6 and num_3 != num_4
          and num_3 != num_5 and num_3 != num_6 and num_4 != num_5
          and num_4 != num_6 and num_5 != num_6):
        break
        # 判斷號碼是否有重複
    elif (num_1 == num_2 or num_1 == num_3 or num_1 == num_4 or num_1 == num_5
          or num_1 == num_6 or num_2 == num_3 or num_2 == num_4
          or num_2 == num_5 or num_2 == num_6 or num_3 == num_4
          or num_3 == num_5 or num_3 == num_6 or num_4 == num_5
          or num_4 == num_6 or num_5 == num_6):
        num = sorted([num_1, num_2, num_3, num_4, num_5, num_6])  # sorted函数可对list进行排序
        print("號碼遇到重複:", num, )
        a = 0
        continue
print("發財號碼為:", [num_1, num_2, num_3, num_4, num_5, num_6])
num = sorted([num_1, num_2, num_3, num_4, num_5, num_6])   # sorted函数可对list进行排序
print("由小到大排列為:", num,)
