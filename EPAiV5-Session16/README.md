# EPAiV5-Session16
Session 16 assignment

![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session16/actions/workflows/python-app.yml/badge.svg)

## Completion: 7/10 Test Cases Are Complete

## Features

- Create and initialize inventory
- Update item information in the inventory
- Merge multiple inventories
- Retrieve items in a specific category
- Find the most expensive item in the inventory
- Check if an item is in stock
- View available categories

## Project Structure

- `inventory_system.py`: Contains the main implementation of the inventory management system.
- `test_cases.py`: Includes unit tests for the inventory management functions.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/aravindchakravarti/EPAiV5-Session16.git
   ```

2. Navigate to the project directory:
   ```
   cd EPAiV5-Session16
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the inventory management system, import the necessary functions from `inventory_system.py`:

Create a new inventory
```
inventory = create_inventory()
```
Update inventory
```
update_info = {'price': 1200, 'quantity': 7}
update_inventory(inventory, 'Electronics', 'Laptop', update_info)
```
... (use other functions as needed)