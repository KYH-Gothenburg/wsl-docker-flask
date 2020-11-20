import persitstence.repository.names_repo as nr


def get_all_names():
    return [name.to_dict() for name in nr.get_all_names()]