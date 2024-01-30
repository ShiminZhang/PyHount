# declare requirements
import os
from langchain.agents import agent
import dotenv
from langchain.chains import ConversationChain
from langchain.agents import ZeroShotAgent
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.initialize import initialize_agent
from langchain.agents.types import AgentType
from langchain.prompts import ChatPromptTemplate
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
# define tools
def LoadRequirement():
    # convert requirement to documentation
    return

def DocumentationToCode(In):
    question = f"I want to write a program, its documentation is {In}. Please write the python code for me"
    response = llm.invoke(question)
    answer = response.content
    return answer

# 构建chatgpt的input和问出来
def AskGpt(In):
    question = f"I have a program, its description is {In}. Please give me a code documentation of this program."
    response = llm.invoke(question)
    answer = response.content
    return f"documentation: \n {answer}"

# 这里应该读取一个文件
def LoadDescription(Destription):
    with open('ProjectDescription.txt', 'rt') as file:
        data = file.read()
    return data

def Main():
    # 按此种格式输入即可，需要记忆的最小单位暂定为api
    CustomTools = [
        Tool(
            name = "Design to code documentation",
            description="input description in normal language, return as code documentation",
            func = AskGpt
        ),
        Tool(
            name = "Code documentation to python code",
            description="input code documentation1, return as code",
            func = DocumentationToCode
        ),
        Tool(
            name = "LoadDescription",
            description="return the design desciption as string",
            func = LoadDescription
        )
    ]
    # 这里有很多种chain他们的区别是什么
    EngineerAgent = initialize_agent(
        agent="zero-shot-react-description",llm=llm,tools=CustomTools,verbose=True,handle_parsing_errors=True)
    EngineerAgent.run("load description, get the code documentation and code for me")

if __name__ == "__main__":
    Main()