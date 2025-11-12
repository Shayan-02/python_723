# dictianary

car = {"brand" : "saipa motmaen", "model" : "pride", "year" : 1397}

car["color"] = "pink"
car.update({"speed" : 100})
car["brand"] = "dignity"

d = car.copy()

d["color"] = "brown"

# car[i] = car.get(i)

for i in car:
    print(i, "->", car.get(i))