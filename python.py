# 1. Update Values in Dictionaries and Lists:

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['x'] = 30
print(x)
print(students)
print(sports_directory)
print(z)


# 2. Iterate Through a List of Dictionaries:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output+= f'{key} - {val},'
        print(output)

iterateDictionary(students)

#  3. Get Values From a List of Dictionaries:

def iterateDictionary2(key_names,some_list):
    for i in range(0,len(some_list)):
        for key,val in some_list[i].items():
            if key_names == key:
                print(val)
print(iterateDictionary2('first_name',students))


# 4. Iterate Through a Dictionary with List Values:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key, val in some_dict.items():
        print('                 ')
        print(f"{len(val)} {key.upper()}")
        for i in range(0,len(val)):
            print(val[i])

print(printInfo(dojo))