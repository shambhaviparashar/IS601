
# Midterm Project: Dosa Restaurant Orders Processor

## Overview
This project processes order data for a Dosa restaurant from a JSON file, generating two output files:
1. **`customers.json`** – containing a mapping of customer phone numbers to customer names.
2. **`items.json`** – containing item names, prices, and the number of times each item has been ordered.

The script is designed as part of the Midterm Project for IS601, and aims to help the restaurant analyze customer orders and item popularity.

---

## Files and Structure

```
midterm_project/
│
├── midterm_project.py       # Python script that processes the orders
├── example_orders.json      # Sample input file with restaurant orders for testing
├── customers.json           # Output file containing customer phone numbers and names
└── items.json               # Output file containing item names, prices, and order counts
```

---

## Requirements
- **Python 3.x** must be installed on your system.

---

## How to Run

1. **Download/Clone** the repository to your local machine.
2. Ensure the `example_orders.json` file (or a similar JSON file) is present in the `midterm_project` folder.
3. Open a terminal and navigate to the `midterm_project` folder:
   ```bash
   cd path/to/midterm_project
   ```
4. Run the script using the following command:
   ```bash
   python midterm_project.py example_orders.json
   ```
   - This will read the orders from `example_orders.json` and generate the following two output files:
     - `customers.json`: Maps customer phone numbers to names.
     - `items.json`: Contains item names, prices, and the total number of times each item was ordered.

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

## Example Usage

Once the script is run, the following steps are executed:

1. The script reads the input JSON file (`example_orders.json`).
2. It extracts customer names and phone numbers, writing them to `customers.json`.
3. It processes all items, recording their prices and the total number of times they were ordered, and writes this data to `items.json`.

---

## Version Control

This project is managed through Git and is hosted on a private GitHub repository. The work has been completed in a dedicated branch named `MidtermProject`. Commits have been made throughout the development process to demonstrate progress, and collaborators (MattToegel and any graders) have been invited to review the project.

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
