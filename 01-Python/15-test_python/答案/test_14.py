# @Author : 强小林
# @CreateDate : 2020/5/22 10:22
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""

python打卡第十四天
1、将昨天的图书管理系统，通过文件来实现书籍数据的永久存储
（提示：进入系统时先读文件数据，退出系统后再全部重新写入数据）
2、
actual_data = "1234"  # 实际值
expect_data = "123"  # 期望值
断言实际值和期望值是否一致，如果一致输出测试用例通过，如果不一致输出测试用例失败，无论是否通过，都输出测试完毕
（提示：要用到异常处理，断言失败的异常是AssertionError）

"""

print("-------------------第2题-------------------")

actual_data = "1234"  # 实际值
expect_data = "123"  # 期望值
try:
    assert actual_data == expect_data
except AssertionError:
    print("测试用例未通过")
else:
    print("测试用例通过")
finally:
    print("测试完毕")

print("-------------------第1题-------------------")


class LibrarySystem(object):
    """图书管理系统"""
    all_books = []

    def __init__(self, file_name):
        self.file_name = file_name

    def file_read(self, file_name):
        """
        读取文件内容，并更新至类属性all_books中
        :param file_name: 要读取的文件名
        :return: 文件中的书籍信息
        """
        try:
            with open(file_name, "r", encoding="utf8") as f:
                txt = f.readlines()
            for book_info in txt:
                self.all_books.append(eval(book_info))  # 默认为字符串，需要转换为原本的表达式，即dict
        except:  # 有异常则新建目录，内容为空
            with open(file_name, "w", encoding="utf8") as f:
                f.write("")
        return self.all_books

    def file_write(self, file_name):
        """
        向文件中写入内容，清空写入。由于删除无法处理，所以清空，将整个all_books全部重新写入
        :param file_name: 要写入的文件名
        :return:
        """
        try:
            with open(file_name, "w", encoding="utf8") as f:
                for book_info in self.all_books:
                    f.write(str(book_info) + "\n")  # 数据本身为dict，需要转换为str才能写入
        except Exception as e:
            print("程序出现异常：{}".format(e))

    def print_menu(self):
        """
        输出提示用户的菜单
        :return:
        """
        print("-" * 30)
        print("【1】：添加图书\n【2】：删除图书\n【3】：显示所有图书\n【4】：退出")

    def print_books(self, list_books):
        """输出对应列表的每个书的信息"""
        for book_info in list_books:
            print("编号:{} 书名:{} 位置:{}".format(book_info["编号"], book_info["书名"], book_info["位置"]))

    def get_book_id(self):
        """获取所有图书的编号值，存入列表中"""
        book_ids = []
        for book_info in self.all_books:
            book_ids.append(book_info["编号"])
        return book_ids

    def get_same_book(self, book_name):
        """
        获取指定库中，同一书名的书籍的信息
        :param book_name:书籍名称
        :return:相同书名的书籍的信息
        """
        same_book = []
        for book_info in self.all_books:
            if book_info["书名"] == book_name:
                same_book.append(book_info)
        return same_book

    def add_book(self):
        """
        添加图书，编号不能重复，若编号重复提示用户重新输入
        :return:
        """
        dict_add = {}
        book_ids = self.get_book_id()
        while True:
            dict_add["编号"] = input("请输入图书编号：")
            if dict_add["编号"] in book_ids:
                print("您输入的编号已存在，请重新输入")
            else:
                break  # 输入的id不存在时，说明输入正确，退出提示输入图书编号的while循环
        dict_add["书名"] = input("请输入图书名称：")
        dict_add["位置"] = input("请输入图书位置：")
        self.all_books.append(dict_add)
        print("添加完毕，返回菜单页面")

    def del_book(self):
        """
        找到书籍名称，并根据该书籍名称的书籍id删除书籍（删除的编号必须是该书籍名称的编号）
        非常规场景处理：①没有该书籍，②书籍id不正确
        :return:
        """
        while True:
            book_name = input("请输入要删除的书名：")
            li_deletes = self.get_same_book(book_name)  # 获取要删除的同名书籍的所有信息，每个元素为一个字典
            book_count = len(li_deletes)  # 获取要删除的同名书籍的数量
            books_count = len(self.all_books)  # 获取此时所有图书的数量

            if book_count > 0:
                print("找到{}本书籍名为：{}".format(book_count, book_name))
                self.print_books(li_deletes)  # 输出找到的所有同名书籍的信息

                while len(self.all_books) == books_count:  # 当数据删除成功时，时退出while循环
                    book_del = input("请选择删除书籍的编号：")
                    # 遍历所有找到的同名书籍的信息，根据id进行删除时
                    for book_info in li_deletes:
                        if book_del == book_info["编号"]:
                            self.all_books.remove(book_info)
                            break  # 编号唯一，只要找到编号，则退出for循环
                    else:
                        print("您输入的编号不正确，请重新输入")  # 确保要删除的编号在范围内，否则提示不正确
                break  # 只要有对应的书籍名称，即可退出最外部的while循环，无需再提示用户输入要删除的书名
            else:
                print("未找到您要删除的书籍，请重新输入")
        print("删除完毕，返回菜单页面")

    def all_book(self):
        """
        输出当前所有图书的信息
        :return:
        """
        book_count = len(self.all_books)
        if book_count == 0:
            print("当前图书馆没有任何书籍")
        else:
            print("当前共有{}本书籍，所有的图书信息如下；".format(book_count))
            self.print_books(self.all_books)
            print("查询完毕，返回菜单页面")

    def main_library(self):
        print("------欢迎进入图书管理系统------")
        self.all_books = self.file_read(self.file_name)
        while True:
            self.print_menu()  # 打印菜单
            num = input("请输入您的选项：")
            if num == "1":
                self.add_book()  # 添加图书
            elif num == "2":
                self.del_book()  # 删除图书
            elif num == "3":
                self.all_book()  # 查询所有图书
            elif num == "4":
                print("谢谢使用，程序即将关闭")
                break  # 退出程序
            else:
                print("您输入的选项有误，请重新选择")
        self.file_write(self.file_name)


library_sys = LibrarySystem(r"D:\workspace\python\test_python\library.txt")
library_sys.main_library()
