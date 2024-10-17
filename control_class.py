from writing_data_to_a_file import Write
from reading_data_from_a_file import Read
from data_change import Editing

class Control:
    def __init__(self, name_file, connection_key : int, key_to_meaning, meaning) -> None:
        self.write = Write(name_file, connection_key, key_to_meaning, meaning)
        self.read = Read(name_file)
        self.editing = Editing(name_file)