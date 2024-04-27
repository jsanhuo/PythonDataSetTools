import openai
from openai import OpenAI
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-JmroZD3byV792L6MgVi1xkhSmQEShoCBMXPYoyhhu22iJuR7",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.cn/v1"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # 指定模型
    messages=[
    {"role": "user", "content": "How many English words can you translate into Chinese at most?"}
  ]
)
print(response.choices[0].message.content)
