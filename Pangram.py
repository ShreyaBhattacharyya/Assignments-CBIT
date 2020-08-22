def checkpangram(string):
    alphabet = ['a','b','c','d','e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #storing the alphabet in an array
    for char in alphabet:
        if char not in string.lower(): #taking each individual letter and checking if the entered string contains it
            return False
    return True

s = input("Enter a string:")
if checkpangram(s) == True:
    print("It is a pangram")
else:
    print("It is not a pangram")
