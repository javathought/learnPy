phonebook3 = {}
phonebook3["John"] = 938477566
phonebook3["Jack"] = 938377264
phonebook3["Jill"] = 947662781
print(phonebook3)

phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook2)

for name, number in phonebook3.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook3["John"]
print(phonebook3)

phonebook2.pop("Jack")
print(phonebook2)

phonebook3 = {"John": 938477566, "Jack": 938377264, "Jill": 947662781, "Jake": 938273443}

# write your code here
phonebook3.pop("Jill")

# testing code
if "Jake" in phonebook3:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook3:
    print("Jill is not listed in the phonebook.")
