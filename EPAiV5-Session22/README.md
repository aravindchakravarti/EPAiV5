# EPAiV5-Session22
Session - 22: Inheritance

# Python Inheritance and OOP Assignment
![Build Status](https://github.com/aravindchakravarti/EPAiV5-Session22/actions/workflows/python-app.yml/badge.svg)

## Overview

This project demonstrates object-oriented programming concepts in Python, focusing on inheritance, method overriding, method extension, delegation, and the use of slots. The implementation includes a hierarchy of classes representing different types of people (Person, Student, Professor, Employee) and a Location class utilizing slots.

## Class Structure

The project implements the following class hierarchy:

Person

├── Student

├── Professor

├── Employee

└── StudentProfessor (inherits from both Student and Professor)

## Features

- Base class `Person` with name, age, and job attributes
- Inheritance demonstration with specialized classes
- Method overriding and extension
- Multiple inheritance example with `StudentProfessor`
- Use of `__slots__` for memory optimization in `Location` class
- Comprehensive test suite using pytest
