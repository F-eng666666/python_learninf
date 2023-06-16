list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]


res = map(lambda x,y: x+y,list1,list2)
print(res)
print(type(res))
print(list(res))