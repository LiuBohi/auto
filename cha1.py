
passwordFile = open("SecretPasswordFile.txt")
secretPassword = passwordFile.read()
secretPassword = secretPassword.rstrip()
print("Enter your password.")
typedPassword = input()
if str(typedPassword) == str(secretPassword):
    print("Access granted")
    if typedPassword == "12345":
        print("That password is one that an idiot puts on their luggage.")
else:
    print("Access denied.")
# example 1
print("Hello world.")
print('what is your name?')
myName = input()
print('It is good to know you, ' + myName)
print('THe length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
