import json 

with open('example_1.json', 'r') as file:
    data = json.load(file)
    
with open('example_2.json', 'r') as file:
    data1 = json.load(file)


def json_glance(file):
    print('top')
    n_master_key = len(file.items())
    for i in range(n_master_key):
        key = list(file.items())[i][0]
        value = list(file.items())[i][1]
        if isinstance(value, dict) == False:
            print(' |---', str(key))
        else:
            json_glance(value)
            

json_glance(data1)
