example_dictionary = {'first_name': "Terrance", 'last_name': "KOAR", 'favorite_language': "Python"}
print(example_dictionary.items())
 type(example_dictionary.items())
for key, value in example_dictionary.items():
    print("this is the key:", key)    
    print("this is the value:", value, "\n")