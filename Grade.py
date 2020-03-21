while True:  # 判斷成績是否輸入正確
    a_score = input("請輸入國文分數:")
    b_score = input("請輸入數學分數:")
    c_score = input("請輸入英文分數:")
    d_score = input("請輸入理化分數:")
    try:
        a_score = float(a_score)
        b_score = float(b_score)
        c_score = float(c_score)
        d_score = float(d_score)
        break
    except ValueError:  # 轉換失敗便要求重新輸入數字
        print('成績請輸入阿拉伯數字\n')
        continue
# 計算及格跟不及格有幾科
score_win = 0
score_lose = 0
# 判斷是否及格
if (a_score >= 60) and (a_score <= 100):
    score_win = score_win + 1
    print("國文%.1f分及格" % a_score)
elif (a_score >= 0) and (a_score < 60):
    score_lose = score_lose + 1
    print("國文%.1f分不及格" % a_score)
else:
    print("國文分數輸入錯誤")
if (b_score >= 60) and (b_score <= 100):
    score_win = score_win + 1
    print("數學%.1f分及格" % b_score)
elif (b_score >= 0) and (b_score < 60):
    score_lose = score_lose + 1
    print("數學%.1f分不及格" % b_score)
else:
    print("數學分數輸入錯誤")
if (c_score >= 60) and (c_score <= 100):
    score_win = score_win + 1
    print("英文%.1f分及格" % c_score)
elif (c_score >= 0) and (c_score < 60):
    score_lose = score_lose + 1
    print("英文%.1f分不及格" % c_score)
else:
    print("英文分數輸入錯誤")
if (d_score >= 60) and (d_score <= 100):
    score_win = score_win + 1
    print("理化%.1f分及格" % d_score)
elif (d_score >= 0) and (d_score < 60):
    score_lose = score_lose + 1
    print("理化%.1f分不及格" % d_score)
else:
    print("理化分數輸入錯誤")
print("總共考了%d科，%d科目及格，%d科目不及格" % ((score_win + score_lose), score_win, score_lose))
