# @Author : 强小林
# @CreateDate : 2020/5/21 14:08
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第十三天
1、根据下面运行流程图和提示，实现文字版图书管理功能。
提示：主体流程代码已实现如下，三个功能分别用函数来实现.
每本图书用一个字典来存储：book1 ={‘id’:编号，‘name’:书名，‘location’:位置}
所有的图书放在一个列表：boosk =[book1,book2,book3..............]
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
    输出提示用户的菜单
    :return:
    """
    print("---------------------------------------")
    print("【1】：添加图书\n【2】：删除图书\n【3】：显示所有图书\n【4】：退出")


def print_books(book_list=books):
    """
    输出对应列表的每个书的信息
    :param book_list:存放书籍信息的list，不一定是所有书籍，所以定义为参数
    :return:
    """
    for book_info in book_list:
        print("编号:{} 书名:{} 位置:{}".format(book_info["编号"], book_info["书名"], book_info["位置"]))


def get_book_id(book_list=books):
    """
    获取所有图书的编号值，存入列表中
    :param book_list: 存放书籍信息的list，不一定是所有书籍，所以定义为参数
    :return:
    """
    book_ids = []
    for book_info in book_list:
        book_ids.append(book_info["编号"])
    return book_ids


def get_same_book(book_name, book_list=books):
    """
    获取指定库中，同一书名的书籍的信息
    :param book_name:书籍名称
    :param book_list:存放书籍信息的list，不一定是所有书籍，所以定义为参数
    :return:
    """
    same_book = []
    for book_info in book_list:
        if book_info["书名"] == book_name:
            same_book.append(book_info)
    return same_book


def add_book():
    """
    添加图书，编号不能重复，若编号重复提示用户重新输入
    :return:
    """
    book_ids = get_book_id(books)
    while True:
        book_id = input("请输入图书编号：")
        if book_id in book_ids:
            print("您输入的编号已存在，请重新输入")
        else:
            break  # 输入的id不存在时，说明输入正确，退出提示输入图书编号的while循环
    book_name = input("请输入图书名称：")
    book_location = input("请输入图书位置：")
    books.append({"编号": book_id, "书名": book_name, "位置": book_location})
    print("添加完毕，返回菜单页面")


def del_book():
    """
    找到书籍名称，并根据该书籍名称的书籍id删除书籍（删除的编号必须是该书籍名称的编号）
    非常规场景处理：①没有该书籍，②书籍id不正确
    :return:
    """
    while True:
        book_name = input("请输入要删除的书名：")
        li_deletes = get_same_book(book_name)  # 获取要删除的同名书籍的所有信息，每个元素为一个字典
        book_count = len(li_deletes)  # 获取要删除的同名书籍的数量
        books_count = len(books)  # 获取此时所有图书的数量

        if book_count > 0:
            print("找到{}本书籍名为：{}".format(book_count, book_name))
            print_books(li_deletes)  # 输出找到的所有同名书籍的信息

            while len(books) == books_count:  # 当数据删除成功时，时退出while循环
                book_del = input("请选择删除书籍的编号：")
                # 遍历所有找到的同名书籍的信息，根据id进行删除时
                for book_info in li_deletes:
                    if book_del == book_info["编号"]:
                        books.remove(book_info)
                        break  # 编号唯一，只要找到编号，则退出for循环
                else:
                    print("您输入的编号不正确，请重新输入")  # 确保要删除的编号在范围内，否则提示不正确
            break  # 只要有对应的书籍名称，即可退出最外部的while循环，无需再提示用户输入要删除的书名
        else:
            print("未找到您要删除的书籍，请重新输入")
    print("删除完毕，返回菜单页面")


def all_book():
    """
    输出当前所有图书的信息
    :return:
    """
    book_count = len(books)
    if book_count == 0:
        print("当前图书馆没有任何书籍")
    else:
        print("当前共有{}本书籍，所有的图书信息如下；".format(book_count))
        print_books(books)
        print("查询完毕，返回菜单页面")


def library_sys():
    print("------欢迎进入图书管理系统------")
    while True:
        print_menu()  # 打印菜单
        num = input("请输入您的选项：")
        if num == "1":
            add_book()  # 添加图书
        elif num == "2":
            del_book()  # 删除图书
        elif num == "3":
            all_book()  # 查询所有图书
        elif num == "4":
            print("谢谢使用，程序即将关闭")
            break  # 退出程序
        else:
            print("您输入的选项有误，请重新选择")


library_sys()
