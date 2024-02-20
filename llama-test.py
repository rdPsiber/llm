from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI, ChatMessage
from llama_index.tools import BaseTool, FunctionTool


def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a +  b


multiply_tool = FunctionTool.from_defaults(fn=multiply)

def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a * b


add_tool = FunctionTool.from_defaults(fn=add)

llm = OpenAI(model="gpt-3.5-turbo-instruct")
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)
                               

response = agent.chat("What is 20+(2*4)? Calculate step by step ")




