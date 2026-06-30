from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app=FastAPI()

class NoteCreate(BaseModel):
    title:str=Field(min_length=3,max_length=80)
    body:str=Field(max_length=5000)

    @field_validator("body", "title")
    @classmethod
    def blankbody(cls,value):
        if value.strip() =="":
            raise ValueError ("Spaces are not allowed")
        return value
    

@app.post("/notes")
def notecreate(note:NoteCreate):
    return{"Essay:":note}
