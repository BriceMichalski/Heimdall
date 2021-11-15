from heimdall.framework.model.ApiResource import ApiResource

class BaseImage(ApiResource):
    _DTO_BLACKLIST = ["path","url","filename"]

    def __init__(self,dict) -> None:
        super().__init__(dict)
        self.url = dict.get('url')
        self.name = dict.get('name')
        self.family = dict.get('family')
        self.variant = dict.get('variant')
        self.md5sum = dict.get('md5sum')

        self.path = dict.get('path')
        self.filename = dict.get('url').split('/')[-1]

        