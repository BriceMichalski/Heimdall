from heimdall.model.NetworkRepresentation import NetworkRepresentation
from heimdall.framework.model.meta.Singleton import Singleton
from heimdall.exception.DefinitionConflictException import DefinitionConflictException
from heimdall.exception.ObjectNotFound import NetworkNotFound

from libvirt import libvirtError, virInterface, open, virNetwork


from heimdall.model.NetworkDefinition import NetworkDefinition

class NetworkService(metaclass=Singleton):

    def __init__(self) -> None:
        self.conn = open("qemu:///system")

    def getNetworkList(self):
        netnameList = self.conn.listNetworks()

        netList = []
        for netname in netnameList:
            network = self.conn.networkLookupByName(netname)
            netList.append(NetworkRepresentation(network))

        return netList

    def createNetwork(self,networkDictArg):

        networkDef = NetworkDefinition(networkDictArg)
        self.checkNetworkConflict(networkDef)
        networkXmlDefinition = networkDef.toXml()
        
        network = self.conn.networkDefineXML(networkXmlDefinition)
        network.setAutostart(True)
        network.create()

        return NetworkRepresentation(network)
 


    def deleteNetwork(self,networkDictArg):
        try:
            name = networkDictArg.get("name")
            uuid = networkDictArg.get("uuid")
            network = self.conn.networkLookupByUUIDString(uuid)

        except libvirtError as e:
            raise NetworkNotFound('Network with uuid {} not found.'.format(uuid))

        if network.name() != name:
            raise DefinitionConflictException('Network name and uuid mismatch')

        network.setAutostart(False)
        if network.isActive():
            network.destroy()
        network.undefine()


    def checkNetworkConflict(self,networkDef :NetworkDefinition):
        existingNetwork = self.getNetworkList()

        if networkDef.bridge in [ net.bridge_name for net in existingNetwork ]:
            raise DefinitionConflictException("Bride {} already in use".format(networkDef.bridge))

        if networkDef.name in [ net.name for net in existingNetwork ]:
            raise DefinitionConflictException("Network {} already exist".format(networkDef.name))



    #       
    #   NETWORK INTERFACE
    #

    def getInterfaceList(self):

        interfaces = self.conn.listAllInterfaces()
        intList = []

        int: virInterface
        for int in interfaces:
            intList.append({
                "name": int.name(),
                "mac_address": int.MACString(),
                "active": bool(int.isActive())
            })

        return intList
