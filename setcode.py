animals={"หมา","แมว","สิงโต","เสือ","ช้าง"}
animals.add("เป็ด")
animals.update(("หมู","ยีราฟ"))

pets = set(("หมา","แมว","กระต่าย","แม่น"))
print(animals)
print(pets)

data = animals.difference(pets)
print(data)