from uuid import UUID

from sqlalchemy import insert, update, delete, select

from app.database.db import DB
from app.database.models.feedback import Feedback


class FeedbacksRepository:
    def __init__(self, db: DB):
        self.db = db
        self.model = Feedback

    async def insert_one(self, data: dict) -> UUID:
        async with self.db.get_sessionmaker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            return res.scalar_one()

    async def update_one(self, new_data: dict, id: UUID) -> Feedback:
        async with self.db.get_sessionmaker() as session:
            stmt = (
                update(self.model)
                .values(**new_data)
                .where(self.model.id == id)
                .returning(self.model)
            )
            res = await session.execute(stmt)
            return res.scalar_one()

    async def delete_one(self, id: UUID) -> Feedback:
        async with self.db.get_sessionmaker() as session:
            stmt = delete(self.model).where(self.model.id == id).returning(self.model)
            res = await session.execute(stmt)
            return res.scalar_one()

    async def get_one(self, id: UUID) -> Feedback:
        async with self.db.get_sessionmaker() as session:
            stmt = select(self.model).where(self.model.id == id)
            res = await session.execute(stmt)
            return res.scalar_one()
