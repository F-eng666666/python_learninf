import zipfile

#is_zipfile(filename)，测试filename的文件，看它是否是个有效的zipfile
path = r'D:\fengfan1\Desktop\flash_station\log分析\5g_pkg.zip'
ret = zipfile.is_zipfile(r'D:\fengfan1\Desktop\flash_station\log分析\5g_pkg.zip')
print(ret)


z = zipfile.ZipFile(path,'r')

#z.namelist()，返回一个列表，内容是zip文件中所有子文件的path（相对于zip文件包而言的）。相当于是一个保存了zip内部目录结构的列表
ret = z.namelist()
print(ret)


#z.extract(member, path=None, pwd=None)，从zip中提取一个文件，member可以是namelist中的某个文件，
#也可以从z.infolist 中得到filename，将它放到指定的path下，pwd是密码，
#用于被加密的zip文件；如果path没有指定，比如在脚本ipython下运行，会
#提取保存在脚本默认根目录下，生成test_file文件，并提取出a.text文件保存在文件夹里；

ret = z.extract('update/firehose/partition_complete_p4K_b256K.mbn', path=None, pwd=None)
print(ret)




#z.close()，关闭文件，结束时必须要有
z.close()

