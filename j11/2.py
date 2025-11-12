family = {
    "father": {
        "name": {"fname": "ali", "lname": "rezaee"},
        "age": 45,
        "job": ["engineer", "driver"],
        "tel": {"mobile": "0912345678", "phone": "77886655"},
    },
    "mother": {
        "name": {"fname": "sara", "lname": "mohammadi"},
        "age": 44,
        "mobile": "09123232323",
    },
    "children": {
        "sons": {
            "son1": {"name": "reza", "age": 20, "job": "student"},
            "son2": {"name": "mohammad", "age": 18, "mobile": "09123454331"},
        },
        "girl": {"name": "ana", "age": 25, "job": ["accountant", "student"]},
    },
}

print(family["children"]["sons"]["son1"]["name"])
print(family["father"]["job"][1])
print(family["father"]["name"]["lname"])

for i in family["father"]["job"]:
    print(i, end=" ")