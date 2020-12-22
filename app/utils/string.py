def remove_prefix(str_: str, prefix):
    if str_.startswith(prefix):
        return str_[len(prefix) :]
    else:
        return str_


def remove_suffix(str_: str, suffix):
    if str_.endswith(suffix):
        return str_[: -len(suffix)]
    else:
        return str_
