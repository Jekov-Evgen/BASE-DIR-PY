import json

class Read:
    def __init__(self) -> None:
        pass
    
    def read_connection_key(self, connection_key):
        with open("bd.json", "r") as fl:
            temp = fl.read()
            transformation = json.loads(temp)
            result = transformation.get(str(connection_key))
            
            return result
        
tt = Read()        
print(tt.read_connection_key(1))