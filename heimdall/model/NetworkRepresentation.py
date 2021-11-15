from libvirt import virNetwork
from heimdall.framework.model.ApiResource import ApiResource

class NetworkRepresentation(ApiResource):

    def __init__(self,network :virNetwork) -> None:
        self.name= network.name()
        self.uuid= network.UUIDString()
        self.autostart= bool(network.autostart())
        self.active= bool(network.isActive())
        self.persistent= bool(network.isPersistent())
        self.bridge_name= network.bridgeName()
        self.dhcp= network.DHCPLeases()
