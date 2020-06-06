# @Author : 强小林
# @CreateDate : 2020/5/25 11:48
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription : 

"""
python打卡第十五天
1、输入一个年月日，如2020-05-25，输出是今年的第几天
2、将以下列表中的所有值存到列表中
li_data = [{"age":15},122,['dsfsdf',[],["jsdfjkls"],{"hhaa":[123,"ert"]}],{"age":[123,456]}]
期望结果res [15,122,dsfsdf,jsdfjkls,123,ert,123,456]

"""
import re
import time

print("-------------第1题-------------")


def get_date_day(date):
    """根据日期，获取是今年的第几天"""
    try:
        str_date = time.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("您输入的日期不存在，无法计算！")
    else:
        return str_date.tm_yday


def input_date():
    """输入日期"""
    while True:
        input_date = input("请输入一个年月日，格式为%Y-%m-%d：")
        if re.search(r"(\d{4}-\d{1,2}-\d{1,2})", input_date):
            return input_date
        else:
            print("您输入的格式不正确，请重新输入！")


def main_day():
    date = input_date()
    return get_date_day(date)


print(main_day())

print("-------------第2题-------------")

li_data = [{"age": 15}, 122, ['dsfsdf', [], ["jsdfjkls"], {"hhaa": [123, "ert"]}], {"age": [123, 456]}]


def get_all_value(li_data: list):
    """获取所有的值"""
    li_res = list()
    if isinstance(li_data, dict):
        li_res += get_all_value(list(li_data.values()))
    elif isinstance(li_data, list) or isinstance(li_data, list) or isinstance(li_data, list):
        for each_data in li_data:
            li_res += get_all_value(each_data)
    else:
        li_res.append(li_data)
    return li_res


print(get_all_value(li_data))
