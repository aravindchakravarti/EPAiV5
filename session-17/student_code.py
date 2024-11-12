def validate(dict_1, dict_2):
    def compare_nested_dict(template_dic, incoming_dict, path=''):
        errors = []  # List to store paths to missing keys
        
        for key, value in template_dic.items():
            current_path = f"{path}.{key}" if path else key  # Track the current path
            
            # Check if key is missing in the incoming dictionary
            if key not in incoming_dict:
                errors.append(current_path)  # Add missing key path to errors
                continue
            
            # If value is a nested dictionary, recurse
            if isinstance(value, dict):
                errors.extend(compare_nested_dict(value, incoming_dict[key], current_path))
        
        return errors

    # Run the comparison
    missing_keys = compare_nested_dict(dict_2, dict_1)

    # Prepare output based on the results
    if missing_keys:
        state = False
        error = "mismatched keys: " + ", ".join(missing_keys)
    else:
        state = True
        error = ''
    
    print (state, error)

    return state, error