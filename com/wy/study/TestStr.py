'''
Created on 2018年5月26日

@author: wanyang
    in:包含,相当于contains
    cmp:比较序列值,不好用
    +:python的+只能是字符串之间的相连,str+int会报错
'''

str1 = "qwertyuiop";
# 截取下标为1到4的字符串,含头不含尾,返回一个新的字符串
print(str1[1:4]);
# 截取字符串,根据最后一个参数,从第一个开始(截取后的字符串加上第一个),
#依次加上最后一个参数的下表长度截取字符串,知道超出该字符串长度
str2 = str1[::2];
print(str2)
# 从1到6,隔下标2截取字符串
print(str1[1:6:2]);