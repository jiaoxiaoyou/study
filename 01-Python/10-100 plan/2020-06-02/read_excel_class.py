# @Author : jiaojie
# @CreateDate : 2020/6/2 22:02
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

import openpyxl


class ReadExcel(object):
    """读取excel中的用例数据"""
    def __init__(self, file_name, sheet_name):
        """

        :param file_name:
        :param sheet_name:
        """
        self.file_name = file_name
        self.sheet_name = sheet_name

    def open(self):
        """打开工作簿和表单"""
        self.workbook = openpyxl.load_workbook(self.file_name)
        self.sheet = self.workbook[self.sheet_name]

    def read_data(self):
        # 打开文件和表单
        self.open()
        # 按行获取所有的表格对象，每一行的内容放在一个元组中
        rows = list(self.sheet.rows)
        # 创建一个列表cases，存放所有的用例数据
        _cases = []
        # 获取表头
        titles = [row.value for row in rows[0]]
        # 获取最大的行
        max_row = self.sheet.max_row
        # 遍历其他的数据行，和表头进行打包，转换成字典，放在case这个列表中
        for row in rows[1: max_row + 1]:
            data = [r.value for r in row]
            case = dict(zip(titles, data))
            cases.append(case)
        return _cases


if __name__ == '__main__':
    do_excel = ReadExcel('case.xlsx', 'Sheet1')
    cases = do_excel.read_data()
    print(cases)
