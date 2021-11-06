
class Role:
    UNAUTHENTICATED = "UNAUTHENTICATED"
    AUTHENTICATED = "AUTHENTICATED"
    USER = "USER"
    ADMIN = "ADMIN"

    _hierachie = {
        ADMIN: 8,
        USER: 4,
        AUTHENTICATED: 2,
        UNAUTHENTICATED: 1
    }

    # 3
    def listRoles(self,currentRole):
        roles = []

        if currentRole - self._hierachie.get(Role.ADMIN) >= 0:
            roles.append(Role.ADMIN)
            currentRole = currentRole - self._hierachie.get(Role.ADMIN)

        if currentRole - self._hierachie.get(Role.USER) >= 0:
            roles.append(Role.USER)
            currentRole = currentRole - self._hierachie.get(Role.USER)

        if currentRole - self._hierachie.get(Role.AUTHENTICATED) >= 0:
            roles.append(Role.AUTHENTICATED)
            currentRole = currentRole - self._hierachie.get(Role.AUTHENTICATED)

        if currentRole - self._hierachie.get(Role.UNAUTHENTICATED) >= 0:
            roles.append(Role.UNAUTHENTICATED)
            currentRole = currentRole - self._hierachie.get(Role.UNAUTHENTICATED)

        return roles

    def hasRole(self,currentRole,target):
        return target in self.listRole(currentRole)
