from werkzeug.routing import BaseConverter

class UUIDConverter(BaseConverter):
    """Performs URL parameter validation against a UUID.

    Example:

    @app.route('/<uuid:uid>')

    """
    def __init__(self, url_map, *items):
        super(UUIDConverter, self).__init__(url_map)
        self.regex = r'[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}'

    def to_python(self, value):
        return value.lower()

    def to_url(self, value):
        return value.lower()



