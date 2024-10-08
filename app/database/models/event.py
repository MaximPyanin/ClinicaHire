from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

from app.constants.user_languages import EventTags
from app.database.base import Base
from app.constants.types import Types

from app.database.models.feedback import Feedback

from app.database.models.language import Tag
from app.database.models.user import User
from app.database.models.registration import Registration


class Event(Base):
    __tablename__ = "events"
    id: Mapped[Types.UUID_PK]
    location: Mapped[str]
    date: Mapped[date]
    created_at: Mapped[Types.CREATED_AT]
    description: Mapped[str]
    tag_id: Mapped[EventTags] = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"))
    organizer_id: Mapped[Types.UUID_PK] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )

    tag: Mapped["Tag"] = relationship(back_populates="events", uselist=False)
    organizer: Mapped["User"] = relationship(
        back_populates="organized_events", uselist=False
    )

    feedbacks: Mapped[list["Feedback"]] = relationship(
        back_populates="event", uselist=True
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="events", uselist=True, secondary=Registration.__table__
    )
