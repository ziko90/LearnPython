# Exercise 39 - Dictionaries
# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a bacis set of states and some cities in them
cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out soe cities

print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states
print('-' * 10)
print("Michigans's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using state then cities dict

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abrreviated {abbrev}")

# print every city in state
print('-' *10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now both at the same time
print('-' * 10)
for state, abbrev in list(states.items()): # zwraca liste w postaci [('Miasto', 'Skrot'), ('Miasto', 'Sktor')]
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('*' * 10)
print(list(states.items())) # dict.items() This method returns a list of tuple pairs
print('*' * 10)

print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas') #The method get() returns a value for the given key. If key is not available then returns default value None.


if not state:
    print('Sorry, no Texas.')

# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is {city}")

print('*' * 10)
print(states.get('Texas'))  # throw "None"
print('*' * 10)
print(states['New York'])  # 'NY'
#print(states['Texas'])  #key error 'Texas'

lis = list(states.items())
print(lis)
print(lis[1])
print(list(states.items())[0])

for i in range(len(lis)):
    print(lis[i])

print(states)
print(sorted(states))
print(sorted(states.items()))
new_lis = list(sorted(states.items()))
print(new_lis)
print('*' * 10)
# key=lambda t: t[0] sortuje po kluczu t[1] sortuje po wartosci klucza lub key = function
new = sorted(states.items(), key=lambda t: t[0])  #sorted by key
print(new)
print('*' * 10)
new1 = sorted(states.items(), key=lambda t: t[1])  #sorted by value
print(new1)
print('*' * 10)
new2 = sorted(states.items(), key=lambda t: len(t[0]))  #sorted by length of key string
new4 = sorted(states.items(), key=lambda t: len(t[0]), reverse=True)  #sorted by length of key string - reverse
print(f'sortowanie po dlugosci \n {new2}')
print(f'sortowanie po dlugosci - reverse \n {new4}')
print('*' * 10)
print('*' * 10)
print('sortowanie po nazwie\n', new)
new3 = sorted(states.items(), key=lambda t: t[0], reverse=True)  #sorted by key - reverse
print('sortowanie po nazwie - reverse \n', new3)
#test