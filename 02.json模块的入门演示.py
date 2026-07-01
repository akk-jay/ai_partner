#写入json数据文件
import json
# user = {'name': '张三',
#         'age': 18,
#         'hobbies':['reading','swimming'],
#         'gender':'male'}
#
# with open('resources/user.json','w',encoding='utf-8') as f:
# #ensure_ascii=False:默认为True，确保所有的数据输出都是ascii编码（中文为非ascii码，非ascii会被转义）；#False，非ascii码保留原样输出
# # indent=2:会在输出的json格式中添加缩进（格式化）
#     json.dump(user,f,ensure_ascii=False,indent=2)





#读取json数据文件
with open('resources/user.json','r',encoding='utf-8') as f:
    user = json.load(f)
    print(user)
    print(type(user))