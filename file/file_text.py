import os
import glob
import pathlib
import sys
import zipfile


def get_path_name(path):
    print(u"绝对路径、子文件夹、文件名")
    #path = 'D:\\fengfan1\\Desktop\\flash_station\\log分析'
    for root, dirs, files in os.walk(path):
        print(root)
        print(dirs)
        for zip_path in glob.glob(root+r"\*.zip"):
            if(zipfile.is_zipfile(zip_path)): 
                z = zipfile.ZipFile(zip_path,'r')
                ret = z.namelist()
                if("contents.xml" in ret and 'md5.txt' in ret): #for     ,continue
                    #print(ret)
                    print("zip:",zip_path)
                    z.close()
                    return 0

    return -1

def main():
    get_path_name('D:\\fengfan1\\Desktop\\flash_station\\log分析')

if __name__ == '__main__':
    print("enter fac_flash_tool.py __main__")
    main()
    sys.exit(0)