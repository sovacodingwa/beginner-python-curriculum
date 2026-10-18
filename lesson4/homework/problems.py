import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
systems= ["windowss", "mac", "linux"]
length= len(systems)
print(systems[length-1])
systems.reverse()
print(systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects=["math","english","history","science"]
print(subjects[1])
subjects.sort()
print(subjects)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
error = ["404", "324","123","125","385"]
for i in range(len(error)):     
    print(error[i])

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
lang = ["python","java"]
num = random.randint(0,1)
print(lang[num])
lang.append("chicken")
print(lang)
# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["1234567890", "password", "qwerty", "12345","123456","admin123"]
print(passwords[len(passwords)//2])
passwords.remove(passwords[0])
print(passwords)