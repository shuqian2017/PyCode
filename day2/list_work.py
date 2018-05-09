__author__ = 'fke'

product_list = [
    ('Ipone', 5800),
    ('Mac Pro', 9500),
    ('book', 50),
    ('bike', 850),
    ('coffee', 65),
    ('M_LED', 512)
]

shop_list = []
money = input("请输入你的工资：")
if money.isdigit():
    money = int(money)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("请选择你要购买的商品编号")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= money:  # 判断是否买的起该商品
                    shop_list.append(p_item)
                    money -= p_item[1]
                    print("已经将 %s 添加到您的购物车，你的当前余额为：\033[41;1m %s \033[0m" % (p_item, money))
                else:
                    print("\033[41;1m 您的余额只剩下%s啦，还买个毛线\033[0m" % money)
            else:
                print("你输入的商品编号%s不存在".format(user_choice))
        elif user_choice == 'q':
            print("----------------------商品列表-------------------------")
            for p in shop_list:
                print(p)
            print("你的剩余余额为%s" % money)
            exit()
        else:
            print("无效的选项")

