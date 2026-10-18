import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
os_list = ["Linux", "macOS", "Windows"]
print(os_list[len(os_list) - 1])
os_list.reverse()
print(os_list)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["Math", "History", "Scince", "English"]
print(subjects[1])
subjects.sort()
print(subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
error_codes = [
    "ERR_CONNECTION_TIMED_OUT"
    "ERR_NAME_NOT_RESOLVED"
    "ERR_INTERENET_DISCONNECTED"
    "ERR_SLL_PROTOCOL_ERROR"
    "ERR_CONNECTION_REFUSED"
]
print(f"Number of error codes: {len(error_codes)}")
print("_" * 30)
for code in error_codes:
    print(code)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
languages = ["Python", "JavaSript"]
random_languages = random.choice(languages)
print(f"Randomly selected language: {random_languages}")
languages.append("Go")
print(f"Update list: {languages}")


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
import secrets
import string

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(characters) for _ in range(12))
passwords = [generate_password() for _ in range(6)]
print("Original List:", passwords)
middle_index = len(passwords) // 2
print("Middle Password:", passwords[middle_index])
remove_first = passwords.pop(0)
print("Removed First Password:", remove_first)
print("Remaining List:", passwords)


