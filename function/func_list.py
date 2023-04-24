def hello():
    print("Hello, world!")

def hello1():
    print("Hello, worldwwww!")

func_list = [hello, hello1]
func_list[0]()
func_list[1]()

def hello():
    print("Hello, world!")

def hello1():
    print("Hello, worldwwww!")

# 使用函数名称构成的字符串列表
func_list = ["hello", "hello1"]

# 执行函数列表中的所有函数
for name in func_list:
    # 将函数名称转换为函数对象
    func = globals()[name]
    # 调用函数
    func()