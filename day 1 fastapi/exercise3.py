from fastapi import FastAPI
from starlette import status
app=FastAPI()
@app.post("/product", status_code=status.HTTP_201_CREATED)
def add_product():
    return{"you added products successfuuly"}