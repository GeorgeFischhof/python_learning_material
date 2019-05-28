
# https://docs.python.org/3/library/json.html
# https://en.wikipedia.org/wiki/JSON
# http://json-schema.org/

import json


# Read json from file and from string

with open('people.json') as people_data:
    people_from_file = json.load(people_data)

    people_data.seek(0)  # go back to beginning of file
    people_string = people_data.read()

    people_from_string = json.loads(people_string)

print('people_from_file: \n', people_from_file)
print('people_from_string: \n', people_from_string)


# Write json to file and to string

my_car = {
    "type": "Tesla",
    "fuel": "electric",
    "mileage": 42,
}
with open('./car_output.json', 'w') as output_data:
        json.dump(my_car, output_data, indent=2)

car_json = json.dumps(my_car)
print('car_json: \n', car_json)
print('type car_json: \n', type(car_json))  # str ==> not dict, so really json
