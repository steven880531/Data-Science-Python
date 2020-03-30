#P2-50：讓使用者輸入城市名稱與天氣，並印出「我在OOO，天氣OOO」

#【函數】
#函數"input"與"print"資料導入的使用

city = input("請輸入你所在的城市：")
weather = input("請輸入目前的天氣：")
print("我在{}，天氣{}".format(city, weather))
