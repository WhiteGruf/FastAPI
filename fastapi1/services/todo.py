from sqlalchemy.sql.expression import table
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db_fp import get_session
import tables
from typing import List, Optional
from models.todo import ToDo, ToDoCreate, ToDoUpdate


class ToDoListsService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self,close: Optional[ToDo] = None) -> List[tables.ToDoList]:
        query = self.session.query(tables.ToDoList)
        if query:
            query = query.filter_by(close = close)
        todolist = query.all()
        return todolist

    def _get(self, id: int, filter_id: str) -> List[tables.ToDoList]:
        if filter_id=="todo_id":
            todolist = (
                self.session
                .query(tables.ToDoList)
                .filter_by(id = id)
                .first()
            )
        if filter_id=="user_id":
            todolist = (
                self.session
                .query(tables.ToDoList)
                .filter_by(user_id = id)
                .all()
            )
        if not todolist:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        return todolist
            
    def get(self, id: int) -> tables.ToDoList:
        return self._get(id, "todo_id")

    def user_todo_get(self, id: int) -> tables.ToDoList:
        return self._get(id, "user_id")


    def create(self, todo_data: ToDoCreate) -> tables.ToDoList:
        todolist = tables.ToDoList(**todo_data.dict())
        self.session.add(todolist)
        self.session.commit()
        return todolist

    def update(self, id: int,todo_data: ToDoUpdate) -> tables.ToDoList:
        todolist = self.get(id)
        for field, value in todo_data:
            setattr(todolist, field, value)
        self.session.commit()
        return todolist
    
    def delete(self, id:int):
        todolist = self._get(id, "todo_id")
        self.session.delete(todolist)
        self.session.commit()
