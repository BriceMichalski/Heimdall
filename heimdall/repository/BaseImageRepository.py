from heimdall.exception.ObjectNotFound import BaseImageNotFound
from heimdall.framework.resources.Database import DatabaseConnection
from heimdall.framework.resources.TinyReposiory import TinyRepository,Query
from heimdall.model.BaseImage import BaseImage

class BaseImageRespositry(TinyRepository):

    def __init__(self) -> None:
        self.clazz = BaseImage
        self.table = DatabaseConnection().getTable(self.clazz)

    def insert(self,baseImage):
        self.assertType(baseImage)
        self.table.insert(self.jsonify(baseImage))

    def findAll(self):
        images = self.table.all()
        return [BaseImage(image) for image in images]

    def findByUUID(self,uuid):
        imageDict = self.table.get(Query().uuid == uuid)
        if imageDict == None:
            raise BaseImageNotFound('base image with uuid {} not found'.format(uuid))

        return BaseImage(imageDict)
    
    def delete(self,uuid):
        self.table.remove(Query().uuid == uuid)