import streamlit as st


#设置页面的配置项
import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App", #整个网页的标题
    page_icon="🧊",
    layout="wide",#控制整个网页的布局
    initial_sidebar_state="expanded",#控制侧边栏的状态
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



#大标题
st.title("一及标题")
st.header('二及标题')
st.subheader('三及标题')


#段落文字
st.write('《紫罗兰永恒花园》是京都动画打造的治愈系经典动漫，以细腻唯美的画风与温柔深刻的叙事打动无数观众。故事背景设定在硝烟散尽的架空战后时代，少女薇尔莉特曾是被当作战争武器的少年兵，不懂人情冷暖，没有自我与情绪，一生都在听从命令、奔赴战场。残酷的战争夺走了她的双臂，也让她遗失了感知温柔的能力。')
st.write('战争落幕之后，薇尔莉特褪去战士身份，成为一名自动手记人偶，以代写书信为生。她穿梭于世间各个角落，为不同的人执笔写信，记录思念、遗憾、告白与离别。在一封封信件的书写过程中，她亲眼见证人间百态，慢慢读懂亲情、爱情与羁绊的意义，一点点褪去冰冷，学会感知与共情')
st.write('整部作品没有激烈的冲突，却以温柔的笔触诠释成长与救赎。薇尔莉特始终追寻着少佐那句 “我爱你” 的真谛，在自我救赎的路上慢慢成为温柔而强大的人。它告诉观众，爱藏在细碎的温柔里，所有历经伤痛的成长，终会开出温柔永恒的花')


#图
st.image('./resources/cat.jpg')
#音频
st.audio('./resources/音频.mp3')
#视频
st.video('./resources/视频.mp4')
#logo
st.logo('./resources/cat.jpg')
#表格
student_data = {
    'name':['1','2','3','4','5','6'],
    'age':[21,22,23,24,25,26],
    'shux':[32,323,45,634,55,43]
}
st.table(student_data)
#输入框
name = st.text_input('请输入name')
st.write(f'您输入的姓名为:{name}')

password = st.text_input('请输入密码',type='password')
st.write(f'密码:{(password)}')
#单选按键
gender = st.radio('请输入你的性别',['男','女','未知'],index=2)
st.write(f'您的性别为:{gender}')