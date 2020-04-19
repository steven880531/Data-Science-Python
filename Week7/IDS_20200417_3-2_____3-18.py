#3-2. 3-18
#判斷奇數偶數－－合併


user_int = input("請輸入一個正整數：")
user_int = int(user_int)

if (user_int % 2) == 0 :
    print("{}是偶數" .format(user_int))
else:
    print("{}是奇數" .format(user_int))