s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)

# lookup
if 1 in s:
    print(True)

# remove
s.remove(3)

string = "aaaaaaaaaabbbbbbbbbbbbccccccccccceeeeeeeeee"
sett = set(string)

print(sett)

# hashmap - dict
d = {"greg": 1, "steve": 2, "rob": 3}

print(d)

# adding
d["arsh"] = 4

print(d)

# check
if "greg" in d:
    print(True)

print(d["greg"])

# loop for key, val
for key, val in d.items():
    print(f"key {key}: val {val}")
    

#output
# {1, 2, 3}
# True
# {'c', 'a', 'e', 'b'}
# {'greg': 1, 'steve': 2, 'rob': 3}
# {'greg': 1, 'steve': 2, 'rob': 3, 'arsh': 4}
# True
# 1
# key greg: val 1
# key steve: val 2
# key rob: val 3
# key arsh: val 4