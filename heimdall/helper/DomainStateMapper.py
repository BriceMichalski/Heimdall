from heimdall.framework.model.meta.Singleton import Singleton
from libvirt import VIR_DOMAIN_NOSTATE,VIR_DOMAIN_RUNNING,VIR_DOMAIN_BLOCKED,VIR_DOMAIN_PAUSED,VIR_DOMAIN_SHUTDOWN,VIR_DOMAIN_SHUTOFF,VIR_DOMAIN_CRASHED,VIR_DOMAIN_PMSUSPENDED

class DomaineStateMapper(metaclass=Singleton):

    stateMap = {
        VIR_DOMAIN_NOSTATE : "no state",
        VIR_DOMAIN_RUNNING : "running",
        VIR_DOMAIN_BLOCKED : "blocked",
        VIR_DOMAIN_PAUSED : "paused",
        VIR_DOMAIN_SHUTDOWN : "shutdown",
        VIR_DOMAIN_SHUTOFF : "shutoff",
        VIR_DOMAIN_CRASHED : "crashed",
        VIR_DOMAIN_PMSUSPENDED : "suspended"
    }

    def toString(self,int):
        return self.stateMap.get(int)