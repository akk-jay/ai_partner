# #读文件
#
# #1.打开文件
# file = open('resources/prompt.txt', 'r', encoding='utf-8')  #r:读模式  w:写模式  a:追加模式  rb:二进制读模式  wb:二进制写模式  r+:读写模式  rb+:二进制读写模式  w+:读写模式  wb+:二进制读写模式
# #utf-8:编码格式  ascii:美国信息交换标准代码  gbk:简体中文编码格式  unicode:国际编码格式  utf-16:16位编码格式  utf-32:32位编码格式
# # 打开这个文件会有一个返回值，这个返回值是一个文件对象，通过这个文件对象可以对文件进行读写操作  file  #文件对象   file.read()  #读取文件内容
#
#
# #2.读文件
# # content = file.read()
# # print(content)
#
# content_list = file.readlines()
# for line in content_list:
#     print(line.strip())
#
#
#
# #3.关闭文件
# file.close()




#写文件

# #1.打开文件
# file = open('resources/静夜思.txt', 'w', encoding='utf-8')
#
#
#
# #2.写内容
# file.write('床前明月光，疑是地上霜。\n')
# file.write('举头望明月，低头思故乡。\n')
#
#
#
#
# #3.关闭文件
# file.close()


#
# #================================================文件操作释放资源正确操作================================================
# #1.打开文件
# file = open('resources/静夜思.txt', 'w', encoding='utf-8')
#
#
#
# #2.写内容
# try:
#     file.write('床前明月光，疑是地上霜。\n')
#     file.write('举头望明月，低头思故乡。\n')
#
#
#
# # 3.关闭文件
# finally:
#     file.close()




#================================================使用with语句打开文件(推荐方式）===============================================

with open('resources/静夜思.txt', 'w', encoding='utf-8') as file:
    file.write('床前明月光，疑是地上霜。\n')
    file.write('举头望明月，低头思故乡。\n')

