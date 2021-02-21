# greeting = "Good morming, "
# name = "Paritosh"

# Concating two string
# c = greeting+name
# print(c)

name = "Paritosh"
print(name[3])
# name[3] = "d"  --> Does not work


print(name[2:6])

print(name[:6]) #--> Is same as print(name[0:6])
print(name[1:]) #--> Is same as print(name[1:7])
print(name[-5:-2]) #--> Is same as print(name[3:6])

name = "ParitoshIsAGoodBoy"
print(name[0::3])