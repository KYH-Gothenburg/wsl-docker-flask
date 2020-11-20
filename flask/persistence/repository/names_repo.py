from persistence.db import session
from ..models.thing import Thing

def get_all_names():
    return session.query(Thing).all()



def add_names(names):
    session.add_all(names)
    session.commit()