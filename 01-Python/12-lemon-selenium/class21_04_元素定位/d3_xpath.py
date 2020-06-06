# @Author : jiaojie
# @CreateDate : 2020/5/17 20:03
# @Description : 
# @UpdateAuthor : 
# @LastUpdateTime : 
# @UpdateDescription :

"""
1. 相对路径更简洁
2. 绝对路径不灵活

//相对路径

/绝对路径：/html/body/

//标签名称
* 号是通配符，表示匹配某一个标签名，属性
[]条件， 属性=  id=  name=
. 当前节点
.. 父节点
@ 选择属性

后面的 / 子层级
后面的// 子孙层级

索引去表示xpath的时候，养成加括号的习惯
xpath 索引是优先级很高的


@ 条件组合
//input[@name]
//div/input[@*='wd']

and  or

class 有空格

//a[contains(text(), '地图')]
//span[contains(@class, 'wk')]


"""