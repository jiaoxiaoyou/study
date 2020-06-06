# @Author : jiaojie
# @CreateDate : 2020/6/2 11:11
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
2020-06-02 python 打卡
封装一个类从case.xlsx中读数据并组装成以下格式：
[
{'case_id': 1, 'data': "{'python1','123456','123456'}", 'excepted': '{"code":1,"msg":"注册成功"}'},
{'case_id': 2, 'data': "{'python1','123456','12345'}", 'excepted': '{"code":0,"msg":"两次密码不一致"}'},
{'case_id': 3, 'data': "{'python18','123456','123456'}", 'excepted': '{"code":0,"msg":"该账户已存在"}'}
]

"""

import openpyxl

workbook = openpyxl.load_workbook('case.xlsx')
sheet = workbook['Sheet1']
# 按行获取所有的表格对象，每一行的内容放在一个元组中
rows = list(sheet.rows)
# 创建一个列表cases，存放所有的用例数据
cases = []
# 获取表头
titles = [row.value for row in rows[0]]
# 获取最大的行
max_row = sheet.max_row
# 遍历其他的数据行，和表头进行打包，转换成字典，放在case这个列表中
for row in rows[1: max_row+1]:
    data = [r.value for r in row]
    case = dict(zip(titles, data))
    cases.append(case)
print(cases)
