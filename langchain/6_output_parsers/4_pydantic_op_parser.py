from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(temperature=1.9)

class Person(BaseModel):

    name: str = Field(description='name of the person')
    age: int = Field(gt=18, description='age of the person')
    city: str = Field(description='city that the person belongs to')
    fav_food_item: str = Field(description="favorite food item of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='give me the name, city, age and favorite food item name of a fictional person from {place} \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions}
)

# prompt = template.invoke({})
# result = model.invoke(prompt)

chain = template | model | parser
result = chain.invoke({'India'})
print(result)

# final_result = parser.parse(result.content)
# print(final_result)