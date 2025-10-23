fname = input("name: ")
lname = input("last name: ")
age = int(input("age: "))

# way1
print("your first name is", fname, ",your last name is", lname, ".", "\nSo your full name is", fname, lname, "\nYour age is", age*2, "years old.")

# way2 (f-string)
print(f"your first name is {fname} ,your last name is {lname}.\nSo your full name is {fname} {lname}.\nyour age is {age*2} years old.")

#way3 (format)
print("your first name is {} ,your last name is {}.\nSo your full name is {} {}.\nyour age is {} years old.".format(fname, lname, fname, lname, age*2))