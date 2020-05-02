#1. 4-25
#介於 x 到 y 之間的奇數有幾個（包含 x 與 y 假如它們是奇數）
  
x = int(input("請輸入起始的正整數："))
y = int(input("請輸入終止的正整數："))
odd_counter = 0
i = x
while i <= y:
    if i % 2 == 1:
        odd_counter += 1
    i += 1

print("===============")
print("{} 到 {} 之間的奇數有 {} 個".format(x, y, odd_counter))