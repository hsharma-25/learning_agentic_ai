from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3-0324:fastest",    ##specify the repo of the model that you eant to use
    task = "text-generation"                        ##what task do you want the model to do
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("Who is the founder of Anthropic?")
print(result.content)