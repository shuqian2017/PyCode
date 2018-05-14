__author__ = 'fke'

# class People:   # 经典类
class People(object):  # 新式类

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def eat(self):
        print("%s is eatting..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)


# 多继承，假设man和woman都可以有的类
class Relation(object):

    # def __init__(self, name, n2):
    #     print(self.name)

    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))
        self.friends.append(obj)

class Man(Relation, People):

    # 多继承时，假设子类没有构造方法(如下被注释掉时)，上面的Relation构造方法调用self.name时出错.同理看下面的woman调用
    '''
    # Man类和Woman类有共同属性，如果man有自己的属性如money，那就需要将man进行重新初始化
    def __init__(self, name, age, money):   # 此时调用自己的构造方法进行初始化
        # 下面的2种继承父类的构造方法
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)        # 有共同的属性name,age 所以这部分可以调用父类的构造方法
        self.money = money
        print("%s 一出生就有%s money" % (self.name, self.money))
    '''

    def piao(self):
        print("%s is piaoing......1 hour.....done" % self.name)

    # 重构父类的sleep方法
    def sleep(self):
        People.sleep(self)        # 先执行父类的sleep方法，再执行自己的sleep方法
        print("man is sleeping ")


class Woman(People, Relation):

    '同上面，虽然woman也没有自己的构造方法，但是它是先继承People，而其里面有关于name的构造方法，所以再继承Relation 虽然它也没有构造方法，再调用make_friends时此已经有self.name属性故不会出错'

    def get_birth(self):
        print("%s is born a baby....." % self.name)

# m1 = Man("fke", 22, 100)
m1 = Man("fke", 22)

w1 = Woman("lucy", 24)


w1.make_friends(m1)
m1.name = "大帅逼"  # 假设初始化后fke改名字了，但其实还是她这个人
print("\033[31;1mfke已经更名为%s\033[0m" % w1.friends[0].name)
