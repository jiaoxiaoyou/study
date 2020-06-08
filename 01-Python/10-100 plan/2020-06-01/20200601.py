# @Author : jiaojie
# @CreateDate : 2020/6/1 20:21
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
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


# 给图书馆内预定义一些数据

book1 = {"编号": "1", "书名": "天龙八部", "位置": "1号架2层"}
book2 = {"编号": "2", "书名": "天龙八部", "位置": "b区32架"}
book3 = {"编号": "3", "书名": "笑傲江湖", "位置": "a区44架"}
book4 = {"编号": "4", "书名": "笑傲江湖", "位置": "a区1架"}
books = [book1, book2, book3, book4]  # 存放所有图书的信息，全局变量

def print_menu():
    """
    输出提示用户的选项
    :return:
    """
    print("-----------------------------------")
    print("【1】：添加图书\n【2】：删除图书\n【3】：显示所有图书\n【4】：退出")

def get_books_id(book_list=books):
    """
    获取所有图书的编号值，存入列表中
    :param book_list: 存放书籍信息的list，不一定是所有书籍，所以定义为参数
    :return:
    """
    books_id = []
    for book in books:
        books_id.append(book["编号"])
    return books_id

def add_book():
    """
    添加图书，编号不能重复，若编号重复提示用户重新输入
    :return:
    """
    books_id = get_books_id(books)
    while True:
        book_id = input("请输入图书编号：")
        if book_id in books_id:
            print("您输入的编号已存在，请重新输入")
        else:
            break
    book_name = input("请输入图书名称：")
    book_location = input("请输入图书位置：")
    books.append({"编号":book_id, "书名":book_name, "位置":book_location})
    print("添加完毕，返回菜单页面")

def get_same_book(book_name, book_list=books):
    """
    获取指定库中，同一书名的书籍的信息
    :param book_name:
    :param book_list:
    :return:
    """
    del_books_list = []
    for book in books:
        if book_name == book["书名"]:
            del_books_list.append(book)
    return del_books_list

def del_book():
    """
    找到书籍名称，并根据该书籍名称的书籍id删除书籍（删除的编号必须是该书籍名称的编号）
    非常规场景处理：①没有该书籍，②书籍id不正确
    :return:
    """
    while True:
        del_book_name = input("请输入要删除的图书名：")
        del_books_list = get_same_book(del_book_name)
        del_book_count = len(del_books_list)
        books_count = len(books)

        if del_book_count > 0:
            print("找到{}本书籍名为：{}".format(del_book_count, del_book_name))
            print_books(del_books_list)

            while len(books) == books_count:
                del_book_id = input("请输入要删除图书的编号：")
                for del_book in del_books_list:
                    if del_book_id == del_book["编号"]:
                        books.remove(del_book)
                        break
                else:
                    print("您输入的编号不正确，请重新输入")
            break
        else:
            print("未找到您要删除的图书，请重新输入")
    print("删除完毕，返回菜单页面")




def print_books(book_list=books):
    """
    输出对应列表的每个书的信息
    :param book_list: 存放书籍信息的list，不一定是所有书籍，所以定义为参数
    :return:
    """
    for book_info in book_list:
        print("编号：{} 书名：{} 位置：{}".format(book_info['编号'], book_info['书名'], book_info['位置']))

def all_book():
    """
    输出当前所有图书的信息
    :return:
    """
    book_count = len(books)
    if book_count == 0:
        print("当前图书馆没有任何图书")
    else:
        print("当前共有{}本图书，所有的图书信息如下：".format(book_count))
        print_books()
        print("查询完毕，返回菜单页面")


def library_sys():
    print("---欢迎进入图书管理系统---")
    while True:
        # 打印菜单
        print_menu()
        num = input("请输入您的选项：")
        if num == "1":
            # 添加图书
            add_book()
        elif num == "2":
            # 删除图书
            del_book()
        elif num == "3":
            # 查询所有图书
            all_book()
        elif num == "4":
            print("谢谢使用，程序即将关闭")
            break
        else:
            print("您输入的选项有误，请重新选择")


library_sys()