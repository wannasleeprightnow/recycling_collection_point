import uuid

from sqlalchemy import Boolean, UUID
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(), primary_key=True, default=uuid.uuid4()
    )
    telegram_username: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
