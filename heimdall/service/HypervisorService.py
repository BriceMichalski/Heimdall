from heimdall.framework.model.meta.Singleton import Singleton
import libvirt

class HypervisorService(metaclass=Singleton):

    def __init__(self) -> None:
        self.conn = libvirt.open("qemu:///system")
    
    def hyperviseurInfo(self):

        nodeinfo = self.conn.getInfo()

        infos = {
            self.conn.getHostname(): {
                "type": self.conn.getType(),
                "maxVcpu": self.conn.getMaxVcpus(None),
                "model": nodeinfo[0],
                "memory_size": str(nodeinfo[1])+'MB',
                "cpu_count": nodeinfo[2],
                "cpu_socket_count": nodeinfo[5],
                "cpu_cores_per_socket": nodeinfo[6],
                "cpu_thread_per_cores": nodeinfo[7]
            }
        }

        return infos 
