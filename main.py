import os
from fc import Tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage


load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Debug statement')
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
    tools = [Tool.add, Tool.multiply]
    llm_with_tools = llm.bind_tools(tools)
    query = "What is 3 * 12? Also, what is 11 + 49?"

    messages = [HumanMessage(query)]
    response = llm_with_tools.invoke(query).tool_calls

    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    for tool_call in ai_msg.tool_calls:
        selected_tool = {"add": Tool.add, "multiply": Tool.multiply}[tool_call["name"].lower()]
        tool_output = selected_tool.invoke(tool_call["args"])
        messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))


