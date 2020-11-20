from persitstence.db import session
from ..models.thing import Thing

def get_all_names():
    return session.query(Thing).all()