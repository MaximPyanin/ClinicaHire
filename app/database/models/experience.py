from app.database.base import Base
from app.database.models.user import User
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from app.database.base import Base
from app.constants.types import Types

class Experience(Base):
    __tablename__ = "experiences"
    id: Mapped[Types.UUID_PK]
    position: Mapped[str]
    location: Mapped[str | None]
    start_year: Mapped[date | None]
    end_year: Mapped[date | None]
    description: Mapped[str | None]
    company: Mapped[str | None]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates="experiences",uselist=False)