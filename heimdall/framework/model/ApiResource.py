
class ApiResource:

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