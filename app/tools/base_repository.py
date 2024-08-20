from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.orm import selectinload
from fastapi import Depends
from app.tools.database import get_db
from app.tools.constants import DatabaseQueryOrder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, asc, desc, inspect
from typing import Optional, Any


class BaseRepository:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.db = db

    async def create(self, model_instance, ongoing_transaction=False):
        self.db.add(model_instance)
        if not ongoing_transaction:
            await self.db.commit()
            await self.db.refresh(model_instance)
        return model_instance

    async def delete(self, model_instance, ongoing_transaction=False):
        await self.db.delete(model_instance)
        if not ongoing_transaction:
            await self.db.commit()

    async def get_all(
        self,
        model,
        filter: Optional[dict[InstrumentedAttribute, Any]] = None,
        relationships: Optional[list[InstrumentedAttribute]] = None,
        order_by: Optional[InstrumentedAttribute] = None,
        order: DatabaseQueryOrder = DatabaseQueryOrder.DESC,
        limit: int = 100,
        offset: int = 0,
    ):
        if order_by is None:
            order_by = inspect(model).primary_key[0]
        if filter is None:
            filter = {}
        if relationships is None:
            relationships = []
        order_by = desc(order_by) if order == DatabaseQueryOrder.DESC else asc(order_by)
        stmt = (
            select(model)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .where(*[attribute == value for attribute, value in filter.items()])
            .options(
                *[selectinload(relationship) for relationship in relationships]
            )  # no chaining
        )
        models = await self.db.execute(stmt)
        return models.scalars().all()

    async def get_one(
        self,
        model,
        filter: Optional[dict[InstrumentedAttribute, Any]] = None,
        relationships: Optional[list[InstrumentedAttribute]] = None,
    ):
        if filter is None:
            filter = {}
        if relationships is None:
            relationships = []
        stmt = (
            select(model)
            .where(*[attribute == value for attribute, value in filter.items()])
            .options(*[selectinload(relationship) for relationship in relationships])
        )  # no chaining
        model = await self.db.execute(stmt)
        return model.scalars().first()
