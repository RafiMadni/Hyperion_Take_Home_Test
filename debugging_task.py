# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) # NameError occurs, k should be key, ive corrected the name here and changed to key

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", # syntax error, incorrect quotation marks used, ive added the double quotation marks on d'oh 
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer']) # Keys need to be passed as a list, ive put the keys in a list using []

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!
    '''