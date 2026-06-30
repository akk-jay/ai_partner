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
system_prompt = "你是苏西，是一个可爱的助手，你很乐意帮助用户回答问题"


#初始化聊天信息
if 'messages' not in st.session_state:   #messages: 聊天信息  #如果session_state中没有messages，则初始化一个空列表   session_state:会话状态
    st.session_state.messages = []    #st.session_state.messages: 聊天信息

for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])
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
            {"role": "system", "content": system_prompt},  # 系统角色
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



