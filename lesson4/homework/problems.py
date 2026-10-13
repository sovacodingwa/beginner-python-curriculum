import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.

systems = ["Windows","Linux","MacOS"]
length2 = len(systems)
last_system = systems[length2-1]
print("the last system is", last_system)
systems.reverse()
print(systems)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.

school = ["ELA","Math","Art","PE"]
length3 =  len(school)
second_to_last_school = school[length3-1]
print("The second to last subject is", second_to_last_school)
school.sort()
print(school)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.

error = ["low battery error","PEBKAC","tecnical error","cat's too lazy error","computer on fire error"]
print("there are",len(error),"errors")
for code in error:
    print(code)

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.

program = ["Python","BASIC"]
random_program = random.choice(program)
print(random_program)
program.append("C++")
print(program)

# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.

passwords = ["172016","123456","789012","284719","583447","478370"]
length4 = len(passwords)
mid_password = passwords[length4-3]
print(mid_password)
first_password = passwords.pop(0)
print(first_password)
print(passwords)
print("THE END! :)")