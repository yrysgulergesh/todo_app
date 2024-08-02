from pydantic import BaseModel

# Token Schema for JWT tokens
class Token(BaseModel):
    access_token: str
    token_type: str

# Token Data Schema
class TokenData(BaseModel):
    username: str | None = None

# User Schema
class User(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True

# User Create Schema for Registration
class UserCreate(BaseModel):
    username: str
    password: str

# Task Schema
class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

