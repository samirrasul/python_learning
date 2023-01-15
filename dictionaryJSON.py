import json

person = {'name': 'Jacob', 'age': 24, 'birth place': 'London', 'has children': False, 'professions': ['mathemtician', 'engineer']}

personJSON = json.dumps(person, indent=4)

print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

person1 = json.loads(personJSON)
print(person1)