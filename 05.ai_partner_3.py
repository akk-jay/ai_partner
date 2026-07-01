from random import choices

import streamlit as st
import os
from openai import OpenAI

print('重新执行本文件，渲染展示页面')

#设置页面的配置项
st.set_page_config(
    page_title="AI Partner", #整个网页的标题
    page_icon="🎡",
    layout="wide",#控制整个网页的布局
    initial_sidebar_state="expanded",#控制侧边栏的状态
    menu_items={

    }
)




#大标题
st.title("AI Partner")

#logo
st.logo('./resources/cat.jpg')

#系统提示词
system_prompt = """
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。:规则:
1.每次只回1条消息
2.禁止任何场景或状态描述性文字
3.匹配用户的语言
4.回复简短，像微信聊天一样
5.有需要的话可以用emoji表情
6.用符合伴侣性格的方式对话
7.回复的内容，要充分体现伴侣的性格特征
伴侣性格:%s
伴侣性别:%s
你必须严格遵守上述规则来回复用户
"""

#初始化聊天信息
if 'messages' not in st.session_state:   #messages: 聊天信息  #如果session_state中没有messages，则初始化一个空列表   session_state:会话状态
    st.session_state.messages = []    #st.session_state.messages: 聊天信息
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = '苏西'      #如果session_state中没有nick_name，则初始化一个值，同上
if 'gender' not in st.session_state:
    st.session_state.gender = '女生'      #如果session_state中没有gender，则初始化一个值，同上     后面都是设置的默认值
if 'nature' not in st.session_state:
    st.session_state.nature = '文静温柔的姑娘'    #如果session_state中没有nature，则初始化一个值，同上



#左侧的侧边栏   with:streamlit中上下文管理器
# st.sidebar.subheader("伴侣信息")
# st.sidebar.text_input("昵称")
# st.sidebar.text_input("性别")
# st.sidebar.text_input("性格")
with st.sidebar:
    st.subheader("伴侣信息")
    #昵称
    nick_name = st.text_input("昵称",value=st.session_state.nick_name)
    if nick_name:                                    #如果nick_name有值的话，把nick_name的值赋给st.session_state.nick_name
        st.session_state.nick_name = nick_name
    #性别
    gender = st.text_input("性别",value=st.session_state.gender)
    if gender:                                    #如果gender有值的话，把gender的值赋给st.session_state.gender
        st.session_state.gender = gender
    #性格
    nature = st.text_area("性格",value=st.session_state.nature)  #text_area: 文本区域
    if nature:                                    #如果nature有值的话，把nature的值赋给st.session_state.nature
        st.session_state.nature = nature




#展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])  #
    # if message['role'] == 'user':
    #     st.chat_message('user').write(message['content'])
    # elif message['role'] == 'assistant':
    #     st.chat_message('assistant').write(message['content'])



#消息输入框
prompt = st.chat_input("你想文什么?")
if prompt:  #字符串会自动转化为布尔值，如果字符串为非空，则为True;否则为False
    # st.write(f"User has sent the following prompt: {prompt}")
    st.chat_message('user').write(prompt)
    print('---------------->ai调用大模型，prompt',prompt)
    #将用户消息添加到聊天信息中
    st.session_state.messages.append({"role": "user", "content": prompt})


#创建与ai大模型交互的客户对象（DEEPSEEK_API_KEY环境变量的名字就是大模型的密钥）
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")
#与ai大模型进行交互（参数）

    # print([
    #         {"role": "system", "content": system_prompt},
    #         *st.session_state.messages
    #     ])

    response = client.chat.completions.create(
        model="deepseek-v4-pro",  # 模型名称
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature, st.session_state.gender)},  # 系统角色
            # {"role": "user", "content": prompt},  # 用户角色
            *st.session_state.messages
        ],
        stream=True,  # 是否流式返回
        reasoning_effort="high",  # 理解努力程度
        extra_body={"thinking": {"type": "enabled"}}  # 额外的请求体
    )
#输出大模型返回的结果（非流式输出的解析方式）
    # print('-----------------------------大模型返回的结果:',response.choices[0].message.content)
    # st.chat_message('assistant').write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})


# 输出大模型的返回结果（流式输出的解析方式）
    response_message = st.empty()    #创建一个空组件，用来显示大模型的返回结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message('assistant').write(full_response)  # 输出内容


    #将大模型返回结果添加到聊天信息中
    st.session_state.messages.append({"role": "assistant", "content": full_response})



