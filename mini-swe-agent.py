from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI(
    base_url="https://api.flyapi.tech/v1",
    #此处不声明api_key，因为OpenAI SDK会自动读取环境中env中的key
    #codex: load_dotenv() 已加载 .env；省略 api_key 时，SDK 会读取 OPENAI_API_KEY
)

def query_lm(messages):
    response = client.responses.create(
        model='gpt-5.6-sol',
        input=messages
    )
    return response.output_text

messages = [{"role": "user", "content": "掷一个 d20 骰子"}]
print(query_lm(messages))