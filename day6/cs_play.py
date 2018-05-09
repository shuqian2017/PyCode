__author__ = 'fke'

class Role:
    n = 123  # 类变量
    n_list = []
    name = "我是类name"

    def __init__(self, name, role, weapon, life_value=100, money=5000):
        # 构造函数
        # 在实例化时做一些类的初始化工作
        self.name = name    # r1.name = name 实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value    # 前面加2个下划线-->"__"表示私有属性,只能程序内部访问
        self.money = money

    def __del__(self):
        # 析构函数: 在实例释放 销毁的时候执行,通常用于做一些收尾的工作,如关闭一些数据库的链接,临时文件等.
        pass
        # print("%s 彻底死了。。。。" % self.name)

    def show_status(self):
        print("\033[34;1mname:%s weapon:%s life_val:%s\033[0m" % (self.name, self.weapon, self.__life_value))

    def __shot(self):     # 类的方法，功能（动态属性）
        # 前面加2个下划线-->"__"表示私有方法,只能程序内部访问
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 50
        print("%s:ah..., I got shot..." % self.name)

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name, gun_name))


r1 = Role('fke', 'police', 'AK47')      # Role(r1,'fke','police','AK47') 把一个类变成具体对象的过程叫实例化（初始化一个类，造林一个对象）
r1.buy_gun('沙漠之鹰')
r1.got_shot()
r1.__shot__()
print(r1.show_status())
# print(r1.__life_value)

r2 = Role('jack', 'terrorist', '98K')
r2.got_shot()

r1.name = "黄飞鸿"
r1.n_list.append("from r1")
r1.bullet_prove = True
r1.n = "修改类变量"
print(r1.n, r1.name, r1.bullet_prove, r1.weapon)


r2.name = "方世玉"
r2.n_list.append("from r2")
print("r2:", r2.name, r2.n, r2.n_list)

print(Role.n_list)

Role.n = "ABC"
print(r1.n, r2.n)
