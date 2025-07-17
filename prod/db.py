from pymongo import MongoClient
from datetime import *
# from deepTest import currUserId

client = MongoClient('localhost', port=27017)
prod_DB = client['products-db']
info = prod_DB['products']

def addMood(grade):
    day = {
        "mood" : grade,
        "date" : datetime.now('%D'),
        "user_id" : currUserId
    }
    info.insert_one(day)

def get_userMood():
    data = info.find({'user_id' : 1895572923})
    return data.to_list()


print(*get_userMood(), sep='\n')

data = {
    'День' : [a['date'] for a in get_userMood()]
}
print(data)

























#data = products.find()  Если втупую попробовать вывести data, то питон вернёт <Cursor object> - это итерируемый объект, забавы ради можно фиксить это либо .to_list() либо *[a for a in data], sep='\n'