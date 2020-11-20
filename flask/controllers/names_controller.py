import persistence.repository.names_repo as nr
from persistence.models.thing import Thing

def get_all_names():
    return [name.to_dict() for name in nr.get_all_names()]


def add_names(names):
    names = [Thing(a_name=name['name']) for name in names]
    nr.add_names(names)