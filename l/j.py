import json

data = {"fecha": '13/02/12',"hora": '13:05', "dato": 1002}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

