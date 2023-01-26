from asyncpg import UniqueViolationError

from utils.db_api.models.user import User


async def add_user(user_id: int):
    try:
        user = User(user_id=user_id, status=False)
        await user.create()
    except UniqueViolationError:
        print('User creation error')


async def get_user_status(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user.status


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_all_active_users(user_id):
    users = await User.query.where(User.status == True).where(User.user_id != user_id).gino.all()
    return users


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_user_status(user_id, status: bool):
    user = await select_user(user_id)
    await user.update(status=status).apply()


async def delete_user(user_id):
    user = await select_user(user_id)
    await user.delete()
