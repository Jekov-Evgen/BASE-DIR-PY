from writing_data_to_a_file import Write
from reading_data_from_a_file import Read
from data_change import Editing

class Control:
    def __init__(self, name_file : str, connection_key : int, key_to_meaning, meaning):
        try:
            temp = name_file.split(".")
            
            if temp[1] == "json":
                self.write = Write(name_file, connection_key, key_to_meaning, meaning)
            self.read = Read(name_file)
            self.editing = Editing(name_file)
        except:
            return "You passed a non-json file, look at the name_file argument"