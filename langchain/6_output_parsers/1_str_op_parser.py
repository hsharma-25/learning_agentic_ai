from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

model = ChatOpenAI()

##prompt for detailed output
template_1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

##prompt for summary-like output
template_2 = PromptTemplate(
    template="Write the summary of the following text. /n {text}",
    input_variables=['text']
)

# prompt_1 = template_1.invoke({
#     'topic': 'blackhole'
# })
# result_1 = model.invoke(prompt_1)

# prompt_2 = template_2.invoke({
#     'text': result_1.content
# })
# result_2 = model.invoke(prompt_2)
# print(result_2.content)

parser = StrOutputParser()

## parser helps to extract string output from model's prompt1 output and feed it to the next prompt
chain = template_1 | model | parser | template_2 | model | parser

result = chain.invoke({'topic': 'blackhole'})
print(result)