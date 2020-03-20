#randon=隨機數工具包MOD模組
import random

i = int(input("請輸入要玩幾次:"))
a = 0
play_win = 0
computer_win = 0
play_computer = 0
while a < i:

    play = int(input("請輸入剪刀(1)石頭(2)布(3):"))
    computer = random.randint(1, 3)
    if play > 3:
        print("輸入錯誤請重新輸入")
        continue

    if play == 1:
        print("玩家出剪刀,", end="")
    elif play == 2:
        print("玩家出石頭,", end="")
    elif play == 3:
        print("玩家出布,", end="")

    if computer == 1:
        print("電腦出剪刀結果")
    elif computer == 2:
        print("電腦出石頭結果")
    elif computer == 3:
        print("電腦出布結果")
#石頭贏剪刀
#剪刀贏布
#布贏石頭
    if ((play == 1 and computer == 3)
            or (play == 2 and computer == 1)
            or (play == 3 and computer == 2)):

        print("***玩家贏了***")
        play_win += 1
    elif play == computer:
        print("***雙方平手***")
        play_computer += 1
    else:
        print("***電腦贏了***")
        computer_win += 1
    a += 1
print("總共比了%d場玩家贏了%d場，電腦贏了%d場，平手%d場，勝率%.2f%%" % (i, play_win, computer_win, play_computer, play_win/i*100))
