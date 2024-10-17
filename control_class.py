from writing_data_to_a_file import Write
from reading_data_from_a_file import Read
from data_change import Editing

class Control:
    def __init__(self, connection_key : int, key_to_meaning, meaning) -> None:
        self.write = Write(connection_key, key_to_meaning, meaning)
        self.read = Read()
        self.editing = Editing()