import random
import os
while True:
    q = input("開始請按(1)離開請按(2):")
    if q == "1":
        lottery = []
        i = 0
        while True:
            groups = input("請輸入要抽幾組號碼:")  # 此為你想要幾組電腦選號
            quantity = input("請輸入總球數:")  # 玩的彩卷有幾號例如:大樂透為1~49個號碼就輸入49
            ball = input("請輸入抽出幾球:")  # # 玩的彩卷會出幾個號碼例如:大樂透選6個號碼就輸入6
            try:
                groups = int(groups)
                quantity = int(quantity)
                ball = int(ball)
                break
            except ValueError:  # 轉換失敗便要求重新輸入數字
                print("抽獎號碼及組數要輸入阿拉伯數字")
                continue
        if  quantity <= ball:
            print("總球數不能等於以及小於抽球數")
            continue
        else:
            if quantity == 49 and ball == 6:
                print("您玩的是大樂透6個號碼全中為頭獎")
                while i < groups:
                    lottery = (random.sample(range(1, quantity), k=ball))
                    num = sorted(lottery)
                    l =[]
                    for o in lottery:
                        t = "%02d" % o
                        l.append(t)
                    m = []
                    for n in num:
                        u = "%02d" % n
                        m.append(u)
                    print("發財號碼為:" + ",".join(l), end="")
                    print("由小到大為:" + ",".join(m))
                    i += 1
            elif quantity == 38 and ball == 6:
                print("您玩的是威力彩第一區6個號碼全中+第二區01~08選一號中獎即為頭獎")
                while i < groups:
                    lottery = (random.sample(range(1, quantity), k=ball))
                    num = sorted(lottery)
                    l =[]
                    for o in lottery:
                        t = "%02d" % o
                        l.append(t)
                    m = []
                    for n in num:
                        u = "%02d" % n
                        m.append(u)
                    print("發財號碼為:" + ",".join(l), end="")
                    print("由小到大為:" + ",".join(m))
                    i += 1
            elif quantity == 39 and ball == 5:
                print("您玩的是金彩539，5個號碼全中獎即為頭獎")
                while i < groups:
                    lottery = (random.sample(range(1, quantity), k=ball))
                    num = sorted(lottery)
                    l =[]
                    for o in lottery:
                        t = "%02d" % o
                        l.append(t)
                    m = []
                    for n in num:
                        u = "%02d" % n
                        m.append(u)
                    print("發財號碼為:" + ",".join(l), end="")
                    print("由小到大為:" + ",".join(m))
                    i += 1
            elif quantity == 24 and ball == 12:
                while i < groups:
                    lottery = (random.sample(range(1, quantity), k=ball))
                    num = sorted(lottery)
                    l =[]
                    for o in lottery:
                        t = "%02d" % o
                        l.append(t)
                    m = []
                    for n in num:
                        u = "%02d" % n
                        m.append(u)
                    print("發財號碼為:" + ",".join(l), end="")
                    print("由小到大為:" + ",".join(m))
                    i += 1
            else:
                while i < groups:
                    lottery = (random.sample(range(1, quantity), k=ball))
                    num = sorted(lottery)
                    l =[]
                    for o in lottery:
                        t = "%02d" % o
                        l.append(t)
                    m = []
                    for n in num:
                        u = "%02d" % n
                        m.append(u)
                    print("發財號碼為:" + ",".join(l), end="")
                    print("由小到大為:" + ",".join(m))
                    i += 1
    elif q == "2":
        break
print("感謝使用祝您一路發")
os.system('pause')
