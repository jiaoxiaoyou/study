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
    def __init__(self, root_dir):
        self.root_dir = os.path.abspath(root_dir)

    @staticmethod
    def is_file_size_gt(file_path, min_size=1024):
        ret_file_size = 0
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            if file_size > min_size:
                ret_file_size = file_size
        return ret_file_size

    def traverse_dir(self, dst_dir):
        files_path = []
        for entry in os.listdir(dst_dir):
            full_path = os.path.join(dst_dir, entry)
            if os.path.isdir(full_path):
                files_path += self.traverse_dir(full_path)
            else:
                files_path.append(full_path)
        return files_path

    def get_file_list_gt_than(self, min_size):
        files_path = self.traverse_dir(self.root_dir)
        dst_files_path = {}
        for file_path in files_path:
            dst_file_size = file_system.is_file_size_gt(file_path, min_size)
            if dst_file_size > 0:
                dst_files_path[file_path] = dst_file_size

        if dst_files_path:
            for file_path, file_size in dst_files_path.items():
                print("%s - %s" % (file_path, file_size))


if __name__ == "__main__":
    path = input("请输入一个目录路径：")
    file_system = FileSystem(path)
    file_system.get_file_list_gt_than(1024)