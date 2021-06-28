from fastapi import APIRouter
#from .users import router as users_router
from .auth import router as auth_router
from .houses import router as houses_router
from .todo import router as todo_router

router = APIRouter()
router.include_router(auth_router)
#router.include_router(users_router)
router.include_router(houses_router)
router.include_router(todo_router)