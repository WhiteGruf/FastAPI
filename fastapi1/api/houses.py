from fastapi import APIRouter, Depends, Response, status, Request
from fastapi.templating import Jinja2Templates
from models.houselists import HouseList, HouseSold, HouseCreate, HouseUpdate
from models.auth import User 
from services.houses import HouseListsService
from services.auth import get_current_user
from typing import List, Optional
from db_fp import get_conn

router = APIRouter(
    prefix='/house',
)
templates = Jinja2Templates(directory="templates/")


@router.get('/', response_model=List[HouseList])
def get_hlists(
    sold: Optional[HouseSold] = None, 
    service: HouseListsService = Depends()
    ):
    return service.get_list(sold = sold)


@router.post('/', response_model=HouseList)
def create_house(
    house_data: HouseCreate,
    user: User = Depends(get_current_user),
    service: HouseListsService = Depends()
):
    return service.create(house_data)

@router.get('/{house_id}', response_model= HouseList)
def get_house(
    house_id: int,
    request: Request,
    user: User = Depends(get_current_user),
    service: HouseListsService = Depends(),
):
    request = service.get(house_id)
    return request#templates.TemplateResponse('index.html', context={'request':request})

@router.get('/login/{user_id}', response_model= HouseList)
def get_users_house(
    user_id: int,
    user: User = Depends(get_current_user),
    service: HouseListsService = Depends(),
):
    return service.user_house_get(user_id)

@router.put('/{id}', response_model=HouseList)
def update_house(
    house_id: int,
    house_data: HouseUpdate,
    user: User = Depends(get_current_user),
    service: HouseListsService = Depends(),
):
    return service.update(house_id, house_data)


@router.delete('/{id}')
def delete_house(
    house_id: int,
    user: User = Depends(get_current_user),
    service: HouseListsService = Depends(),
):
    service.delete(house_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)