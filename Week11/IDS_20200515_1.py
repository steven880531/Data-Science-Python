#1. 5
#印出 xx市 的每人每月最低生活費為 xx,xxx

citycost_dic = {
    "臺北市" : 17005,
    "新北市" : 15500,
    "桃園市" : 15281,
    "臺中市" : 14596,
    "臺南市" : 12388,
    "高雄市" : 13099,
    "金門縣" : 11648,
    "連江縣" : 11648
             }

living_area = input("請輸入您的居住城市：")
living_cost = citycost_dic[living_area]
print("{} 的每人每月最低生活費為 {:,}".format(living_area, living_cost))