from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.constants.types import Types
from app.database.base import Base
from app.constants.user_languages import UsersLevels,UsersLanguages
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.database.models.event import Event


class Language(Base):
    __tablename__ = "languages"
    id: Mapped[Types.UUID_PK]
    name: Mapped[UsersLanguages]
    level: Mapped[UsersLevels]
