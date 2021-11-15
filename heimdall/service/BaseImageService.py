from heimdall.exception.DefinitionConflictException import DefinitionConflictException
from heimdall.exception.AlreadyExistException import AlreadyExistException
from heimdall.exception.ChecksumException import ChecksumException
from heimdall.framework.model.Endpoint import *
from heimdall.framework.resources.Configuraton import Configuration
from heimdall.framework.model.TermColors import TermColors
from heimdall.repository.BaseImageRepository import BaseImageRespositry
from heimdall.model.BaseImage import BaseImage

import os
import requests 
import hashlib

class BaseImageService(Endpoint):

    def __init__(self) -> None:
        config = Configuration()
        self.workingDir = config.workingDir
        self.baseImageDir = config.workingDir + "/base_images"

        self.repository = BaseImageRespositry()

        if not os.path.isdir(self.baseImageDir):
            os.mkdir(self.baseImageDir)

    def newBaseImage(self,args):
        image = BaseImage(args)

        download_dest = os.path.join(self.baseImageDir,image.filename)

        if os.path.exists(download_dest):
            raise AlreadyExistException("A base image with name '{}' already exist".format(image.filename))

        # download image file
        with requests.get(image.url, stream=True) as r:
            r.raise_for_status()
            with open(download_dest,'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)

        md5 = hashlib.md5()
        block_size = 128 * md5.block_size
        imageFile = open(download_dest,'rb')
        chunk = imageFile.read(block_size)
        while chunk:
            md5.update(chunk)
            chunk = imageFile.read(block_size)

        md5sum = md5.hexdigest()    

        if md5sum != image.md5sum:
            error = "The announced checksum does not match the one of the downloaded file"
            print(f"{TermColors.FAIL} * "+ error + ": File will be deleted " + TermColors.ENDC) #TODO use logger
            os.remove(download_dest)
            raise ChecksumException(error)

        image.path = download_dest
        self.repository.insert(image)

        return image
    
    def delete(self,uuid,name=None):

        image = self.repository.findByUUID(uuid)

        if name != None and image.name != name:
            raise DefinitionConflictException('Base image name and uuid mismatch')

        os.remove(image.path)

        if not os.path.exists(image.path):
            self.repository.delete(uuid)



    def getImageList(self):
        return self.repository.findAll()