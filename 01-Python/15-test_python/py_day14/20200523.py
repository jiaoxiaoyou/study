# @Author : jiaojie
# @CreateDate : 2020/5/23 22:40
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
import json
file_path = "library_sys.json"
books = []

def read_books():
    books_list = []
    try:
        with open(file_path, "r", encoding="utf8") as fr:
            books_list = json.load(fr)
    except json.decoder.JSONDecodeError as e:
        print("图书馆暂时没有书")
    finally:
        return books_list


def save_books(content_list=[]):
    """
    将多个图书的数据反序列化成json字符串保存到文件中
    :param content_list:
    :return:
    """
    with open(file_path, "w") as fr:
        json.dump(content_list, fr)


def print_menu():
    """
    输出提示用户的选项
    :return:
    """
    print("-----------------------------------")
    print("【1】：添加图书\n【2】：删除图书\n【3】：显示所有图书\n【4】：退出")

def get_books_id():
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
    books_id = get_books_id()
    while True:
        book_id = input("请输入图书编号：")
        if book_id in books_id:
            print("您输入的编号已存在，请重新输入")
        else:
            break
    book_name = input("请输入图书名称：")
    book_location = input("请输入图书位置：")
    books.append({"编号": book_id, "书名": book_name, "位置": book_location})
    save_books(books)
    print("添加完毕，返回菜单页面")

def get_same_book(book_name):
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
                        save_books(books)
                        break
                else:
                    print("您输入的编号不正确，请重新输入")
            break
        else:
            print("未找到您要删除的图书，请重新输入")
    print("删除完毕，返回菜单页面")


def print_books(books_list):
    """
    输出对应列表的每个书的信息
    :param book_list: 存放书籍信息的list，不一定是所有书籍，所以定义为参数
    :return:
    """
    for book_info in books_list:
        print("编号：{} 书名：{} 位置：{}".format(book_info['编号'], book_info['书名'], book_info['位置']))

def all_books():
    book_count = len(books)
    if book_count == 0:
        print("当前图书馆没有任何图书")
    else:
        print("当前共有{}本图书，所有的图书信息如下：".format(book_count))
        print_books(books)
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
            all_books()
        elif num == "4":
            print("谢谢使用，程序即将关闭")
            break
        else:
            print("您输入的选项有误，请重新选择")


if __name__ == "__main__":
    books = read_books()
    library_sys()

# actual_data = "1234"
# expect_data = "123"
#
# try:
#     assert actual_data == expect_data
#     print("测试用例通过")
# except AssertionError:
#     print("测试用例失败")
# finally:
#     print("测试完毕")


