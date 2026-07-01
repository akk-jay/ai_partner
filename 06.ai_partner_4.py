from random import choices
import datetime
import json

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



#保存会话信息函数
def save_session():
    if st.session_state.session_id:
        # 构建新的会话对象
        session_data = {"session_id": st.session_state.session_id,
                        "nick_name": st.session_state.nick_name,
                        "gender": st.session_state.gender,
                        "nature": st.session_state.nature,
                        "messages": st.session_state.messages}
        # 如果 session 不存在，则创建
        if not os.path.exists("sessions"):
            os.makedirs("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.session_id}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#生成会话标识
def gen_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")




#加载所有会话列表信息
def load_sessions():     # load_sessions:加载所有会话列表信息
    sessions_list = []     # sessions: 会话列表
    # 加载sessions目录下的文件
    if os.path.exists("sessions"): # 判断sessions目录是否存在
        for file in os.listdir("sessions"): # 遍历sessions目录下的所有文件   listdir: 列出目录的文件和子目录
            if file.endswith(".json"): # 判断文件是否以.json结尾
                sessions_list.append(file[:-5:]) # 将文件名添加到会话列表中，[:-5:]表示去掉文件名的后缀.json
    sessions_list.sort(reverse=True)  # 对会话列表进行排序
    return sessions_list


#加载指定会话信息
def load_session(session_name):
    if os.path.exists(f"sessions/{session_name}.json"):  #判断指定会话文件是否存在
        #读取会话数据
        try:
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.session_id = session_name
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.gender = session_data["gender"]
                st.session_state.nature = session_data["nature"]
                st.session_state.messages = session_data["messages"]
        except Exception:
            st.error("加载会话失败")




#删除会话信息的函数
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")   #remove: 删除文件
            #如果删除的是当前会话，，则需要更新会话列表
            if session_name == st.session_state.session_id:
                st.session_state.messages = []
                st.session_state.session_id = gen_session_name()
    except Exception:
        st.error("删除会话失败")






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
#会话标识（给当前会话起个名字，当前时间）
if 'session_id' not in st.session_state:
    st.session_state.session_id = gen_session_name()







#左侧的侧边栏   with:streamlit中上下文管理器
# st.sidebar.subheader("伴侣信息")
# st.sidebar.text_input("昵称")
# st.sidebar.text_input("性别")
# st.sidebar.text_input("性格")
with st.sidebar:
    st.subheader("AI控制面板")

    #新建会话
    if st.button("新建会话",width='stretch',icon="🚀"):
        #1.保存当前会话的聊天信息
        save_session()
        #2.创建新会话
        if st.session_state.messages:
            st.session_state.session_id = gen_session_name()
            st.session_state.messages = []
            save_session()
            st.rerun()  # 重新运行当前页面

   #会话历史
    st.text("会话历史")           #输出普通文本
    sessions_list = load_sessions()
    for session in sessions_list:
        col1, col2 = st.columns([4,1])
        with col1:
            #加载会话信息
            #三元运算符：如果条件为真，则返回第一个表达式的值，否则，返回第二个返回时的值 -- >语法：值1  if  条件  else 值二
            if st.button(session,width='stretch',icon="✉️", key=f"load_{session}", type='primary' if session == st.session_state.session_id else 'secondary'):
                load_session(session)
                st.rerun()
        with col2:
            #删除会话信息
            if st.button("",width='stretch',icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()
        # st.button(session,width='stretch',icon="✉️")
        # st.button("",width='stretch',icon="❌️")

#分割线
    st.markdown("___")



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
st.text(f'会话名称：{st.session_state.session_id}')
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])  #
    # if message['role'] == 'user':
    #     st.chat_message('user').write(message['content'])
    # elif message['role'] == 'assistant':
    #     st.chat_message('assistant').write(message['content'])





#消息输入框
prompt = st.chat_input("你想问什么?")
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


    #保存会话信息
    save_session()



