#创建列表
list1 = ['a', 'b', 'c']
print(f"使用方括号创建的list1为{list1}")
list2 = list(('abc',666,list1))
print(list2)
list2 = [i for i in range(10)]
print(list2)

#获取和查找列表中的元素
list3 = ['apple', 'banana', 'cherry', 'cheese', 'grape']
print(f"通过索引获取列表: {list3[1]}")
print(f"通过负索引获取列表: {list3[-1]}")
print(f"通过切片获取列表: {list3[1:3]}")
print(f"通过切片获取列表: {list3[1:]}")
print(f"通过切片获取列表: {list3[:2]}")
print(f"通过切片并指定步长2获取列表: {list3[: : 2]}")
print(f"查找指定元素在列表中的位置: {list3.index('apple')}")
print(f"判断列表是否在列表中{'apple' in list3}")

#修改列表中的元素
list4 = ['apple', 'banana', 'cherry', 'cheese', 'grape']
list4_1 = list4
list4[1] = 'orange'
print(f"list4修改后的列表为: {list4}")
print(f"list4_1修改后的列表为: {list4_1}")
list4[2:3] = ['watermelon', 'huolongguo', 'orange']
print(f"list4修改后的列表为: {list4}")

#删除列表中的元素
list5 = ['apple', 'banana', 'cherry', 'cheese', 'grape', 'orange','watermelon']
list5.remove('banana')
print(f"remove 删除后的列表为: {list5}")
del list5[1]
print(f"del 删除后的列表为: {list5}")
list5.pop()
print(f"pop 默认删除后的列表为: {list5}")
list5.pop(0)
print(f"指定删除0号索引后的列表为: {list5}")
list5.clear()
print(f"清空后的列表为: {list5}")


#在列表中插入元素
list7 = ['apple', 'banana', 'cherry', 'cheese', 'grape']
list7.insert(1, 'orange')
print(f"在索引1插入 orange 后的列表为: {list7}")
list7.append('orange')
print(f"尾部插入orange后的列表为: {list7}")

#与加法运算符（+）不同，extend方法是就地修改原列表，不会返回一个新列表
list7.extend(['watermelon', 'huolongguo'])
print(f"尾部插入后的列表为: {list7}")
print(f"插入后的列表长度为: {len(list7)}")

#列表的其它操作

list8 = ['1', '3', '2', '4', '5']
list8.sort()
print(f"排序后的列表为: {list8}")
list8.reverse()
print(f"反转后的列表为: {list8}")
list8_1 = list8.copy()
print(f"拷贝后的列表为: {list8_1}")
list8_2 = list8 + list8_1
print(f"合并后的列表为: {list8_2}")

list9 = ['1', '3', '2', '4', '5']
list9_1 = ['a', 'b', 'c', 'd', 'e']
list9.extend(list9_1)
print(f"合并后的列表为: {list9}")
list9_1.reverse()
print(f"反转后的列表为: {list9_1}")
print(f"子元素反转后: {list9}")