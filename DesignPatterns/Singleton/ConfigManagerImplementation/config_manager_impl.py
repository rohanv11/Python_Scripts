from __future__ import annotations
from typing import Type, Any

from .config_manager import FileBasedConfigurationManager


class FileBasedConfigurationManagerImpl(FileBasedConfigurationManager):
    __instance = None
    # __lock = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    @staticmethod
    def get_instance() -> FileBasedConfigurationManager:
        return FileBasedConfigurationManagerImpl()

    @staticmethod
    def reset_instance() -> None:
        FileBasedConfigurationManagerImpl.__instance = None

    def get_configuration(self, key: str) -> str:
        return self.properties.get(key)

    def get_configuration_with_type(self, key: str, type_: Type) -> Any:
        if key not in self.properties:
            return None
        value = self.properties[key]
        return self.convert(value, type_)

    def set_configuration(self, key: str, value: str) -> None:
        self.properties[key] = value

    def remove_configuration(self, key: str) -> None:
        self.properties.pop(key)

    def clear(self) -> None:
        self.properties = {}
