from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    id: int
    product_id: int
    quantity: int

orders_db = {}

@app.post("/order")
def create_order(order: Order):
    orders_db[order.id] = order
    return {"message": "Order placed successfully", "order": order}

@app.get("/order/{order_id}")
def get_order(order_id: int):
    return orders_db.get(order_id, {"error": "Order not found"})
