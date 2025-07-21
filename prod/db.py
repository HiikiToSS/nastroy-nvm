from pymongo import MongoClient
from datetime import *

client = MongoClient('localhost', port=27017)
prod_DB = client['products-db']
info = prod_DB['products']

def addMood(grade, userID):
    print(datetime.now().strftime("%d.%m.%Y"))
    day = {
        "mood" : grade,
        'date' : datetime.now().strftime("%d.%m.%Y"),
        "user_id" : userID
    }
    info.insert_one(day)

def get_userINFO(userID):
    data = info.find({'user_id' : userID})
    return data.to_list()

def was_today(userID):
    last_date = info.find({'user_id' : userID}).to_list()
    curr_date = datetime.now().strftime("%d.%m.%Y")
    print([a['date'] for a in last_date][-1], '---', curr_date)
    return curr_date != [a['date'] for a in last_date][-1]



# print(*get_userMood(), sep='\n')

# data = {
#     'День' : [a['date'] for a in get_userMood()]
# }
# print(data)

























#data = products.find()  Если втупую попробовать вывести data, то питон вернёт <Cursor object> - это итерируемый объект, забавы ради можно фиксить это либо .to_list() либо *[a for a in data], sep='\n'