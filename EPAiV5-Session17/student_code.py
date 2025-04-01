def validate(input_dict, template_dict, path=''):
    # Helper function to format the error messages
    def format_error(error_type, key_path):
        return f"{error_type}: {key_path}"

    for key, template_value in template_dict.items():
        current_path = f'{path}.{key}' if path else key

        # Check if the key is missing in input_dict
        if key not in input_dict:
            return False, format_error("mismatched keys", current_path)

        input_value = input_dict[key]

        # Check for type mismatch
        if isinstance(template_value, dict):
            # Recursively validate nested dictionaries
            is_valid, error_message = validate(input_value, template_value, current_path)
            if not is_valid:
                return is_valid, error_message
        elif not isinstance(input_value, template_value):
            return False, format_error("bad type", current_path)

    # Check for extra keys in input_dict that aren't in template_dict
    for key in input_dict:
        current_path = f'{path}.{key}' if path else key
        if key not in template_dict:
            return False, format_error("mismatched keys", current_path)

    return True, ''  # Return True if all checks pass