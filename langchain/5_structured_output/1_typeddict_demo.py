from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': "Harsh", 'age': 21}

print(new_person)