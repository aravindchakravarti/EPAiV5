# EPAiV5-Session15-CapStone

![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session15-CapStone/actions/workflows/python-app.yml/badge.svg)


![image](https://github.com/user-attachments/assets/51b47083-c38a-4fa3-b0aa-469a18fe2100)


## Summary
### What is implemented?
- Dataset loader for `MNIST` and `CIFAR-10`
### What is not implmeneted?
- Dataset loader for Text (NLP)


## Project Overview

This project implements a flexible and efficient DataLoader for handling various datasets, with a focus on MNIST and CIFAR-10. It demonstrates advanced Python concepts and best practices in software development.

## Features

- Supports multiple datasets (MNIST, CIFAR-10)
- Automatic dataset downloading and extraction
- Customizable preprocessing and data augmentation
- Efficient data loading with batching and shuffling
- Comprehensive unit tests
- CI/CD integration with GitHub Actions

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/aravindchakravarti/EPAiV5-Session15-CapStone.git
   cd EPAiV5-Session15-CapStone
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the DataLoader:

```python
from dataloader import DataLoader
#Initialize DataLoader
data_loader = DataLoader(dataset_name='MNIST', batch_size=32)
#Iterate over data
for batch in data_loader:
    # Process the batch
    print(f"Processing batch of size {len(batch)}")
```

## Project Structure

- `dataloader/`: Main package containing the DataLoader implementation
  - `__init__.py`: Package initializer
  - `dataloader.py`: Core DataLoader class
  - `preprocessors.py`: Data preprocessing functions
  - `utils.py`: Utility functions for file handling and timing
- `tests/`: Unit tests
  - `test_dataloader.py`: Comprehensive tests for the DataLoader
- `main.py`: Entry point for running the DataLoader
- `requirements.txt`: Project dependencies
- `.github/workflows/python-app.yml`: GitHub Actions CI configuration

## Advanced Python Concepts Demonstrated

1. Object-Oriented Programming
2. Decorators (`@timer`)
3. Context Managers
4. Generators and Iterators
5. Lambda Functions
6. List Comprehensions
7. Error Handling
8. Type Hinting (implied in the structure)
9. File I/O and Binary Data Handling
10. Use of Standard Library (os, sys, time, etc.)
11. Third-party Library Integration (numpy, matplotlib)
12. Command-line Argument Parsing
13. Modular Project Structure
14. Unit Testing
15. CI/CD Integration

## Running Tests

To run the unit tests:
```
python -m unittest discover tests
```
