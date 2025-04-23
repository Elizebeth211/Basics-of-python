####JSON file
import json
###Python object to a JSON string
data = {
    "name": "Liza",
    "age": 25,
    "city": "Ghent"
}

json_string = json.dumps(data)# Convert Python dictionary to JSON string
print(json_string)# Output: {"name": "Liza", "age": 25, "city": "Ghent"}

###JSON string to a python object
json_data = '{"name": "Liza", "age": 25, "city": "Ghent"}'
python_dict = json.loads(json_data) # Convert JSON string to Python dictionary
print(python_dict["name"])# Output: Liza

##save the python object to a JSON string
with open("data.json", "w") as file:
    json.dump(data, file)  # Save Python dictionary as a JSON file

##Reading JSON from a file
with open("data.json", "r") as file:
    data_from_file = json.load(file)  # Load JSON from file into Python dictionary
print(data_from_file)

###Formatting JSON for better readability
pretty_json = json.dumps(data, indent=4)
print(pretty_json)
##Output {
#        "name": "Liza",
#        "age": 25,
#        "city": "Ghent"
#        }

















