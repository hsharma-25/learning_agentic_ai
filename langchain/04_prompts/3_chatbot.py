from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_hist = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input("You: ")
    chat_hist.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_hist)
    chat_hist.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_hist)