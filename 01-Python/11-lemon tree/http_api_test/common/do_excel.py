# @Author : 小坚强
# @StudentId : 2188
# @Time : 2019/8/23 14:31

import openpyxl


class CaseData(object):
    """测试用例数据类"""

    def __init__(self, *args, **kwargs):
        """
        :param args: args可以获取元组，等同于zip_obj，即(<zip object at 0x000000E613872E48>)
        :param kwargs: kwargs可以获取字典，读取出来的数据有多个字段时可用此，暂时没有遇到，先放到这不处理
        """
        for data in list(*args):  # zip对象转为list后可获取到数据
            setattr(self, *data)  # *data等同于data[0]，data[1]，即表头、值


class DoExcel(object):
    def __init__(self, file_n, sheet_n):
        self.file_name = file_n
        self.sheet_name = sheet_n

    def open_file(self):
        """打开文件并定位到指定表单"""
        # 1、打开工作簿
        self.wb = openpyxl.load_workbook(self.file_name)
        # 2、选中指定表单
        self.sh = self.wb[self.sheet_name]

    def read_data(self):
        """读取表单的内容，返回测试数据对象"""
        # 1、打开工作簿并选中对应表单
        self.open_file()

        # 2、读取数据
        all_case = []  # 空列表，用于存放所有用例数据
        rows = list(self.sh.rows)  # 读取表单所有行的数据

        # 将表头放入列表中，加判断防止表头为空
        titles = [r.value for r in rows[0] if r.value]

        for row in rows[1:]:
            data = [r.value for r in row]
            # 通过打包数据，获得zip对象
            zip_obj = zip(titles, data)
            # 通过CaseData创建实例对象，参数为：zip_obj
            case_data = CaseData(zip_obj)
            # 将测试用例对象添加到列表中
            all_case.append(case_data)
        return all_case

    def write_data(self, **kwargs):
        """向单元格中写入数据"""
        # 1、打开工作簿并选中对应表单
        self.open_file()
        # 2、写入数据
        self.sh.cell(**kwargs)  # 调用时拆包
        # 3、保存文件
        self.wb.save(self.file_name)
