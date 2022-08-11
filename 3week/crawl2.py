import requests
from bs4 import BeautifulSoup
from pymongo.mongo_client import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.local

collection = db.yes24

rows = collection.find()
for row in rows :
    print(row['Title'])  # 이렇게 하면 한줄씩 쳐서 나오게 하기 가능 ! 
    # print(row.Title)   >> 이건 안됨

# res = requests.get("http://www.yes24.com/24/Category/BestSeller")
# soup = BeautifulSoup(res.text, "html.parser")

# for i in range(40) :
#     idx = str(i+1)
#     if idx == "19":
#         idx = "19_line"
#     elif idx == "20" :
#         idx = "20_line"
#     sstr = "#bestList > ol > li.num" + idx + " > p:nth-child(3) > a"
#     ts = soup.select_one(sstr)
 
#     db['yes24'].insert_one({
#         'Title' : ts.text
#     })