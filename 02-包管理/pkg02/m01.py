class Student():
    def __init__(self, name="Noname", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0} and I am {1} years old!".format(self.name,self.age))


def sayHello():
    print("Hi,Bro")

# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("我是模块001")