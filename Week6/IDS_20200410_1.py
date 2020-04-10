#P2-56：檢驗身分證字號尾數是否為奇數

#【函數，資料型態轉換】
#函數"input"的使用
#把"input"函數輸入的"文字"轉換成"整數"
#把布林命名成物件

id_last_digit =  input("請輸入您身分證字號的尾數：")
id_last_digit = int(id_last_digit)
print(type(id_last_digit))
modulo = id_last_digit % 2
ans = modulo == 1
print(ans)