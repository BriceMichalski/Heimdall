
import uuid

class ApiResource:
    
    def __init__(self,dict :dict) -> None:

        if dict.get("uuid") == None:
            self.uuid = str(uuid.uuid1())
        else: 
            self.uuid = dict.get('uuid')


    def asDict(self) -> dict:
        dict = self.__dict__.copy()

        whitelistExist = hasattr(self,'_DTO_WHITELIST')
        blacklistExist = hasattr(self,'_DTO_BLACKLIST')

        if blacklistExist:
            for attr in self._DTO_BLACKLIST:
                dict.pop(attr)

        if whitelistExist:
            filteredDict = {}

            for attr in self._DTO_WHITELIST:
                filteredDict[attr] = dict[attr]

            dict = filteredDict
        
        return dict