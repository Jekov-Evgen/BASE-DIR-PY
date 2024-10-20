import json

class Read:
    def __init__(self, name_file) -> None:
        self.name_file = name_file
    
    
    def read_connection_key(self, connection_key):
        try:
            with open(self.name_file, "r") as fl:
                temp = fl.read()
                transformation = json.loads(temp)
                result = transformation.get(str(connection_key))
                
                return result
        except:
            return "Error opening file"
    
    
    def read_connection_key_minor_key(self, connection_key, minor_key):
        try:
            with open(self.name_file, "r") as fl:
                temp = fl.read()
                transformation = json.loads(temp)
                master_key_data = transformation.get(str(connection_key))
                result = None
            
                if master_key_data:
                    for record in master_key_data:
                        if minor_key in record:
                            result = record.get(minor_key)
                            break
            
                return result
        except:
            return "Error opening file"
        
        
    def output_all_internal_key_data(self, minor_key):
        try:
            with open(self.name_file, "r") as fl:
                temp = fl.read()
                transformation = json.loads(temp)
                all_data = []
                result = []
            
                for key in transformation:
                    all_data.extend(transformation[key])  
            
                for data_dict in all_data:
                    if minor_key in data_dict:
                        result.append(data_dict[minor_key]) 
                
                return result
        except:
            return "Error opening file"