"""
re解析  重点
bs4解析
xpath解析  重点
pyquery解析
"""

# 正则表达式
"""
元字符
.  除换行外任意字符；
\w 数字、字母和下划线；
\s 任意空白符
\d 数字
\n
\t
^  以什么为开头
$  以什么为结束
\W
\S
\D
a|b
() 分组
[...] 字符组  [a-zA-Z0-9]=[/w]
[^...] 除了字符组以外的
---------------------------------------
量词
*  重复零次或更多次
+  重复一次或更多次 \d+
？ 重复零次或一次
{n} 重复n次 
{n，} 重复n次或更多次
{n，m} 重复n次到m次
----------------------------------------
.*贪婪匹配  尽可能多的去匹配
.*?惰性匹配  尽可能少的去匹配，回溯算法
"""
import re
import requests

res = re.findall(r'\d+', 'sdfsa21323asdf2cvafs')
res_two = re.finditer(r'\d+', 'sdfsa21323asdf2cvafs')  # 生成迭代器
res_three = re.search(r'\d+', 'sdfsa21323asdf2cvafs')  # 只会匹配到第一次内容
res_four = re.match(r'\d+', 'sdfsa21323asdf2cvafs')  # match,在匹配是从字符穿开始进行匹配，等于在匹配字符前加^
print(res)
for i in res_two:
    print(i.group())  # 从匹配结果拿数据，提升效率
print(res_three.group())
print(res_four)

# 预加载
item = 'asdf1233aa'
obj = re.compile(r'\d+')
obj.finditer(item)
print(obj.findall(item))

sentence = """
<dic class='西游记'><span id='10010'>中国移动</span></div>
<dic class='西游记'><span id='10011'>中国联通</span></div>
"""
# 想要那数据需要用（）括起来
# （?p<名字>正则）      分组起名字,用迭代器那数据
# 提取数据需要：group(名字)
obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
resault = obj.finditer(sentence)
for i in resault:
    print(i.group('id'))