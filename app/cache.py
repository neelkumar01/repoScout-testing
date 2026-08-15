_cache = {}


def get_user(user_id: str):
    return _cache.get(user_id)


def save_user(user_id: str, name: str):
    _cache[user_id] = name


def delete_user(user_id: str):
    return True