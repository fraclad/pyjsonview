import json 

# some sample JSON files to test
with open('example_1.json', 'r') as file:
    data = json.load(file)
    
with open('example_2.json', 'r') as file:
    data1 = json.load(file)

def var_name(variable):
    """
    

    Parameters
    ----------
    variable : var
        this is the variable that we wish to get the name from.

    Returns
    -------
    variable name (str).

    """
    for name in globals():
        if eval(name) == variable:
            return(name)
        else:
            pass
          
def json_glance(file, first = True):
    """
    

    Parameters
    ----------
    file : dict
        input JSON file is interpreted as dict.
    first : bool, optional
        DESCRIPTION. The default is True.

    Returns
    -------
    text output with keys organized neatly for overview purposes.

    """
    if first == True:
        print(var_name(file))
        global hier 
        global trace 
        hier = 0
        trace = [0]
    else:
        hier = hier
    n_master_key = len(file.items())
    for i in range(n_master_key):
        key = list(file.items())[i][0]
        value = list(file.items())[i][1]
        spacer = ' ' * hier
        if isinstance(value, dict) == False:
            print(spacer,'|---', str(key))
            trace.append(0)
        else:
            print(spacer,'|---', str(key))
            hier += 5
            json_glance(value, first = False)
            trace.append(1)
        if trace[-1] == 1:
            hier -= 5
        else:
            hier = hier
            
json_glance(data1)

