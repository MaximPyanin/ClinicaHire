from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.database.base import Base
from app.constants.types import Types
from app.constants.user_roles import UserRoles
from app.database.models.education import Education
from app.database.models.experience import Experience

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
    expected_country: Mapped[str | None]
    expected_city: Mapped[str | None]
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
    educations: Mapped[list['Education']] = relationship(back_populates='user',uselist=True)
    experiences: Mapped[list["Experience"]] = relationship(back_populates="user", uselist=True)



