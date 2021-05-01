import pymongo



myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["rasa"]

mycol = mydb["conversations"]



for x in mycol.find():
    if x['sender_id'] == "unity_participant":
        for item in x:
            for y in x['events']:
                print (y['event'])
                try:
                    print (y['name'])
                    print (y['action_text'])
                except:
                    pass