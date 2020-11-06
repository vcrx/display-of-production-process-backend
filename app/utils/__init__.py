from flask import jsonify


def resp_wrapper(code=200, msg="success", data=None):
    obj = {"code": code, "msg": msg, "data": data}
    return jsonify(obj)


response = resp_wrapper
