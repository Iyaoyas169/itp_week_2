# ITP Week 2 Day 1 (In-Class) Practice

# Dictionary

person_1 = {
    "first_name": "Scooby",
    "favorite_snack": "Rare Candy",
    "wears_glasses": True
    }

# verify the type of person_1 to be a dictionary by using type
#print(type(person_1))

# add a key value pair to person_1 with the last_name of Doo
person_1["last_name"] = "Doo"
#print(person_1)

# update person_1 favorite_snack to "Scooby Snacks"
person_1.update({"favorite_snack": "Scooby Snacks"})
#print(person_1)

# Remove the "wears_glasses" key:value from person_1
person_1.pop("wears_glasses")
#print(person_1)

# Print all KEY names in the dictionary, one by one:
# for x in person_1:
  # print(x)


# Print all VALUES in the dictionary, one by one:
# for x in person_1:
#   print(person_1[x])

# DICTIONARY SUB-LIST*

# You can also use the values() method to return values of a dictionary:

#for x in some_dict.values():
  #print(x)

# You can use the keys() method to return the keys of a dictionary:

#for x in some_dict.keys():
  #print(x)

# Loop through both keys and values, by using the items() method:

#for x, y in some_dict.items():
  #print(x, y)
