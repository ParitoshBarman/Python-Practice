myDic = {"hi":'Kire',
'hello':"Ohe",
"fan":'Pakha',
'bakso':'Box'
}

print('Options are -->',myDic.keys())
# print('The meaning is--> ',myDic[input('Enter your word --> ')]) # New method that I found
# a = input('Enter your word --> ')
# print(myDic[a])
# Below line will not throw an error if the the key not present in the dictionary
print('The meaning is--> ',myDic.get(input('Enter your word --> '))) # New method that I found
