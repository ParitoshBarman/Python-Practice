myDict = {
    "Fast": "In a quick manner",
    "Pari": "A Good boy",
    "Marks": [1,2,3],
    "annotherDict":{
        'Paritosh':'Playrer'
    },
    1:2
}

print(type(myDict))

print(list(myDict))
print(type(myDict))

print(myDict)

# Dictionary Methodes
print(myDict.keys())  # Prints the keys of the Dictonari
print(myDict['annotherDict'].keys())  # Prints the keys of keys of the Dictonari

print(myDict.values())  # Prints the values of the Dictonari
print(myDict['annotherDict'].values())  # Prints the values of values of the Dictonari


print(myDict.items())  # Prints the items of the Dictonari
print(myDict['annotherDict'].items())  # Prints the list of (keys, values) in Tuple 

print(myDict)
myDict.update({"Mamlet":"Puitta"})
print(myDict)


updateDict = {
    'kire':'oiiii',
    'bal':'dhur bal',
    "Pari": "Vary vary good boy" #  Vary vary important**********
}
myDict.update(updateDict)
print(myDict)

print(myDict.get('Pari')) # Prints valeu assosiated with key Pari
print(myDict['Pari']) #  # Prints valeu assosiated with key Pari


# Difference between .grt and [] Syntax in Dictionarys
print(myDict.get('Pari2')) #  Return None as Pari2 is not present in the Dictionary
print(myDict['Pari2']) #  Throw an error as Pari2 is not present in the Dictionary

