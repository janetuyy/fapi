from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User
from users.schemas import CreateUser
from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_user(session: AsyncSession, user_in: CreateUser) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user

async def get_users_dict(session: AsyncSession) -> dict[str, User]:
    stmt = select(User).order_by(User.username)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    users_dict = {user.username: user for user in users}
    return users_dict