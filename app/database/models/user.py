from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.base import Base
from app.constants.types import Types
from app.constants.user_roles import UserRoles
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.database.models.event import Event
    from app.database.models.feedback import Feedback
from app.database.models.registration import Registration
from app.database.models.role import Role


class User(Base):
    __tablename__ = "users"
    id: Mapped[Types.UUID_PK]
    name: Mapped[str]
    surname: Mapped[str]
    phone: Mapped[str]
    summary: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str]
    expected_salary: Mapped[float | None]
    password: Mapped[str]
    linkedin: Mapped[str | None]
    city: Mapped[str]
    country: Mapped[str]
    avatar: Mapped[str | None]
    hobby: Mapped[str | None]
    portfolio: Mapped[str | None]
    deleted_at: Mapped[bool]
    share_profile: Mapped[bool]
    refresh_token: Mapped[UUID | None]
    expired_at: Mapped[datetime | None]
    role_id: Mapped[UserRoles] = mapped_column(
        ForeignKey("roles.id", ondelete="CASCADE")
    )

    role: Mapped["Role"] = relationship(back_populates="users", uselist=False)



