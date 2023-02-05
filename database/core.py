from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    Session)


class SQLAlchemy:
    def __init__(self):
        self.engine = self.create_engine()
        self.Base = declarative_base()
        self.session = self.create_session()

    def create_engine(self):
        engine = create_engine("sqlite:///database/dungeon_dragon.db")
        return engine

    def create_session(self):
        return Session(self.engine)
