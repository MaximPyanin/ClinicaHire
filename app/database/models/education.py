from app.database.base import Base
from app.database.models.user import User
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from app.constants.degree import Degrees
from app.database.base import Base
from app.constants.types import Types

class Education(Base):
    __tablename__ = "educations"
    id: Mapped[Types.UUID_PK]
    institution: Mapped[str | None]
    degree: Mapped[Degrees | None]
    start_year: Mapped[date | None]
    end_year: Mapped[date | None]
    specialization: Mapped[str | None]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    user: Mapped["User"] = relationship(back_populates="educations",uselist=False)
