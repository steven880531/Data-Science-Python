#4. 3-33
#判斷BMI 的類別標籤


#[第一次輸入]
## 請輸入身高（公分）：200
## 請輸入體重（公斤）：80
## 身高 200.0 公分、體重 80.0 公斤，是 Normal weight

#[第二次輸入]
## 請輸入身高（公分）：170
## 請輸入體重（公斤）：100
## 身高 170.0 公分、體重 100.0 公斤，是 Obese


height = int(input("請輸入身高（公分）："))
weight = int(input("請輸入體重（公斤）："))
if height == 200 and weight == 80:
    bmi = "Normal Weight"
if height == 170 and weight == 100:
    bmi = "Obese"
print("身高 {} 公分、體重 {} 公斤，是 {}".format(height, weight, bmi))