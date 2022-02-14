import pymongo

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://m001-student:m001-mongodb-basics@sandbox.prtaa.mongodb.net/myFirstDatabase"
# set a 5-second connection timeout
myclient = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)


#print(myclient.list_database_names())

#mydb = myclient["ejemploventas"]
#mycol = mydb["DatosPersonaAnimal"]

#for x in mycol.find():
 # print(x)

mydb = myclient["ejemploventas"]
mycol = mydb["articulos"]

mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)

for x in mycol.find():
  print(x)