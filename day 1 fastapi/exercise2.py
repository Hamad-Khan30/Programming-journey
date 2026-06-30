from fastapi import FastAPI
app=FastAPI()
@app.get("/tax")
def taxes(amount:float, rate: float=0.17):
    tax=amount*rate
    total=tax*amount
    return{"Tax=": tax,
           "Toatl= ": total}