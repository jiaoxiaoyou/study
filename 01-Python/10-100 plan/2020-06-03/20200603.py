# @Author : jiaojie
# @CreateDate : 2020/6/03 18:18
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
python打卡
1、从test_12.txt中读取内容，输出内容格式为
[{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '13760246701', 'pwd': '123456'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'}]

2、实现一个文件复制器函数，指定原始复制路径（从哪复制）和复制目的路径（复制到哪），只复制文件，目录不用复制

"""
import os
from shutil import copyfile
import glob


def read_lines(file_name, mode='r'):
    fr = open(file_name, mode, encoding='utf8')
    # 所有url
    files_list = []
    # 每个 url
    file_dict = {}
    for line in fr.readlines():
        for items in line.split(','):
            item = items.split(':',1)
            file_dict[item[0]] = item[1]
        files_list.append(file_dict)
    return files_list

    # 一定要关闭文件
    fr.close()

res = read_lines("test_12.txt")
print("从文件中读取到的数据为：\n{}".format(res))


def copy_file(src_path, dst_path):
    os.chdir(src_path)
    for src_file in glob.glob('*'):
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        if os.path.isfile(src_file):
            copyfile(src_file,dst_path+src_file)
            print("成功的把{}复制到{}".format(src_path+"/"+src_file, dst_path+src_file))

#copy_file(r"./",r'./test/')


def copy2_file(src_path, dst_path):
    try:
        os.chdir(src_path)
        for src_file in os.listdir("."):
            print(src_file)
            if os.path.isfile(src_file):
                # 读取每一个文件
                with open(src_file, 'r', encoding="utf8") as f:
                    src_content = f.read()
                # 重写每一个文件
                if not os.path.exists(dst_path):
                    os.mkdir(dst_path)
                new_path = os.path.join(dst_path, "cp_" + src_file)
                print(new_path)
                with open(new_path, "w", encoding="utf8") as f:
                    f.write(src_content)
    except Exception as e:
        print("程序出现异常：{}".format(e))


copy2_file(r"./",r'./test/')







