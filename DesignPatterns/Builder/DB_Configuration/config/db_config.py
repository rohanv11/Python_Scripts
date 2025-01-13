from __future__ import annotations

from dataclasses import dataclass

from .builder import Builder


@dataclass
class DatabaseConfiguration:
    database_url: str
    username: str
    password: str
    max_connections: int
    enable_cache: bool
    is_read_only: bool

    @staticmethod
    def builder() -> DatabaseBuilder:
        return DatabaseConfiguration.DatabaseBuilder()

    class DatabaseBuilder(Builder["DatabaseConfiguration"]):

        def __init__(self):
            self._instance = DatabaseConfiguration(None, None, None, None, None, None)
        
        def set_database_url(self):
            self.database_url = self._instance.database_url
            return self
        
        def set_username(self):
            self.username = self._instance.username
            return self

        def set_password(self):
            self.password = self._instance.password
            return self

        def set_max_connections(self):
            self.max_connections = self._instance.max_connections
            return self

        def set_enable_cache(self):
            self.enable_cache = self._instance.enable_cache
            return self


        def set_is_read_only(self):
            self.is_read_only = self._instance.is_read_only
            return self

        def build(self) -> DatabaseConfiguration:
            self.set_database_url() \
                .set_username()  \
                .set_password()  \
                .set_max_connections() \
                .set_enable_cache() \
                .set_is_read_only()

            return DatabaseConfiguration(self.database_url, self.username, self.password, self.max_connections, self.enable_cache, self.is_read_only)