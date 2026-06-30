import streamlit as st
import os
from openai import OpenAI



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

#消息输入框
prompt = st.chat_input("你想文什么?")
if prompt:  #字符串会自动转化为布尔值，如果字符串为非空，则为True;否则为False
    # st.write(f"User has sent the following prompt: {prompt}")
    st.chat_message('user').write(prompt)
    print('---------------->ai调用大模型，prompt',prompt)





#创建与ai大模型交互的客户对象（DEEPSEEK_API_KEY环境变量的名字就是大模型的密钥）
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")
#与ai大模型进行交互（参数）
    response = client.chat.completions.create(
        model="deepseek-v4-pro",  # 模型名称
        messages=[
            {"role": "system", "content": system_prompt},  # 系统角色
            {"role": "user", "content": prompt},  # 用户角色
        ],
        stream=False,  # 是否流式返回
        reasoning_effort="high",  # 理解努力程度
        extra_body={"thinking": {"type": "enabled"}}  # 额外的请求体
    )
#输出大模型返回的结果
    print('大模型返回的结果',response.choices[0].message.content)
    st.chat_message('assistant').write(response.choices[0].message.content)




