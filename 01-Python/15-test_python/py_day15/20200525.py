"""
python打卡第十五天
1、输入一个年月日，如2020-05-25，输出是今年的第几天
2、将以下列表中的所有值存到列表中
li_data = [{"age":15},122,['dsfsdf',[],["jsdfjkls"],{"hhaa":[123,"ert"]}],{"age":[123,456]}]
期望结果res [15,122,dsfsdf,jsdfjkls,123,ert,123,456]

"""
import time


# 方法一：

def time_to_days():
    while True:
        input_time = input("请输入一个年月日，例如：2020-05-25：")
        try:
            struct_time = time.strptime(input_time, "%Y-%m-%d")
            print("{}是今年的第{}天".format(input_time, struct_time.tm_yday))
            break
        except ValueError as e:
            print("输入的格式不正确，请重新输入")


def recursive_traversal_values(obj):
    """
    :param obj:
    :param n:
    :return: list
    """
    return_list = []
    if type(obj) == dict:
        return_list += recursive_traversal_values(list(obj.values()))
    elif type(obj) == list:
        for item in obj:
            return_list += recursive_traversal_values(item)
    else:
        return_list.append(obj)
    return return_list



if __name__ == "__main__":
    li_data = [{"age": 15}, 122, ['dsfsdf', [], ["jsdfjkls"], {"hhaa": [123, "ert"]}], {"age": [123, 456]}]
    print(recursive_traversal_values(li_data))
    #time_to_days()