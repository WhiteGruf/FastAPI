from fastapi import FastAPI, Query, Path, Body
from typing import List
#import api.router
from api import router

app = FastAPI()
app.include_router(router)

