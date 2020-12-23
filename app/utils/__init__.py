from flask import jsonify


def resp_wrapper(code=200, msg="success", data=None, inherit_code=True):
    obj = {"code": code, "msg": msg, "data": data}
    if inherit_code:
        return jsonify(obj), code
    else:
        return jsonify(obj)


response = resp_wrapper


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def safe_float(value, default=None):
    return safe_cast(value, float, default)


def safe_int(value, default=None):
    return safe_cast(value, int, default)


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def safe_round(value, digits=2):
    try:
        value = float(value)
        return round(value, digits)
    except Exception:
        return value


def normalize_query_param(value):
    """
    Given a non-flattened query parameter value,
    and if the value is a list only containing 1 item,
    then the value is flattened.

    :param value: a value from a query parameter
    :return: a normalized query parameter value
    """
    value: str = value if len(value) > 1 else value[0]
    return value


def get_query(params):
    """
    Converts query parameters from only containing one value for each parameter,
    to include parameters with multiple values as lists.

    :param params: a flask query parameters data structure
    :return: a dict of normalized query parameters
    """
    params_non_flat = params.to_dict(flat=False)
    return {k: normalize_query_param(v) for k, v in params_non_flat.items()}
