from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __table_args__ = {'extend_existing': True}
    def __repr__(self):
        return str({c.name: getattr(self, c.name) for c in self.__table__.columns})