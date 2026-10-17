from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

schema = [
    ResponseSchema(name = 'Fact 1', description="fact 1 about the topic"),
    ResponseSchema(name = 'Fact 2', description="fact 2 about the topic"),
    ResponseSchema(name = 'Fact 3', description="fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'topic': 'blackhole'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)