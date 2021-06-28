import uvicorn

from settings import settings_w
'''
                                            !!!!создание таблиц бд!!!!'''
from tables import Base
from db_fp import engine

Base.metadata.create_all(engine) 


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host = settings_w.server_host,
        port = settings_w.server_port,
        reload = True,
        )