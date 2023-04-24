import os
import glob
import pathlib
import sys
def llll():
    #脚本运行的绝对路径
    ret = pathlib.Path(__file__).parent.resolve()
    print(ret)

    #windows 上储存临时文件的路径：LOCALAPPDATA
    ret = os.getenv('LOCALAPPDATA')
    print(ret)

    file_path_1 = ret+"//filt.txt"
    #判断文件是否存在
    if os.path.exists(file_path_1):
        os.remove(file_path_1)#删除文件

    #打开文件
    f1 = open(file_path_1, "a+")
    print(ret)


    #参数为文件夹路径，可以返回文件夹下的所有子文件夹、文件名称
    path = 'D:\\fengfan1\\Desktop\\flash_station\\log分析'
    for file_name in os.listdir(path):
        print(file_name)


    #绝对路径、子文件夹、文件名。 此方法可以遍历文件夹下的所有文件、子文件及内的所有文件：
    print(u"绝对路径、子文件夹、文件名")
    path = 'D:\\fengfan1\\Desktop\\flash_station\\log分析'
    for root, dirs, files in os.walk(path):
        #print("1111111111111111111")
        print(root)
        print(dirs)
        for file_abs in glob.glob(root+r"\*.txt"):
            print("txt:",file_abs)
            #if(),判断压缩包内的文件

        #print(files)


    #参数为路径以及文件过滤条件，若不设置过滤需填写为*，此函数会返回包括路径的文件夹和文件名
    path = r"D:\fengfan1\Desktop\flash_station\log分析"
    signal = r"\*"
    path = path + signal
    print(path)
    print(glob.glob(path)[0],type(glob.glob(path)))
    print(r"********************")
    for file_abs in glob.glob(path):
        #print("file_abs: " ,type(file_abs))
        print(file_abs)
        #print(file_abs[file_abs.find(path)+len(path)-4:])

def get_path_name(path):
    print(u"绝对路径、子文件夹、文件名")
    #path = 'D:\\fengfan1\\Desktop\\flash_station\\log分析'
    for root, dirs, files in os.walk(path):
        #print("1111111111111111111")
        print(root)
        print(dirs)
        for file_abs in glob.glob(root+r"\*.txt"):
            print("txt:",file_abs)
import os

if os.access("./data/test_file.txt", os.F_OK):
    print("文件存在")
if os.access("./data/test_file.txt", os.R_OK):
    print("文件可读")
if os.access("./data/test_file.txt", os.W_OK):
    print("文件可写")
if os.access("./data/test_file.txt", os.X_OK):
    print("文件可执行")

if os.access("data", os.F_OK):
    print("文件夹存在")
if os.access("data", os.R_OK):
    print("文件夹可读")
if os.access("data", os.W_OK):
    print("文件夹可写")
if os.access("./data/test_file.txt", os.W_OK):
    print("文件可写")
if os.access("data", os.X_OK):
    print("文件夹可执行") #文件夹的可执行包括哪些操作？打开，压缩，复制等等



def main():
    get_path_name('D:\\fengfan1\\Desktop\\flash_station\\log分析')

if __name__ == '__main__':
    print("enter fac_flash_tool.py __main__")
    main()
    sys.exit(0)