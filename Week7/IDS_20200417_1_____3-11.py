#1. 3-11
#月薪超過 4 萬或存款超過 50 萬就發信用卡

#input,轉換資料型態為float,if,or


mouthly_income = input("請輸入月薪：")
saving_account = input("請輸入存款：")
mouthly_income = int(mouthly_income)
saving_account = int(saving_account)

#"if"只支援"float"，不支援"str"與"int"
#注意條件後的":"，只能用半形，且下行的結果要縮排：按"tab鍵"
if mouthly_income > 40000 or saving_account > 500000:
    print("發信用卡")