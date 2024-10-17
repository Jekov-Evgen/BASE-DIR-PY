import json

class Write:
    def __init__(self, connection_key : int, key_to_meaning, meaning) -> None:
        self.__all_data = {}
        
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
        with open("bd.json", "w"):
            pass
        
        with open("bd.json", "w") as fl:
            json.dump(self.__all_data, fl, indent=4)