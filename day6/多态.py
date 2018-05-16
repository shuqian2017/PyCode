__author__ = 'fke'

class People(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eatting..." % self.name)

    # 多态：同一个接口多种实现形式
    @staticmethod
    def People_sleep(obj):
        obj.sleep()

    def talk(self):
        print("%s is talking..." % self.name)

class Man(People):

    def piao(self):
        print("%s is piaoing......1 hour.....done" % self.name)

    # 重构父类的sleep方法
    def sleep(self):
        print("%s is sleeping...5H" % self.name)


class Woman(People):

    def sleep(self):
        print("%s is sleeping...8H" % self.name)

    def get_birth(self):
        print("%s is born a baby....." % self.name)

m1 = Man("fke", 22)
w1 = Woman("lucy", 24)

# m1.talk()
# w1.talk()
People.People_sleep(m1)
People.People_sleep(w1)
