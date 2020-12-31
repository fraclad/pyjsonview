import json 

with open('example_1.json', 'r') as file:
    data = json.load(file)
    
with open('example_2.json', 'r') as file:
    data1 = json.load(file)

def print_var_name(variable):
    for name in globals():
        if eval(name) == variable:
            print(name)
        
def json_glance(file):
    print_var_name(file)
    n_master_key = len(file.items())
    for i in range(n_master_key):
        key = list(file.items())[i][0]
        value = list(file.items())[i][1]
        hier = 0
        if isinstance(value, dict) == False:
            spacer = ' ' * hier
            print(spacer,'|---', str(key))
        else:
            spacer = ' ' * hier
            print(spacer,'|---', str(key))
            hier += 4            
            json_glance(value)
            
json_glance(data1)
