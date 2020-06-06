# @Author : jiaojie
# @CreateDate : 2020/5/21 16:02
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""

python打卡第十三天
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
# book1 = {'id':1, 'name': "MySQL", 'location': '1-1-001'}
# book2 = {'id':2, 'name': "Linux", 'location': '1-1-002'}
# book3 = {'id':3, 'name': "selenium", 'location': '1-1-003'}
# book4 = {'id':4, 'name': "Python", 'location': '1-1-004'}
# book5 = {'id':5, 'name': "PHP", 'location': '1-1-005'}

books = []

def add(id, name='', location=''):
    book_dict = {}
    book_dict['id'] = id
    book_dict['name'] = name
    book_dict['location'] = location
    books.append(book_dict)


def delete(name):
    del_book_lists = []
    del_id_list = []
    for book in books:
        if name == book['name']:
            del_book_lists.append(book)
    print("图书名为：{0}的所有数据：{1}".format(name, del_book_lists))
    del_id = input('请输入要删除的图书编号:')
    for book in books:
        if del_id == book['id']:
            books.remove(book)
    print("剩余的图书：",books)


def show_book_list():
    print(books)

print("样例：1,Python,1-1-001")
book_count = 0
while book_count < 5:
    book = input("请输入图书编号、图书名、图书位置，用英文逗号(,)隔开：")
    #print(book)
    book_list = book.split(',')
    if len(book_list) == 3:
        book_count += 1
        add(book_list[0], book_list[1], book_list[2])
    else:
        print("输入的图书信息不正确")

show_book_list()
del_book = input("请输入要删除的图书名：")
delete(del_book)
