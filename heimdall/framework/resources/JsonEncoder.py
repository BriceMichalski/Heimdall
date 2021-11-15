from heimdall.framework.model.ApiResource import ApiResource

from json import JSONEncoder

class JsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ApiResource):
            return obj.asDict()
      
        return JSONEncoder.default(self, obj)