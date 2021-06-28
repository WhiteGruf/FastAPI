from sqlalchemy.sql.expression import table
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from db_fp import get_session, get_conn
import tables
from typing import List, Optional
from models.houselists import  HouseSold, HouseCreate, HouseUpdate


class HouseListsService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session



    def get_list(self,sold: Optional[HouseSold] = None) -> List[tables.HouseList]:
        query = self.session.query(tables.HouseList)
        if query:
            query = query.filter_by(sold = sold)
        hlists = query.all()
        return hlists

    def _get(self, id: int, filter_id: str) -> tables.HouseList:
        if filter_id=="house_id":
            house = (
                self.session
                .query(tables.HouseList)
                .filter_by(house_id = id)
                .first()
            )
        if filter_id=="user_id":
            house = (
                self.session
                .query(tables.HouseList)
                .filter_by(user_id = id)
                .first()
            )
        if not house:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
        return house
            
        
    

    def get(self, id: int) -> tables.HouseList:
        return self._get(id, "house_id")

    def user_house_get(self, id: int) -> tables.HouseList:
        return self._get(id, "user_id")


    def create(self, house_data: HouseCreate) -> tables.HouseList:
        houselist = tables.HouseList(**house_data.dict())
        self.session.add(houselist)
        self.session.commit()
        return houselist

    def update(self, id: int,house_data: HouseUpdate) -> tables.HouseList:
        house = self.get(id)
        for field, value in house_data:
            setattr(house, field, value)
        self.session.commit()
        return house
    
    def delete(self, id:int):
        house = self._get(id, "house_id")
        self.session.delete(house)
        self.session.commit()
