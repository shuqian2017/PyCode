__author__ = 'fke'

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eatting..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)


class Man(People):

    def piao(self):
        print("%s is piaoing......1 hour.....done" % self.name)

    # 重构父类的sleep方法
    def sleep(self):
        People.sleep(self)        # 先执行父类的sleep方法，再执行自己的sleep方法
        print("man is sleeping ")


class Woman(People):

    def get_birth(self):
        print("%s is born a baby....." % self.name)

m1 = Man("fke", 22)
m1.eat()
m1.piao()
m1.sleep()

w1 = Woman("lucy", 24)
w1.get_birth()
# w1.piao()
