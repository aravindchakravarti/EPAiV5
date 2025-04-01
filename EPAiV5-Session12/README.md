# EPAiV5-Session12
EPAiV5 Session 12 assignment

# Details
Username: Aravind D. Chakravarti

Email : aravinddcsadguru@gmail.com

# Project Details
### Function 
```python
def cast_and_clean_data(data: list, cast_type: list) -> list:
    return [cast_func(value) if value != '' else 'N/A' for value, cast_func in zip(data, cast_type)]
```
Casts each element in the `data` list to the corresponding type specified in the `cast_type` list.
If data not exists then it appends by 'N/A'

This function takes two lists:
- `data`: A list of values to be cast.
- `cast_type`: A list of types or casting functions (such as `int`, `str`, etc.).

It then applies the corresponding type to each value in `data`. The function uses a list comprehension
that zips the `data` and `cast_type` lists, and applies the casting function to each element.

### Reading the file
```python
with open('nyc_parking_tickets_extract-1.csv') as file:
    # Read the header line and split it into a list of column names
    header_info = next(file).strip('\n').split(',')
```
Above opens the file in new context and reads the file in lazy way (line by line), we get the header by reading the first line

```python
# Create a namedtuple class with the column names from the header
ind_car_data = namedtuple('ind_car_data', header_info)
```
We create the named tuple using the header which extracted before

```python
# Process each line in the file
for line in file:
    # Split the line by commas and cast each element to the corresponding type
    line_data = cast_and_clean_data(line.strip("\n").split(','), cast_type)
```
We fetch each line, then we split each data by using `.` seperator and cast it using `cast_and_clean_data`

```python
# Update the vehicle manufacturer count in the dictionary
if car.Vehicle_make in vehicale_mfgr_match:
    vehicale_mfgr_match[car.Vehicle_make] += 1
else:
    vehicale_mfgr_match[car.Vehicle_make] = 1
```
We check if the key (corresponds to vehicle manufacturer) exists in our arrary, if exists, then we increment it by 1 else, we create the new entry in dictionary.

