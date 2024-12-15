from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class Updateuser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    prioritt: int

class UpdateTask(BaseModel):
    title: str
    content: str
    prioritt: int