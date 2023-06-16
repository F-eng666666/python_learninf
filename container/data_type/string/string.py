import sys
import time
from fnmatch import fnmatch, fnmatchcase

str = "ansel want to sleep"
#获取字符串的长度
def get_length():
    print(len(str))

#在字符串中查找指定子串，找到返回正序下标，找不到返回-1
def find_str():    
    print(str.find('fengfan1'))   

#字符串前缀的操作
def string_urbf():
    #字符串前缀
    """
        字符串前加 u或者不加
        举例:u"字符串中有中文"
        含义
        1、前缀u表示该字符串是unicode编码
        2、Python2中用,用在含有中文字符的字符串前，防止因为编码问题，导致中文出现乱码。
        3、一般要在文件开关标明编码方式采用utf8。
        4、Python3中,所有字符串默认都是unicode字符串。
    """
    str = u"字符串中有中文"
    print("u前缀",str)

    """
        字符串前加 r
        举例:r"adc\n\r\tdkfjkd"
        含义
        1、前缀r表示该字符串是原始字符串,即\不是转义符，只是单纯的一个符号。
        2、常用于特殊的字符如换行符、正则表达式、文件路径。
        3、注意不能在原始字符串结尾输入反斜线,否则Python不知道这是一个字符还是换行符(字符串最后用\表示换行)
    """
    str1= 'input\n'
    str= r'input\n'
    print(str1)
    print(str)

    """
        字符串前加 b
        含义
        1、前缀b表示该字符串是bytes类型。
        2、用在Python3中,Python3里默认的str是unicode类。Python2的str本身就是bytes类,所以可不用。
        3、常用在如网络编程中,服务器和浏览器只认bytes类型数据。如:send 函数的参数和 recv 函数的返回值都是 bytes 类型。
        4、在 Python3 中,bytes 和 str 的互相转换方式是
        str.encode('utf-8')
        bytes.decode('utf-8')
    """
    """
        字符串前加 f
        1、Python3.6新加特性,前缀f用来格式化字符串。可以看出f前缀可以更方便的格式化字符串,比format()方法可读性高且使用方便。
        2、而且加上f前缀后,支持在大括号内,运行Python表达式。
        3、还可以用fr前缀来表示原生字符串。
    """

    t0 = time.time()
    time.sleep(1)
    name = 'processing'
    # 以 f开头表示在字符串内支持大括号内的python 表达式
    print(f'{name} done in {time.time() - t0:.2f} s') 

def testFStr():                #字符串的格式化处理
    name = 'alex'
    age = 25
    print(f'my name is {name}, i am {age} years old')
    
#字符串长度测量
path = r'D:\pathfengfan1\Desktop\flash_station\log分析\*.txt'

#字符串中通配符的使用
def wildcard_string():
    #*通配符* 代替零、一或多个字符
    print(fnmatch('test.txt','*'))                  #True
    print(fnmatch('test.txt','test*'))              #True
    print(fnmatch('test.txt','*.txt'))              #True
    print(fnmatch('test.txt','test.txt*'))          #True
    print(fnmatch('test.txt','*.t*'))               #True,注意前后的*
    print(fnmatch(path,'*Desktop'))                 #False

    #通配符？代替任意一个字符
    print(fnmatch('test.txt','?est.txt'))
    print(fnmatch('test.txt','test.tx?'))
    print(fnmatch('test.txt','test.txt?'))
    print(fnmatch('test.txt','test.t?'))

    #通配符[],匹配abcd中任意一个字符
    print(fnmatch('test.txt','[abcd]est.txt'))
    print(fnmatch('test.txt','[rst]est.txt'))
    #通配符[],匹配a-z中任意一个字符
    print(fnmatch('test.txt','[a-d]est.txt'))
    print(fnmatch('test.txt','[a-z]est.txt'))


    # fnmatch函数，不区分大小写
    print(fnmatch('test.txt','*.txt')) 
    print(fnmatch('test.txt','*.TXT')) 

    # fnmatchcase函数，区分大小写
    print(fnmatchcase('test.txt','*.txt')) 
    print(fnmatchcase('test.txt','*.TXT')) 


#字符串的判断
def test_blank():
    username ="          "
    password = "sss"
    #1.通过isspace判断是否为空
    if username.isspace() or password.isspace():  #判断输入的用户名或密码是否为空
        print('用户名或密码不能为空')
    #2.通过len判断是否为零来判断
    if len(username) ==0 or len(password) == 0:  #判断输入的用户名或密码是否为空
        print('用户名或密码不能为空')
    else:
        print("密码输入格式正确")









 

def main():
    #get_length()
    #find_str()
    #wildcard_string()
    test_blank()



if __name__ == '__main__':
    print("enter fac_flash_tool.py __main__")
    main()
    sys.exit(0)