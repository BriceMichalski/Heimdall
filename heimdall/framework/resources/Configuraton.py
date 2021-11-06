import yaml 

from heimdall.framework.model.meta.Singleton import Singleton

class Configuration(metaclass=Singleton): 

    def __init__(self) -> None:
        configFile = 'heimdall/config/application.yml'   # TODO : Allow env var like HEIMDALL_CONFIG_FILE fr override default config
        with open(configFile, "r") as stream:
            try:
                config = yaml.safe_load(stream)

                self._server = ServerConfiguration(config.get("server"))
                self._database = DatabaseConfiguration(config.get("database"))
                self._security = SecurityConfiguration(config.get("security"))

            except Exception as exc:
                print(exc)

    @property
    def server(self):
        return self._server

    @property
    def database(self):
        return self._database

    @property
    def security(self):
        return self._security

class SecurityConfiguration():
    
    def __init__(self,config) -> None:
        self._jwt_ttl_minutes = config.get('jwt_ttl_minutes')
        self._admin = AdminConfiguration(config.get("admin"))
    
    @property
    def admin(self):
        return self._admin
    
    @property
    def jwt_ttl_minutes(self):
        return self._jwt_ttl_minutes

class DatabaseConfiguration():

    def __init__(self, config :dict) -> None:
        self._path = config.get("path")

    @property
    def path(self):
        return self._path


class ServerConfiguration():

    def __init__(self, config :dict) -> None:
        self._host =  config.get("host")
        self._port =  config.get("port")
        self._debug = config.get("debug")
        self._secret = config.get('secret')

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port
    
    @property
    def debug(self):
        return self._debug
    
    @property
    def secret(self):
        return self._secret


class AdminConfiguration():

    def __init__(self, config :dict) -> None:
        self._username =  config.get("username")
        self._password =  config.get("password")

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password