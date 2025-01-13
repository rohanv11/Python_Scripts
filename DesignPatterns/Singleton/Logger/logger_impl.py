from .logger import Logger, LogLevel
import time


class LoggerImpl(Logger):
    __instance = None

    def __init__(self):
        self.filepath = None
        self.log_buffer = []

    @classmethod
    def get_instance(cls) -> Logger:
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @classmethod
    def reset_instance(cls) -> None:
        cls.__instance = None

    def log(self, level: LogLevel, message: str) -> None:
        if not self:
            raise Exception("logger not instantiated")

        if not  self.get_log_file():
            raise Exception("filepath not specified")

        data = (level, message)
        self.log_buffer.append(data)
        
        

    def set_log_file(self, file_path: str) -> None:
        LoggerImpl.file_path = file_path

    def get_log_file(self) -> str:
        if LoggerImpl.file_path:
            return LoggerImpl.file_path

    def flush(self) -> None:
        if not self.get_log_file():
            raise Exception("filepath not specified")
        
        with open(self.get_log_file(), "w") as file:
            for item in self.log_buffer:
                file.write(str(item) + "\n")
            
            self.log_buffer = []


    def close(self) -> None:
        pass
