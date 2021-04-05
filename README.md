# SimpleJSON

## Read & Write

### Import the package
```python
from simplerjson import <function>

# Exemple
from simplerjson import read, to_obj
# or
import simplerjson
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