from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User
from users.schemas import CreateUser


async def create_user(session: AsyncSession, user_in: CreateUser) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user