import json

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

DB_PASSWORD = "6yt9h3"
db = dict()
db_type = "dict"
# db = list()
# db_type = "list"

# handle POST request
@app.post("/items/{item_id}")
def create_item(item_id, i):
    # i means item, but we need to parse it from json
    i = json.loads(i)
    # if the item is actually an item, then we can create it
    if i["type"] == "item":
        print("Creating item with ID:" + item_id + "and data:" + str(i))
        if db_type == "list":
            db.append({"item_id": item_id, "item": i})
        else:
            db[item_id] = i
        return {"item_id": item_id, "item": i}

@app.get("/items/{item_id}")
def read_item(item_id):
    if db_type == "list":
        item = next(i for i in db if i["item_id"] == item_id)
    else:
        item = db.get(item_id)
    return {"item_id": item_id, "item": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
