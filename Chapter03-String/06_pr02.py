latter = '''Dear <|NAME|>,
You are selected!

Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Please enter your name --> ")
date = input("Please enter Date: --> ")

latter = latter.replace("<|NAME|>", name)
latter = latter.replace("<|DATE|>", date)

print(latter)