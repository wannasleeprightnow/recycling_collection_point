import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class EventModel(Base):
    __tablename__ = "event"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    title: Mapped[str]
    event_description: Mapped[str]
