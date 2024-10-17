import json

class Editing:
    def __init__(self, name_file : str) -> None:
        self.name_file = name_file
    
    def changing_data_by_internal_key(self, connection_key, minor_key, new_value):
        try:
            with open(self.name_file, "r") as fl:
                temp = fl.read()
                transformation = json.loads(temp)
        
            master_key_data = transformation.get(str(connection_key))
        
            if master_key_data:
                for record in master_key_data:
                    if minor_key in record:
                        record[minor_key] = new_value
                        break
                
            with open(self.name_file, "w") as fl:
                json.dump(transformation, fl, indent=4)
        except:
            return "Ошибка открытия файла"
        