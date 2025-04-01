# inventory_system.py
import pprint

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    invntry_dict = dict(Electronics={}, Groceries={})
    return invntry_dict

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    if category in inventory:
        if item_name not in inventory[category]:
            inventory[category][item_name] = {}
            inventory[category][item_name].update(update_info)
        else:
            inventory[category][item_name].update(update_info)
    return inventory

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    for key in inv2:
        if (key in inv1 and
            isinstance(inv1[key], dict) and
            isinstance(inv2[key], dict)):
            merge_inventories(inv1[key], inv2[key])
        else:
            inv1[key] = inv2[key]
    
    return inv1

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    for key in inventory:
        if key == category:
            return inventory[category]
        elif isinstance(inventory[key], dict):
            result = get_items_in_category(inventory[key], category)
            if (result):
                return result
    
    # There is no such key
    return None

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    max_item = {'name': None, 'Value': 0}  # Initialize max_item with a default dictionary
    for key, value in inventory.items():
        if isinstance(value, dict):
            if 'price' in value:  # Check if the dictionary has 'price'
                if value['price'] > max_item['Value']:
                    max_item = {'name': value['name'], 'Value': value['price']}
            # Recursively search in nested dictionaries
            nested_max_item = find_most_expensive_item(value)
            if nested_max_item['Value'] > max_item['Value']:
                max_item = nested_max_item
    return max_item

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    item_details = {'name': None, 'quantity': None}  # Initialize item_details with default values
    for key, value in inventory.items():
        if key == item_name:
            item_details['name'] = value['name']  # Access the 'name' directly from value
            item_details['quantity'] = value['quantity']  # Access the 'quantity' directly
            return item_details
        elif isinstance(value, dict):
            result = check_item_in_stock(value, item_name)  # Recursively check nested dictionaries
            if result:  # If found in nested dict, return the result
                return result
    return None  # R

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    keys = []
    for key in inventory:
        keys.append(key)

    return keys

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    pass

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    pass

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    pass
