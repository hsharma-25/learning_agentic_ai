from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1, max_completion_tokens=10)
##temperature is the parameter for adjusting the creativity(randomness) of the results, varies from 0 to 2
##max_completion_tokens

result = model.invoke("What is the capital of India?")

print(result)
print(result.content)       ##print only content not the other json info