
newAge=0

def edad(age,year):
    global newAge
    newAge=2070-year+age
    return newAge


print('Su edad en el 2070 será: ', edad(20, 2020))