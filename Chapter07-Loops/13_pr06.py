number = int(input("Enter the number-->"))

fact = 1
for i in range(1,(number+1)):
    fact = fact * i

print(f"The factrial of the {number} is {fact}")