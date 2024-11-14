## CI/CD and Details
Name: Aravind D. Chakravarti
This project uses GitHub Actions for continuous integration, running tests on Python 3.8 and 3.11.

![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session17/actions/workflows/python-app.yml/badge.svg)

## License

This project is open-sourced under the MIT License.


# Dictionary Operations Library

A Python library that provides robust dictionary validation and merging capabilities.

## Features

### 1. Dictionary Validation
The `validate()` function performs deep validation of dictionaries against a template, checking for:
- Type matching
- Missing keys
- Extra keys
- Nested dictionary validation

### 2. Dictionary Merging
Two implementations for merging multiple dictionaries:
- `merge_with_defaultdict()`: Uses collections.defaultdict
- `merge_with_counter()`: Uses collections.Counter

## Installation
```
pip install -r requirements.txt
```

## Usage

### Dictionary Validation
```python
from student_code import validate
# Define a template
template = {
  'user_id': int,
  'name': {
    'first': str,
    'last': str
    }
}

# Validate a dictionary
input_dict = {
  'user_id': 100,
  'name': {
    'first': 'John',
    'last': 'Doe'
    }
}
is_valid, error = validate(input_dict, template)
```


### Dictionary Merging
```python
from student_merge import merge_with_defaultdict, merge_with_counter
# Sample dictionaries
d1 = {'python': 10, 'java': 3}
d2 = {'java': 10, 'python': 6}
# Using defaultdict
result1 = merge_with_defaultdict(d1, d2)
# Using Counter
result2 = merge_with_counter(d1, d2)
```

## Testing

The project includes comprehensive test cases for both validation and merging functionalities. Run tests using:
```
pytest test_validate.py
pytest test_merge.py
```
