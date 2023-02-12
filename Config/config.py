import json
def writeConfig(setting, value):
    with open('Config/config.json','r+') as file:
        data = json.load(file)
        data[setting] = value
        file.seek(0)
        json.dump(data,file,indent=4)
        file.truncate()

def readConfig(setting):
    with open('Config/config.json', 'r') as f:
        data = json.load(f)
    return(data[setting])


        
