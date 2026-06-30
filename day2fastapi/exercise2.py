from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class NoteCreate(BaseModel):
    title:str
    body:str
    secret_token:int
class OutputRespone(BaseModel):
    secret_token:int

@app.post("/notes")
def notecreate(note:NoteCreate,response_model=OutputRespone):
    return{"Essay:": response_model}
