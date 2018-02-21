from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test']



def createDevice(device):
    device_id = db['Devices'].insert_one(device).inserted_id
    print(device_id)

def createUser(user):
    user_id = db['Users'].insert_one(user).inserted_id
    print(user_id)

createDevice({"Test":"Device"})
