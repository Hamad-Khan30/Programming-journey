from fastapi import FastAPI
app=FastAPI()
@app.get("/ping")
def ping():
    return {"pong": True}


@app.get("/echo/{word}")
def echo_word(word:str):
    return{"Word:": word[::-1]}
