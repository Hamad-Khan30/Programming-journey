from fastapi import FastAPI
from fastapi import Depends
app=FastAPI()

def pagination(skip: int=0, limit: int=100):
    if skip < 0:
        skip = 0
    if limit > 100:
        limit = 100

    return{"minimum limit":skip,
            "Our maximum limit is":limit}
    
@app.get("/product")
def addproducts( show = Depends(pagination)):
    return show

@app.get("/order")
def checkorders( show= Depends(pagination)):
        return show
