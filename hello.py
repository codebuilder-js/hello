# This program says hello and asks for my name

print('Hello, world!')
print('What is your name?')

userName = input()

print('It is good to meet you, ' + userName)
print('The length of your name is: ' + str(len(userName)))
print('What is your age?')

userAge = input()

print('You will be ' + str(int(userAge) + 1) + ' in a year.')
