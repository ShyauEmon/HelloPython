# randon隨機數工具包MOD模組
import random
a = 0
play_win = 0
computer_win = 0
play_computer = 0

while True:  
    # 判斷遊玩次數是否整數
    i = input("請輸入要玩幾次:")
    try:
        i = int(i)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('遊玩次數請輸入阿拉伯數字\n')
        continue
while a < i:
    computer = str(random.randint(1, 3))
    play = input("請輸入剪刀(1)石頭(2)布(3):")
    # 如果玩家輸入不等於1.2.3.剪刀.石頭.布.scissors.rock.paper會請玩家再次輸入
    if (play != "1" and play != "2" and play != "3"  
            and play != "剪刀" and play != "石頭" and play != "布"
            and play != "scissors" and play != "rock" and play != "paper"):
        print("輸入錯誤請重新輸入")
        continue
    # 將隨機出來的數值轉成computer_a,computer_b才能判斷平手情況
    if computer == "1":
        computer_a = "剪刀"
        computer_b = "scissors"
    elif computer == "2":
        computer_a = "石頭"
        computer_b = "rock"
    elif computer == "3":
        computer_a = "布"
        computer_b = "paper"
    # 輸出玩家跟電腦分別出了什麼
    if play == "1" or play == "剪刀" or play == "scissors":
        print("玩家出剪刀,", end="")
    elif play == "2" or play == "石頭" or play == "rock":
        print("玩家出石頭,", end="")
    elif play == "3" or play == "布" or play == "paper":
        print("玩家出布,", end="")
    if computer == "1":
        print("電腦出剪刀結果")
    elif computer == "2":
        print("電腦出石頭結果")
    elif computer == "3":
        print("電腦出布結果")
    # 判斷輸贏原則石頭贏剪刀,剪刀贏布,布贏石頭
    if ((play == "1" and computer == "3")
            or (play == "2" and computer == "1")
            or (play == "3" and computer == "2")
            or (play == "剪刀" and computer == "3")
            or (play == "石頭" and computer == "1")
            or (play == "布" and computer == "2")
            or (play == "scissors" and computer == "3")
            or (play == "rock" and computer == "1")
            or (play == "paper" and computer == "2")):
        print("***玩家贏了***")
        play_win += 1
    elif play == computer or play == computer_a or play == computer_b:
        print("***雙方平手***")
        play_computer += 1
    else:
        print("***電腦贏了***")
        computer_win += 1
    a += 1
print("總共比了%d場玩家贏了%d場，電腦贏了%d場，平手%d場，勝率%.2f%%" % (i, play_win, computer_win, play_computer, play_win/i*100))
