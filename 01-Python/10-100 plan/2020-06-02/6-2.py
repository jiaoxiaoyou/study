"""
2020-06-02 python 打卡
封装一个类从case.xlsx中读数据并组装成以下格式：
[
{'case_id': 1, 'data': "{'python1','123456','123456'}", 'excepted': '{"code":1,"msg":"注册成功"}'},
{'case_id': 2, 'data': "{'python1','123456','12345'}", 'excepted': '{"code":0,"msg":"两次密码不一致"}'},
{'case_id': 3, 'data': "{'python18','123456','123456'}", 'excepted': '{"code":0,"msg":"该账户已存在"}'}
]
"""
import xlrd
class ExcelData():
    def __init__(self, data_path, sheetname):
        self.data_path = data_path
        self.sheetname = sheetname
        self.data = xlrd.open_workbook(self.data_path)
        self.table = self.data.sheet_by_name(self.sheetname)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def readExcel(self):
        datas = []
        for i in range(1, self.rowNum):
            sheet_data = {}
            for j in range(self.colNum):
                c_cell = self.table.cell_value(i, j)
                sheet_data[self.keys[j]] = c_cell
            datas.append(sheet_data)
        return datas
if __name__ == "__main__":
    data_path = "C:/Users/Administrator/PycharmProjects/istester100_001/venv/2020-study/case.xlsx"
    sheetname = "Sheet1"
    get_data = ExcelData(data_path, sheetname)
    datas = get_data.readExcel()
    for i in  datas:
        print(i)
