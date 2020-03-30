#P2-68：球員BMI與過重判斷

#【函數，數值格式調整，布林，資料型態轉換】
#函數"input"與"print"資料提取填空的使用
#把"input"函數輸入的"文字"轉換成"浮點數"
#把"print"函數導入的數值調整成小數點兩位

player_name = input("請輸入球員姓名：")
player_height = input("請輸入球員身高(cm)：")
player_weight = input("請輸入球員體重(kg)：")
player_height = float(player_height)
player_weight = float(player_weight)
player_bmi = player_weight / (player_height/100)**2
print("{}的身體質量指數為：{:.2f}".format(player_name, player_bmi))
print("{}是否過重：{}".format(player_name, player_bmi > 30))