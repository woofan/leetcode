'''
按照字典中某键值排序
'''
a=[{'name':'zhangsan','age':14},{'name':'lisi','age':18},{'name':'wang','age':40}]
sorted(a,key = lambda x:x['age'], reverse = False)


a= {'zhang':14,'wang':18,'li':80}
sorted(a,key = lambda x:x[1], reverse = False)