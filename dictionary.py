import sys

people = {
    "sajith":"6477469123",
    "ok perfect" : "9447772645"
}
name = input("name:")
if name in people:
    number = people[name]
    print(f"number:{number}")