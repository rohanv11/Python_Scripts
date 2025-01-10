from typing import Optional
import threading

from .connection_pool import ConnectionPool
from .database_connection import DatabaseConnection


class ConnectionPoolImpl(ConnectionPool):
    __instance = None
    __lock = threading.Lock()

    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.connection_pool = self.initialize_pool(max_connections)

    @staticmethod
    def get_instance(max_connections) -> ConnectionPool:
        if ConnectionPoolImpl.__instance is None:
            with ConnectionPoolImpl.__lock:
                if ConnectionPoolImpl.__instance is None:
                    ConnectionPoolImpl.__instance = ConnectionPoolImpl(max_connections)
        
        return ConnectionPoolImpl.__instance

    @staticmethod
    def reset_instance() -> None:
        ConnectionPoolImpl.__instance = None

    def initialize_pool(self, max_connections) -> None:
        return [DatabaseConnection() for i in range(max_connections)]

    def get_connection(self) -> Optional[DatabaseConnection]:
        for connection in self.connection_pool:
            if connection.is_free:
                connection.is_free = False
                return connection
        
        return None

    def release_connection(self, connection: DatabaseConnection) -> None:
        connection.is_free = True

    def get_available_connections_count(self) -> int:
        return sum([1 for connection in self.connection_pool if connection.is_free])

    def get_total_connections_count(self) -> int:
        return self.max_connections
