import pymongo

client = pymongo.MongoClient("mongodb+srv://anubhav:ar66007@anubhav.xbat2.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database=client['my_database']
collections=database['Table1']

record=collections.find()

for i in record:
    print(i)

#data=collections.find({"companyName":"iNeuron"})

#for i in data:

 #   print(i)

 data1=collections.find({"courseOffered":{"$gt": "E"}})
 for i in data1:
     print(i)