from typing import Optional
from fastapi import FastAPI, Query, Path
import uvicorn
from pydantic import BaseModel
from enum import Enum


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


"""
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    crap = "crap"
"""

app = FastAPI()

# kwargs, ge = 1 is greater than or equal to 1, le = less than or equal to, gt = greater than, gt/lt important for floats (0.0 not valid)


@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(title="The ID of the item to get", gt=0, le=1000), q: str
):  # or Query(default = ["foo", "bar"]) q: list = Query(default = []) this won't check contents of list unlike list[str]
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


"""
@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title = "The ID of the item to get"),
    q: list[str]
    | None = Query(
        default=None,
        title="Query String",
        description="Query string for the items to search in the database that have a good match ",
        alias = "item-query")
):  # or Query(default = ["foo", "bar"]) q: list = Query(default = []) this won't check contents of list unlike list[str]
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
"""


"""
# Query
@app.get("/items/")
async def read_items(q:str | None = Query(default = None, min_length = 3, max_length = 50, regex = "^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""

"""
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # different ways of working with enum values
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    if model_name == ModelName.crap.value:
        return {"model_name": model_name, "message": "CRAP"}
    return {"model_name": model_name, "message": "Have some residuals"}
"""
"""
# query parameters with defaults
@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
"""

"""
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price with tax": price_with_tax})
    return item_dict
"""

"""
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
"""
