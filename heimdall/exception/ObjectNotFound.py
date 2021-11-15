
class ObjectNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class DomainNotFound(ObjectNotFound):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NetworkNotFound(ObjectNotFound):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BaseImageNotFound(ObjectNotFound):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)