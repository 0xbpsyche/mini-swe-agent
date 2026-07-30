import re
import subprocess
import os

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

def parse_arction(lm_output: str) -> str:
    """从模型回复中提取bash-action代码块里的命令"""
    matches = re.findall(
        r"```bash-action\s*\n(.*?)\n```"
        lm_output,
        re.DOTALL
    )

    if matches:
        return matches[0].strip()
    else:
        return ""

def execute_action(command: str) -> str:
    """执行动作并返回输出"""
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        env=os.environ,
        encoding="utf-8",
        errors="replace"
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30
    )
    return result.stdout

