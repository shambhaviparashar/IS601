from fastapi import FastAPI, HTTPException, Query, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import json

app = FastAPI()

db_file = 'db.sqlite'

class Customer(BaseModel):
    name: str
    email: str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class Order(BaseModel):
    customer_id: int
    item_id: int
    quantity: int
    order_date: str

@app.post("/customers/", response_model=Customer)
async def create_customer(customer: Customer):
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO customers (name, email) VALUES (?, ?)',
                (customer.name, customer.email)
            )
            conn.commit()
            customer_id = cursor.lastrowid
        return {"id": customer_id, **customer.dict()}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists")

@app.get("/customers/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM customers WHERE id = ?', (customer_id,))
        row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"id": row[0], "name": row[1], "email": row[2]}

@app.put("/customers/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, customer: Customer):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE customers SET name = ?, email = ? WHERE id = ?',
            (customer.name, customer.email, customer_id)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        conn.commit()
    return {"id": customer_id, **customer.dict()}

@app.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Customer not found")
        conn.commit()
    return {"detail": "Customer deleted successfully"}

@app.get("/customers/", response_model=List[Customer])
async def list_customers(
    limit: int = Query(10, description="Limit the number of customers returned"),
    name: Optional[str] = None
):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute(
                'SELECT * FROM customers WHERE name LIKE ? LIMIT ?',
                (f'%{name}%', limit)
            )
        else:
            cursor.execute('SELECT * FROM customers LIMIT ?', (limit,))
        rows = cursor.fetchall()
    return [{"id": row[0], "name": row[1], "email": row[2]} for row in rows]

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO items (name, description, price) VALUES (?, ?, ?)',
            (item.name, item.description, item.price)
        )
        conn.commit()
        item_id = cursor.lastrowid
    return {"id": item_id, **item.dict()}

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items WHERE id = ?', (item_id,))
        row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row[0], "name": row[1], "description": row[2], "price": row[3]}

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?',
            (item.name, item.description, item.price, item_id)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        conn.commit()
    return {"id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Item not found")
        conn.commit()
    return {"detail": "Item deleted successfully"}

@app.get("/items/", response_model=List[Item])
async def list_items(
    limit: int = Query(10, description="Limit the number of items returned"),
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        if min_price is not None and max_price is not None:
            cursor.execute(
                'SELECT * FROM items WHERE price BETWEEN ? AND ? LIMIT ?',
                (min_price, max_price, limit)
            )
        elif min_price is not None:
            cursor.execute('SELECT * FROM items WHERE price >= ? LIMIT ?', (min_price, limit))
        elif max_price is not None:
            cursor.execute('SELECT * FROM items WHERE price <= ? LIMIT ?', (max_price, limit))
        else:
            cursor.execute('SELECT * FROM items LIMIT ?', (limit,))
        rows = cursor.fetchall()
    return [{"id": row[0], "name": row[1], "description": row[2], "price": row[3]} for row in rows]

@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO orders (customer_id, item_id, quantity, order_date) VALUES (?, ?, ?, ?)',
            (order.customer_id, order.item_id, order.quantity, order.order_date)
        )
        conn.commit()
        order_id = cursor.lastrowid
    return {"id": order_id, **order.dict()}

@app.get("/orders/{order_id}", response_model=Order)
async def get_order(order_id: int):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
        row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": row[0], "customer_id": row[1], "item_id": row[2], "quantity": row[3], "order_date": row[4]}

@app.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order: Order):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE orders SET customer_id = ?, item_id = ?, quantity = ?, order_date = ? WHERE id = ?',
            (order.customer_id, order.item_id, order.quantity, order.order_date, order_id)
        )
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Order not found")
        conn.commit()
    return {"id": order_id, **order.dict()}

@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Order not found")
        conn.commit()
    return {"detail": "Order deleted successfully"}

@app.get("/orders/", response_model=List[Order])
async def list_orders(
    limit: int = Query(10, description="Limit the number of orders returned"),
    customer_id: Optional[int] = None
):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        if customer_id:
            cursor.execute(
                'SELECT * FROM orders WHERE customer_id = ? LIMIT ?',
                (customer_id, limit)
            )
        else:
            cursor.execute('SELECT * FROM orders LIMIT ?', (limit,))
        rows = cursor.fetchall()
    return [{"id": row[0], "customer_id": row[1], "item_id": row[2], "quantity": row[3], "order_date": row[4]} for row in rows]

@app.post("/upload-orders/")
async def upload_orders(file: UploadFile = File(...)):
    try:
        orders_data = json.load(file.file)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        try:
            for order in orders_data:
                cursor.execute(
                    'INSERT INTO orders (customer_id, item_id, quantity, order_date) VALUES (?, ?, ?, ?)',
                    (order['customer_id'], order['item_id'], order['quantity'], order['order_date'])
                )
            conn.commit()
        except KeyError:
            conn.rollback()
            raise HTTPException(status_code=400, detail="Order data missing required fields")

    return {"message": "Orders successfully uploaded"}
