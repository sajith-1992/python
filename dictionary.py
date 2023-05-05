import sys

people = {
    "sajith":"6477469123",
    "ok perfect" : "9447772645"
}
name = input("name:")
if name in people:
    print(f"number:{people[name]}")