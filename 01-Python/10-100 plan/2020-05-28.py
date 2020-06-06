# @Author : jiaojie
# @CreateDate : 2020/5/28 21:51
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
7.把电脑某个目录下，所有超过1兆的文件列出来
"""
import os


class FileSystem(object):
    def __init__(self, dir_path, min_size):
        self.dir_path = os.path.abspath(dir_path)
        self.min_size = min_size

    def find_file(self, path):
        files_list = []
        for file_or_dir in os.listdir(path):
            abs_path = os.path.join(path, file_or_dir)
            if os.path.isdir(abs_path):
                files_list += self.find_file(abs_path)
            else:
                files_list.append(abs_path)
        return files_list

    def find_greater_file(self):
        files_list = self.find_file(self.dir_path)
        for file in files_list:
            if os.path.isfile(file):
                file_size = os.path.getsize(file)
                if file_size > self.min_size:
                    print("{} - {}".format(file, file_size))


if __name__ == "__main__":
    path = input("请输入一个目录路径：")
    file_system = FileSystem(path, 1024)
    file_system.find_greater_file()