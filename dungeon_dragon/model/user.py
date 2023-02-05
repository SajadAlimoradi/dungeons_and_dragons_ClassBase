from sqlalchemy import sql
from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
    Column,
    Integer,
    String
)

from database import db


class UserModel(db.Base):
    __tablename__ = "account_users"

    def __init__(self, username, password, avatar):
        self.username = username
        self.password = password
        self.avatar = avatar

    id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String(255),
        nullable=False,
        unique=True
    )

    password = Column(
        String(255),
        nullable=False,
    )

    avatar = Column(
        String(255),
        nullable=False,
    )

    @classmethod
    def create(cls, username, password, avatar):
        try:
            user = cls(
                username=username,
                password=password,
                avatar=avatar
            )
            db.session.add(user)
            db.session.commit()
            # todo: add debug log
        except IntegrityError as e:
            #todo: add exception log
            raise UserAlreadyExist("username already exist. ", params=e.params, orig=e.params)
        return user

    @classmethod
    def update(cls, old_username, new_username):
        stmt = sql.update(cls) \
            .where(cls.username == old_username) \
            .values(username=new_username)
        # breakpoint()
        db.session.execute(stmt)
        db.session.commit()
        # todo: log debug existing record update in account_user
        print("Existing record {old_username} to {new_username} updated in 'account_user'. ")

    @classmethod
    def read(cls, username):
        stmt = sql.select(cls).where(cls.username == username)
        user = db.session.execute(stmt)
        return user

    @classmethod
    def adapt(cls, username):
        stmt = sql.select(cls.username, cls.password, cls.avatar).where(cls.username == username)
        user = db.session.execute(stmt)
        return user

    @classmethod
    def delete(cls, username):
        stmt = sql.delete(cls).where(cls.username == username)
        db.session.execute(stmt)
        db.session.commit()

    def __repr__(self):
        return (self.username, self.password, self.avatar)
