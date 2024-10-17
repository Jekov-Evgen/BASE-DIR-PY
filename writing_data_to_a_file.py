import json

class Write:
    def __init__(self, name_file : str, connection_key : int, key_to_meaning, meaning) -> None:
        self.__all_data = {}
        self.name_file = name_file
        
        temp = [{key_to_meaning : meaning}]
        self.__all_data[connection_key] = temp 
        
    def write_data(self, connection_key : int, key_to_meaning, meaning):
        temp = self.__all_data.get(connection_key)
        temp.append({key_to_meaning : meaning})
        
        self.__all_data[connection_key] = temp
        
        
    def new_connection_key(self, new_connection_key : int, key_to_meaning, meaning):
        temp = [{key_to_meaning : meaning}]
        self.__all_data[new_connection_key] = temp
        
    def write_BD(self):
        try:
            with open(self.name_file, "w"):
                pass
        
            with open(self.name_file, "w") as fl:
                json.dump(self.__all_data, fl, indent=4)
        except:
            return "Ошибка открытия файла"