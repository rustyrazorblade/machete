
# this isn't the most elegant file, we're going to try to keep it slim
# it should just be helper functions to reduce LOC globally

import pyes

search = pyes.ES()
search.create_index_if_missing('machete')


def put_mapping(stype, properties):
    search.put_mapping(stype, {"properties": properties}, ['machete'])




