import json

class Editing:
    def __init__(self) -> None:
        pass
    
    def changing_data_by_internal_key(self, connection_key, minor_key, new_value):
        with open("bd.json", "r") as fl:
            temp = fl.read()
            transformation = json.loads(temp)
        
        master_key_data = transformation.get(str(connection_key))
        
        if master_key_data:
            for record in master_key_data:
                if minor_key in record:
                    record[minor_key] = new_value
                    break
                
        with open("bd.json", "w") as fl:
            json.dump(transformation, fl, indent=4)
        