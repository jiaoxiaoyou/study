"""
2020-06-01 Python 打卡
1、根据下面运行流程图和提示，实现文字版图书管理功能。
提示：主体流程代码已实现如下，三个功能分别用函数来实现.
每本图书用一个字典来存储：book1 ={'id':编号，'name':书名，'location':位置}
所有的图书放在一个列表：books =[book1,book2,book3..............]
主要运用知识点：字典和列表的增删查相关操作， for循环  while循环
基本要求：
实现添加、删除、显示所有书籍的功能函数。
添加图书时：不用考虑书名、编号、位置是否和已有的书籍信息重复：
删除图书时：输入删除的书籍，找到名为书籍的所有数据，显示出来，然后用户根据编号选择删除。
扩展要求：添加图书时，书名和位置可以随便写，编号不能和已经添加过得数据重复
"""

books = [{'id':'1','name':'Python','addr':'a1'},{'id':'2','name':'Java','addr':'a2'}]
del_books = []
def print_menu():
    print("="*40)
    print("           图书管理系统V6.1")
    print("1.查询图书")
    print("2.增加图书")
    print("3.删除图书")
    print("4.退出系统")
    print("="*40)
#函数：添加图书
def add_new_name():
    new_id = input("请输入图书ID：")
    while True:
        new_id = input('请重新输入你要新增的ID：')
        for test_id in books:
            if new_id in test_id['id']:
                print('图书馆有此ID的书籍')
                break
        else:
            break
    new_name = input("请输入图书名称：")
    new_addr = input("请输入图书存放地址：")
    #建立一个字典，把信息保存到字典的相对应位置
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['id'] = new_id
    new_infor['addr'] = new_addr
    #将字典添加到列表中
    books.append(new_infor)
    #打印
    print(books)

#函数：删除
def del_name():
    del_names = input("请输入要删除的图书姓名：")
    for temp in books:
        if del_names in temp['name']:
            del_books.append(temp)
    print(del_books)
    del_id =input('请选择你要删除书籍的ID：')
    for temp1 in books:
        if del_id in temp1['id']:
            books.remove(temp1)
            print("ID为 %s 的书籍已删除"% del_id)
#函数：显示所有图书
def display_all_name():
    for temp in books:
        print("ID：%s\n图书名称：%s\n存放地址：%s\n"%(temp['id'],temp['name'],temp['addr']))

#主函数
def main():

    print_menu()
    while True:
        num = int(input("请输入相对应的数字:"))
        if num ==1:
            display_all_name()
        elif num == 2:
            add_new_name()
        elif num == 3:
            del_name()
        elif num == 4:
            print('欢迎下次使用。。。')
            break
        else:
            print("您输入的选项不正确！")
main()