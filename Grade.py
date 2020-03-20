a_score = float(input("請輸入國文分數:"))
b_score = float(input("請輸入數學分數:"))
c_score = float(input("請輸入英文分數:"))
d_score = float(input("請輸入理化分數:"))
abcd_score = 0
dcba_score = 0

if a_score >= 60 and  a_score <=100:
    print("國文%.1f分及格" % a_score)
elif a_score >=0 and  a_score <60:
    print("國文%.1f分不及格"%a_score)
else:
    print("國文分數輸入錯誤")

if b_score >= 60 and  b_score <=100:
    print("數學%.1f分及格" % b_score)
elif b_score >=0 and  b_score <60:
    print("數學%.1f分不及格"%b_score)
else:
    print("數學分數輸入錯誤")

if c_score >= 60 and  c_score <=100:
    print("英文%.1f分及格" % c_score)
elif c_score >=0 and  c_score <60:
    print("英文%.1f分不及格"%c_score)
else:
    print("英文分數輸入錯誤")

if d_score >= 60 and  d_score <=100:
    print("理化%.1f分及格" % d_score)
elif d_score >=0 and  d_score <60:
    print("理化%.1f分不及格"%d_score)
else:
    print("理化分數輸入錯誤")
#計算科目總共幾個及格
if a_score >= 60:
    abcd_score = abcd_score + 1
else:
    dcba_score = dcba_score + 1
if b_score >= 60:
    abcd_score = abcd_score + 1
else:
    dcba_score = dcba_score + 1
if c_score >= 60:
    abcd_score = abcd_score + 1
else:
    dcba_score = dcba_score + 1
if d_score >= 60:
    abcd_score = abcd_score + 1
else:
    dcba_score = dcba_score + 1
print("總共考了%d科，%d科目及格，%d科目不及格" %((abcd_score + dcba_score),abcd_score,dcba_score))
