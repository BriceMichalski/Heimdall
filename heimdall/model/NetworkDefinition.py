from lxml.builder import E
from lxml import etree

class NetworkDefinition:

    def __init__(self,dict :dict) -> None:
        self.name = dict.get('name')
        self.bridge = dict.get('bridge')
        self.forwardMode = dict.get('forwardMode')
        self.ipAdress = dict.get('ipAdress')
        self.netmask = dict.get('netmask')
        self.dhcpStart = dict.get('dhcpStart')
        self.dhcpEnd = dict.get('dhcpEnd')


    def toXml(self):
        definition = (
            E.network(
                E.name(self.name),
                E.bridge(name=self.bridge),
                E.forward(mode=self.forwardMode),
                E.ip( 
                    E.dhcp(
                        E.range(start=self.dhcpStart,end=self.dhcpEnd )
                    ),
                    address=self.ipAdress, netmask=self.netmask
                )
            )
        )

        return etree.tostring(definition,encoding = "utf-8").decode("utf-8")