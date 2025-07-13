import os
import openai  # 导入OpenAI SDK
from openai import OpenAI

# 从环境变量读取API密钥（已配置为DASHSCOPE_API_KEY）
api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("请先设置DASHSCOPE_API_KEY环境变量")

# 配置OpenAI客户端，指向千问API的兼容端点
client = OpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 千问兼容OpenAI格式的API地址
)

def qwen_chat(prompt, model="qwen-turbo", temperature=0.7):
    """
    调用千问大模型的聊天接口
    参数:
        prompt: str - 用户的问题或提示词
        model: str - 模型名称（qwen-turbo/qwen-plus/qwen-max等）
        temperature: float - 生成随机性（0-1，值越大越随机）
    返回:
        str - 模型生成的回复
    """
    try:
        # 发送聊天请求
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=1000  # 最大生成字符数
        )
        # 提取回复内容
        return response.choices[0].message.content
    except Exception as e:
        return f"API调用失败: {str(e)}"

# 测试代码（直接运行文件时执行）
if __name__ == "__main__":
    print("===== 千问API测试 =====")
    user_input = input("请输入你的问题: ")
    result = qwen_chat(user_input)
    print("\n===== 模型回复 =====")
    print(result)
