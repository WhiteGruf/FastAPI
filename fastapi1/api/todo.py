from services.auth import AuthService, get_current_user 
from services.todo import ToDoListsService
from fastapi import APIRouter, Depends, Response, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from models.todo import ToDoUpdate, ToDoCreate, ToDo, ToDoClose
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List, Optional
from models.auth import User 

router = APIRouter(
    prefix="/todo"
)


@router.get('/', response_model=List[ToDo])
def get_todo_lists(
    close: Optional[ToDoClose] = None, 
    service: ToDoListsService = Depends()
    ):
    return service.get_list(close = close)


@router.post('/', response_model=ToDo)
def create_todo_list(
    todo_data: ToDoCreate,
    user: User = Depends(get_current_user),
    service: ToDoListsService = Depends()):
    return service.create(todo_data)

@router.get('/{todo_id}', response_model= ToDo)
def get_todo_list(
    id: int,
    request: Request,
    user: User = Depends(get_current_user),
    service: ToDoListsService = Depends()):
    request = service.get(id)
    return request

@router.get('/login/{user_id}', response_model=List[ToDo])
def get_users_todo(
    user_id: int,
    user: User = Depends(get_current_user),
    service: ToDoListsService = Depends(),
):
    return service.user_todo_get(user_id)

@router.put('/{id}', response_model=ToDo)
def update_todo(
    id: int,
    todo_data: ToDoUpdate,
    user: User = Depends(get_current_user),
    service: ToDoListsService = Depends(),
):
    return service.update(id, todo_data)


@router.delete('/{id}')
def delete_todo(
    id: int,
    user: User = Depends(get_current_user),
    service: ToDoListsService = Depends(),
):
    service.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)