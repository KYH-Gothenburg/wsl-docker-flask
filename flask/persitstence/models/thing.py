from persitstence.db import Base
import sqlalchemy as sa

class Thing(Base):
    __tablename__ = 'some_names'

    id = sa.Column(sa.Integer, primary_key=True)
    a_name = sa.Column(sa.String(100), nullable=False)


    def __repr__(self):
        return self.a_name

    def to_dict(self):
        return {'name': self.a_name}

