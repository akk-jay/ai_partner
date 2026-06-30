# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

#创建与ai大模型交互的客户对象（DEEPSEEK_API_KEY环境变量的名字就是大模型的密钥）
client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),  # 大模型的密钥
        base_url="https://api.deepseek.com")  # 大模型的地址

#与ai大模型进行交互（参数）
response = client.chat.completions.create(
        model="deepseek-v4-pro",  # 模型名称
        messages=[
            {"role": "system", "content": "你是苏西，是一个可爱的助手，你很乐意帮助用户回答问题"},  # 系统角色
            {"role": "user", "content": "你是谁"},  # 用户角色
        ],
        stream=False,  # 是否流式返回
        reasoning_effort="high",  # 理解努力程度
        extra_body={"thinking": {"type": "enabled"}}  # 额外的请求体
    )#输出大模型返回的结果
print(response.choices[0].message.content)