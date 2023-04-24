from random import randint

class Random():
    def rand(self):
        return randint(0,10)
    def guess(self):
        for i in iter([1,2,3,4,5,6,7,8],5):
            num += 1
            print("第%s次猜对,猜测数字是：%s"%(num,i))


def main():
    Random1 = Random()
    ret = Random1.rand()
    print(ret)
    I = [1,2,3]
    for i in iter(I):
        print(i)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:   #如果不知道什么错误类型，可以写Exception来监听所有错误类型
                print("except:",e)
    finally:
        print("running ending")

    