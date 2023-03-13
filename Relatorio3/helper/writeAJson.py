import json
import os
from bson import json_util 

def writeAJson(data, name: str):
    try:
        parsed_json = json.loads(json_util.dumps(data))

        if not os.path.isdir("./json"): #se não existir uma pasta json, ele cria um
            os.makedirs("./json")
            

        with open(f"./json/{name}.json", 'w') as json_file: #cria um arquivo na pasta json
            json.dump(parsed_json, json_file,
                    indent=4,
                    separators=(',', ': '))
        print(f"JSON file {name}.json created successfully!")
    except Exception as e:
        print(e)