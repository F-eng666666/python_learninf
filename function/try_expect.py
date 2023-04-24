import sys 

class try_except:

    
    def test1(self):  
        i = 0
        j = 12
        try:
            n = j/i
        except ZeroDivisionError as e:
            print("except:",e)
            i = 1
            n = j/i
        except ValueError as value_err:  #可以写多个捕获异常
            print("ValueError")
        finally:
            print("final print")
    def test2(self):
        i = 0
        j = 12
        try:
            n = j/i
        except (ZeroDivisionError,ValueError) as e:
            print("except:",e)
            i = 1
    def test3(self):  
            i = 0
            j = 12
            try:
                n = j/i
            except Exception as e:   #如果不知道什么错误类型，可以写Exception来监听所有错误类型
                print("except:",e)


def main():
    demo1 = try_except()
    #demo1.test1()
    #demo1.test2()
    demo1.test3()

if __name__ == '__main__':
    print("enter fac_flash_tool.py __main__")
    main()
    sys.exit(0)