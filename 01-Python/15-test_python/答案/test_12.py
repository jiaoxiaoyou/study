# @Author : 强小林
# @CreateDate : 2020/5/20 15:23
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第十二天
1、从test_12.txt中读取内容，输出内容格式为
[{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '13760246701', 'pwd': '123456'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'http://119.23.241.154:8080/futureloan/mvc/api/member/login', 'mobilephone': '15678934551', 'pwd': '234555'}]

2、实现一个文件复制器函数，指定原始复制路径（从哪复制）和复制目的路径（复制到哪），只复制文件，目录不用复制
"""
import os


def get_data(file_name, mode="r"):
    file_data = []
    file = open(file_name, mode, encoding="utf8")

    for each_line in file.readlines():
        dict_data = {}
        each_line = each_line.strip("\n")  # 去掉每一行后换行的\n
        for data in each_line.split(","):
            li_data = data.split(":", 1)  # 考虑到url有多个冒号，所以给定参数2，用第1个冒号进行分割
            dict_data[li_data[0]] = li_data[1]
        file_data.append(dict_data)

    file.close()
    return file_data


res = get_data("test_12.txt")
print("从文件中读取到的数据为：\n{}".format(res))


# 第2题还有很多方法，比如使用shutil.copy、os.system等实现，可自行扩展

def file_copy(file_path, new_path):
    try:
        os.chdir(file_path)  # 切换工作目录，参数为绝对路径
        for each_file in os.listdir("."):  # .表示当前目录下，即上一步切换后的工作目录下
            if os.path.isfile(each_file):  # 必须判断是文件，防止存在目录
                with open(each_file, "r", encoding="utf8") as f:
                    content = f.read()  # 先读

                path = os.path.join(new_path, "cp_" + each_file)  # 拼接路径
                with open(path, "w", encoding="utf8") as f:
                    f.write(content)  # 后写
    except Exception as e:
        print("程序出现异常：{}".format(e))


file_copy(r"D:\workspace\python\test_python\src_test_12", r"D:\workspace\python\test_python\dest_test_12")
