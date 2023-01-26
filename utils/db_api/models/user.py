from sqlalchemy import Column, BigInteger, sql, String, Boolean

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    status = Column(Boolean, default=False)

    query: sql.select
