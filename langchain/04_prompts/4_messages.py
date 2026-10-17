from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

message = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about yourself")
]

result = model.invoke(message)
message.append(AIMessage(content=result.content))

print(message)