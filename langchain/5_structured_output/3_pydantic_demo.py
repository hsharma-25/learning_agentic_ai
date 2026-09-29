from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal number representing the CGPA of the student")

new_student = {'name': 'Harsh',
               'age': 21,
               'email': 'harsh@abc.com',
               'cgpa': 5}

student = Student(**new_student)
print(student)