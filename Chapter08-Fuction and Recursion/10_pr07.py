def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


this = "      Pari is a good boy    "
word = "Pari"


print(this)
print(this.strip())




n = remove_and_split(this, word)
print(n)
