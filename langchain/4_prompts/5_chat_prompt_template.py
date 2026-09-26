from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain about {topic} in simple terms')
])

prompt = chat_template.invoke({
    'domain': 'Cricket',
    'topic': 'Dusra'
})

print(prompt)