import pymongo
from classes import Person

myclient = pymongo.MongoClient()
mydb = myclient["staff_database"]
mycollection = mydb["people"]

p = Person()
num_keys = p.get_num()

print(f"Number of keys = {num_keys}")

for i in range(num_keys):
    print(f"{p.get_key(i)} - {p.get_value(i)}")

print(f"Enter {p.get_key(0)}: ")
result = input()
p.give_value(0, result)
mydict = p.person

x = mycollection.insert_one(mydict)
print(x)

result = mycollection.find()
print(result.next())
print(result.count())
