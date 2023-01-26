from sqlalchemy import Column, BigInteger, sql, String, Boolean

from utils.db_api.db_gino import TimedBaseModel


class Message(TimedBaseModel):
    __tablename__ = 'messages'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    original_id = Column(BigInteger)
    message_id = Column(BigInteger)

    query: sql.select