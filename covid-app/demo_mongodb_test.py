import pymongo

myclient = pymongo.MongoClient()

staffdb = myclient["staff_database"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()

staffcol = staffdb["people"]

mydict = { "name": "John", "address": "Highway 37" }
print(y)
