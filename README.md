# SimpleJSON

## Read & Write

### Install and Import the module :

Installing the module :
```bash
~ git clone https://github.com/gabriel-dahan/simpler-json/
~ cd simpler-json/

# Linux / MacOS
~ python3 -m pip install -U .

# Windows 
~ py -3 -m pip install -U .
```
_Consider using the `--user` parameter if you're not a root/admin user._
Importing the module :
```python
import simplerjson
# or
from simplerjson import <function>

# Exemple
from simplerjson import read, to_obj
```
### Read a JSON file
```python
path = 'your/file/path.json'
data = simplerjson.read(path)
```
### Write into a JSON file
```python
# Read
path = 'your/file/path.json'
data = simplerjson.read(path)

# Edit
data['object'] = 'new_object'

# Write
simplerjson.write(data, path)
```

## JSON data to class objects
### Exemple of conversion
```python
data = {'project': {'name': 'SimpleJSON', 'version': '1.0.1'}, 'author': 'TheGabDooSan'}
obj = simplerjson.to_obj(data)

print(obj.project.name)    # --> "SimpleJSON"
print(obj.project.version) # --> "1.0.1"
print(obj.author)          # --> "TheGabDooSan"
```