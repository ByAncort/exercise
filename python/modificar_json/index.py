import json
def leer():
    
    with open('index.json', 'r') as f:
        return json.load(f)


def mostrarData():
    data=leer()
    for i in data:
        return print(i)
        for j in i:
            return print(i[j])


mostrarData()