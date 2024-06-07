from sqlalchemy.orm import Mapped

from .base import Base


class User(Base):
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    active: Mapped[bool]
