# @Author : jiaojie
# @CreateDate : 2020/5/17 0:26
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
异常捕获


"""
dic = {'aa':11}
# try:
#     #print(a)
#     #print(dic['bb'])
#     dict1 = dict([11, 22, 33])
# except NameError as e:
#     print('代码发生了错误')
#     print(e)
# except KeyError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('代码没有发生错误')

# try:
#     print(dic['bb'])
#     print(a)
#     dic1 = dict([11, 22, 33])
# except (NameError, KeyError, TypeError) as e:
#     print(e)

# try:
#     print(dic['bb'])
#     print(a)
#     dic1 = dict([11, 22, 33])
# except Exception as e:
#     print(e)

data1 = [11, 22, 33]
data2 = [22, 33, 44]

try:
    assert data1==data2
except AssertionError as e:
    #print('测试用例没通过')
    raise e
else:
    print('测试用例通过')

#raise NameError('主动引发的异常')