from dataclasses import dataclass


@dataclass
class DatabaseConnection:
    def __init__(self):
        self.is_free = True