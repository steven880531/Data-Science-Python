#2. 4-26
#介於 x 到 y 之間的奇數加總為何（包含 x 與 y 假如它們是奇數）

x = int(input("請輸入起始的正整數："))
y = int(input("請輸入終止的正整數："))
odd_summation = 0
i = x
while i <= y:
    if i % 2 == 1:
        odd_summation += i
    i += 1

print("===============")
print("{} 到 {} 之間的奇數加總為 {}".format(x, y, odd_summation))