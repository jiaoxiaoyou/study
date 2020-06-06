# @Author : jiaojie
# @CreateDate : 2020/5/16 22:44
# @Description : 第13节
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
# 文件的打开和关闭
    open()
    close

# 文件内容写入
    write:写入数据（内容必须是字符串）
    writelines:写入多条数据（内容是可迭代对象：列表）

# 文件内容读取
    read():读取文件中所有内容
    readline()：读取一行内容
    readlines()：按行读取所有的内容，每一行作为一个元素，放入列表中

# 文件打开的方式
    r：读取内容（只读模式）文件不存在会报错
    w：以写入的方式打开文件（文件不存在，创建一个新的文件，文件存在，覆盖原来的内容，重新写入）
    a：以写入的方式打开文件（文件不存在，创建一个新的文件，文件存在，在原内容尾部，追加写入）

"""
def file_read():
    # 打开文件
    fr = open('bj.txt', 'r', encoding='utf8')

    content = fr.read()
    print(type(content))
    print(eval(content))

    #print(fr.readline())

    #print(fr.readlines())

    # 一定要关闭文件
    fr.close()

list1 = [11, 22, 33]
def file_write():
    fw = open('bj.txt', 'a')

    fw.write(str(list1))
    fw.close()

#file_write()

file_read()


# 上下文管理器：with
# 自动关闭文件
with open('bj.txt', 'r', encoding='utf8') as f:
    print(f.read())


