#2. 3-17
#月薪超過 4 萬以及存款超過 50 萬就發信用卡
#否則不發


mouthly_income = input("請輸入月薪：")
saving_account = input("請輸入存款：")
mouthly_income = int(mouthly_income)
saving_account = int(saving_account)

if mouthly_income > 40000 and saving_account > 500000:
    print("發信用卡")
else:
    print("婉拒")