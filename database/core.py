from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"{self.ssn} {self.firstname}"


engine = create_engine("sqlite:///database//mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(12321, "mike", "smith", "m", 35)
session.add(person)
session.commit()

p1 = person = Person(154, "mike", "smith", "m", 35)
p2 = person = Person(5651, "bobe", "jackson", "m", 35)
p3 = person = Person(84098, "Ann", "smith", "m", 35)
p4 = person = Person(8048, "Angela", "Blue", "m", 35)

session.add(p1)
session.add(p2)
session.add(p3)
session.add(p4)
session.commit()
