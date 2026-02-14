from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    id: int
    order_id: int
    amount: float
    status: str

payments_db = {}

@app.post("/payment")
def process_payment(payment: Payment):
    payments_db[payment.id] = payment
    # Logic to verify payment
    return {"message": "Payment processed successfully", "payment": payment}

@app.get("/payment/{payment_id}")
def get_payment(payment_id: int):
    return payments_db.get(payment_id, {"error": "Payment not found"})