import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class CommandModel(Base):
    __tablename__ = "command"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    input_text: Mapped[str]
    output_text: Mapped[str]
