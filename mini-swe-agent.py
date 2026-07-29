from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://cpa.0xpsyche.me/v1",
    #此处不声明api_key，因为OpenAI SDK会自动读取环境中env中的key
    #codex: load_dotenv() 已加载 .env；省略 api_key 时，SDK 会读取 OPENAI_API_KEY
)

def query_lm(messages):
    response = client.responses.create(
        model='gpt-5.6-sol',
        input=messages
    )
    return response.output_text

messages = input()
print(query_lm(messages))