import numpy as np
import matplotlib.pyplot as plt
import random


#对比柱状图bar
x = range(8) 
y = [100,200,400,350,450,350,250,300]
z = [200,300,350,250,450,450,500,250]
plt.figure(figsize=(20,8), dpi=80)
plt.bar( x, y, width=0.2, color='r', label='Bar_1' )
#加一个柱状图，[i+0.2 for i in x]为间距生成式
plt.bar( [i+0.2 for i in x], z, width=0.2, color='b', label='Bar_2' )
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
#修改x刻度名字
plt.xticks([i+0.1 for i in x], ['class1','class2','class3','calss4','class5','class6','class7','calss8']) 
#设置xy标签
plt.xlabel('Classes')
plt.ylabel('Numbers')
plt.title('the Numbers of Classes')

#调整图的尺寸，对于标注超过线时
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.999,hspace=0.3)
plt.show()
