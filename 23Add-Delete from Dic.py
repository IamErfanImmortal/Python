person = {
    'name': 'Rose',
    'age': 33,
}
print(f' Hi {person.get("name")}')
if 'profession' not in person:
    person['profession'] = "Unknow"
    print(f' Proffession: {person.get("profession")}')
    person['profession'] = "Architect"
    person['hobbies'] = "Running , Reading"
print(f' Proffession: {person.get("profession")}')
print(f' Hobbies: {person.get("hobbies")}')
del person['hobbies']   
person.pop ('hobbies') 