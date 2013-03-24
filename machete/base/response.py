
import flask
from flask import current_app, request
import simplejson as _json
from simplejson import dumps
from datetime import datetime


class JSONEncoder(_json.JSONEncoder):
    """
    Modified flask encoder from master, supporting python datetimes and .json
    """

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if hasattr(o, '__html__'):
            return unicode(o.__html__())

        try:
            return o.json
        except:
            pass

        return _json.JSONEncoder.default(self, o)


def success(data=[], meta={}):
    """
    Returns successful API response.

    :param data: The data to be sent back (optional)
    :type data: list or object
    :param meta: The meta information to be sent back (optional)
    :type meta: dict
    :rtype: flask.Response

    """
    response = {"data":data, "meta":meta}
    js = dumps(response, cls=JSONEncoder, indent=None if request.is_xhr else 2 )

    return current_app.response_class(js, mimetype='application/json')


def error(errors=[], meta={}, status_code=400):
    """
    Return an unsuccessful API response.

    :param errors: The errors to be sent back (optional)
    :type errors: list or object
    :param data: any additional data to be passed back to the front end
    :type data: list
    :param meta: The meta information to be sent back (optional)
    :type meta: dict
    :param status_code: The HTTP status code to be sent back (400 by default)
    :type status_code: int
    :rtype: flask.Response

    """
    assert isinstance(errors, list)
    response = flask.jsonify(errors=errors, meta=meta)
    response.status_code = status_code
    return response
