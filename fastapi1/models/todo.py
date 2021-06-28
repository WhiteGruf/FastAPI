from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import Optional
from enum import Enum
from typing import List


class ToDoClose(str, Enum):
    DONE = "DONE"
    NOT_DONE = "NOT DONE"

class TodoModel(BaseModel):
    user_id: Optional[int]
    task: str
    date: date
    close: ToDoClose


class ToDo(TodoModel):
    id: int

    class Config:
        orm_mode = True

class ToDoCreate(TodoModel):
    pass
class ToDoUpdate(TodoModel):
    pass