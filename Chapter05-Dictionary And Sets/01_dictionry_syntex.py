myDict = {
    1:3,
    "Fast": "In a quick manner",
    "Pari": "A Good boy",
    "Marks": [1,2,3],
    "annotherDict":{
        'Paritosh':'Playrer'
    }

}

print(myDict['Fast'])
print(myDict['Pari'])
print("Before changing --> ",myDict['Marks'])


myDict['Marks'] = [48,36]

print("After changing --> ",myDict['Marks'])
print(myDict['annotherDict'])
print(myDict['annotherDict']["Paritosh"])
