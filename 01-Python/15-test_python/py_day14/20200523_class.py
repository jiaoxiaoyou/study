# @Author : jiaojie
# @CreateDate : 2020/5/24 21:19
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

import json
import os


class Library:
    def __init__(self, lib_path):
        real_lib_path = os.path.abspath(lib_path)
        if not os.path.exists(real_lib_path):
            print("Error: Not Found Library File - %s" % lib_path)
        self.lib_path = real_lib_path
        self.books = []
        self._init()

    def _init(self):
        try:
            with open(self.lib_path, "r", encoding="utf8") as fr:
                self.books = json.load(fr)
        except json.decoder.JSONDecodeError as e:
            pass
        except FileNotFoundError as e:
            pass

    def print_books(self, target_books=[]):
        books = target_books if target_books else self.books
        for book in books:
            print("编号：{} 书名：{} 位置：{}".format(book['id'], book['name'], book['location']))
        if not books:
            print("No Books Information")

    def find_books_by_name(self, book_name=''):
        dst_books = []
        for book in self.books:
            if book['name'] == book_name:
                dst_books.append(book)
        return dst_books

    def add_book(self):
        while True:
            book_id = input("请输入图书编号：")
            is_found = False
            for book in self.books:
                if book['id'] == book_id:
                    print("您输入的编号已存在，请重新输入")
                    is_found = True
            if not is_found:
                break

        book_name = input("请输入图书名称：")
        book_location = input("请输入图书位置：")
        self.books.append({"id": book_id, "name": book_name, "location": book_location})
        self.save_books()
        print("添加完毕，返回菜单页面")

    def del_book(self):
        while True:
            del_book_name = input("请输入要删除的图书名：")
            del_books_list = self.find_books_by_name(del_book_name)
            books_count = len(self.books)

            if del_books_list:
                print("找到{}本书籍名为：{}".format(len(del_books_list), del_book_name))
                self.print_books(del_books_list)

                while len(self.books) == books_count:
                    del_book_id = input("请输入要删除图书的编号：")
                    for del_book in del_books_list:
                        if del_book_id == del_book['id']:
                            self.books.remove(del_book)
                            self.save_books()
                            break
                    else:
                        print("您输入的编号不正确，请重新输入")
                break
            else:
                print("未找到您要删除的图书，请重新输入")
        print("删除完毕，返回菜单页面")

    def print_menu(self):
        print("-----------------------------------")
        print("【1】：添加图书\n【2】：删除图书\n【3】：显示所有图书\n【4】：退出")

    def save_books(self):
        with open(self.lib_path, "w") as fr:
            json.dump(self.books, fr)

    def run(self):
        while True:
            self.print_menu()
            num = input("请输入您的选项：")
            if num == "1":
                self.add_book()
            elif num == "2":
                self.del_book()
            elif num == "3":
                self.print_books()
            elif num == "4":
                print("谢谢使用，程序即将关闭")
                break
            else:
                print("您输入的选项有误，请重新选择")


if __name__ == "__main__":
    library = Library("library_2.json")
    library.run()
