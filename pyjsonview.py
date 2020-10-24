import json 

with open('example_1.json', 'r') as file:
    data = json.load(file)

def json_glance(file):
    print('master')
    for i in range(len(file)):
        if type(list(file.keys())[i]) != 'dict':
            print(' |--- ', list(file.keys())[i])
            
json_glance(data)

