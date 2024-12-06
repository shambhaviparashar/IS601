# Final Project: Dosa Restaurant Orders Processor with API

## Overview
This project expands on the Midterm Project by incorporating a REST API using FastAPI. The API provides CRUD operations for customers, items, and orders. It also processes order data for a Dosa restaurant from a JSON file, generating two output files:
1. **`customers.json`** – containing a mapping of customer phone numbers to customer names.
2. **`items.json`** – containing item names, prices, and the number of times each item has been ordered.

The script and API are designed as part of the Final Project for IS601, helping the restaurant analyze customer orders, item popularity, and manage data through a user-friendly API.

---

## Files and Structure

```
final_project/
│
├── api.py                 # FastAPI application for managing customers, items, and orders
├── init_db.py             # Script to initialize the SQLite database
├── customers.json         # Output file with customer phone-to-name mapping
├── items.json             # Output file with item data and popularity
├── example_orders.json    # Sample input file with restaurant orders for testing
└── README.md              # Project documentation
```

---

## Requirements
- **Python 3.x** must be installed on your system.
- Required Python packages:
  - `fastapi`
  - `uvicorn`
  - `sqlite3`
  - `python-multipart`

Install dependencies using:
```bash
pip install fastapi uvicorn python-multipart
```

---

## How to Run

### Running the Script

1. **Download/Clone** the repository to your local machine.
2. Ensure the `example_orders.json` file (or a similar JSON file) is present in the `final_project` folder.
3. Open a terminal and navigate to the `final_project` folder:
   ```bash
   cd path/to/final_project
   ```
4. Run the script to process orders:
   ```bash
   python midterm_project.py example_orders.json
   ```
   - This will generate the following two output files:
     - `customers.json`: Maps customer phone numbers to names.
     - `items.json`: Contains item names, prices, and the total number of times each item was ordered.

### Running the API

1. Initialize the database:
   ```bash
   python init_db.py
   ```
   This creates the SQLite database (`db.sqlite`) with the required tables.

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   - The server will run at `http://127.0.0.1:8000`.
   - Swagger documentation for the API is available at `http://127.0.0.1:8000/docs`.

---

## Input Format (`example_orders.json`)

The input JSON file should have the following structure:

```json
[
  {
    "name": "John Doe",
    "phone": "123-456-7890",
    "items": [
      {"name": "Butter Masala Dosa", "price": 12.95},
      {"name": "Plain Dosa", "price": 8.95}
    ]
  },
  {
    "name": "Jane Smith",
    "phone": "987-654-3210",
    "items": [
      {"name": "Cheese Masala Dosa", "price": 14.50},
      {"name": "Butter Masala Dosa", "price": 12.95}
    ]
  }
]
```

Each order should contain:
- **Customer Name**: The name of the customer.
- **Phone Number**: A string representing the customer's phone number (in the format `xxx-xxx-xxxx`).
- **Items**: A list of items, where each item has a `name` (string) and `price` (float).

---

## API Endpoints

### Customers
- **POST `/customers/`**: Add a new customer.
- **GET `/customers/{id}`**: Retrieve a customer by ID.
- **PUT `/customers/{id}`**: Update a customer's information.
- **DELETE `/customers/{id}`**: Delete a customer.
- **GET `/customers/`**: List customers with optional filters.

### Items
- **POST `/items/`**: Add a new item.
- **GET `/items/{id}`**: Retrieve an item by ID.
- **PUT `/items/{id}`**: Update an item's details.
- **DELETE `/items/{id}`**: Delete an item.
- **GET `/items/`**: List items with optional filters.

### Orders
- **POST `/orders/`**: Add a new order.
- **GET `/orders/{id}`**: Retrieve an order by ID.
- **PUT `/orders/{id}`**: Update an order's details.
- **DELETE `/orders/{id}`**: Delete an order.
- **GET `/orders/`**: List orders with optional filters.

---

## List View and Filters

This project implements:

### **Limited List View**
All collections (`customers`, `items`, `orders`) support limiting the number of results returned using the `limit` query parameter. The default limit is `10` if not specified.

#### Examples:
- List a maximum of 5 customers:
  ```
  GET /customers/?limit=5
  ```
- List a maximum of 3 items:
  ```
  GET /items/?limit=3
  ```
- List a maximum of 7 orders:
  ```
  GET /orders/?limit=7
  ```

### **Filter Parameters**

Each collection supports logical filters:

#### **Customers**:
- Filter by name (partial match):
  ```
  GET /customers/?name=John
  ```

#### **Items**:
- Filter by price range:
  ```
  GET /items/?min_price=10&max_price=20
  ```
- Filter by minimum price only:
  ```
  GET /items/?min_price=15
  ```
- Filter by maximum price only:
  ```
  GET /items/?max_price=25
  ```

#### **Orders**:
- Filter by customer ID:
  ```
  GET /orders/?customer_id=2
  ```

---

## Output Files

1. **`customers.json`**
   - Contains a mapping of phone numbers to customer names:
     ```json
     {
       "123-456-7890": "John Doe",
       "987-654-3210": "Jane Smith"
     }
     ```

2. **`items.json`**
   - Contains item names as keys, and for each item:
     - The price of the item.
     - The number of times the item was ordered.
     ```json
     {
       "Butter Masala Dosa": {
         "price": 12.95,
         "orders": 2
       },
       "Plain Dosa": {
         "price": 8.95,
         "orders": 1
       },
       "Cheese Masala Dosa": {
         "price": 14.50,
         "orders": 1
       }
     }
     ```

---

## Version Control

This project is managed through Git and is hosted on a GitHub repository. The `MidtermProject` branch contains the original implementation, while the `FinalProject` branch extends it with API functionality. Regular commits demonstrate progress throughout development.

---

## How to Contribute

If you wish to contribute to this project:
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Make your changes and commit them with a descriptive message.
4. Push to the branch and create a Pull Request.

---

## Author

**Shambhavi** – IS601 Student
