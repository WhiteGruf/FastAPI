from services.auth import AuthService, get_current_user
from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from models.auth import UserCreate, Token, User 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")



router = APIRouter(
    prefix='/auth',
)


@router.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):

    return templates.TemplateResponse("index.html", {"request": request, "id": id})


@router.post('/sign-up', response_model=Token)
def sig_up(
    user_data: UserCreate, 
    request: Request,
    service: AuthService = Depends(),
    ):
    request = service.register_new_user(user_data)
    return request#templates.TemplateResponse('index.html', context=(request))
        

@router.post('/sign-in',  response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(),
    ):
    print("here")
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )

@router.get('/user', response_model= User)
def get_user(user: User = Depends(get_current_user)):
    return user