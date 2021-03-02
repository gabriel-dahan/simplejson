# SimpleJSON

## Read & Write
### Read a JSON file
```python
path = 'your/file/path.json'
data = Json.read(path)
```
### Write into a JSON file
```python
# Read
path = 'your/file/path.json'
data = Json.read(path)

# Edit
data['object'] = 'new_object'

# Write
Json.write(data, path, indent = 4) # indent is optional
```

## JSON data to class objects
### Exemple of conversion
```python
data = {'project': {'name': 'SimpleJSON', 'version': '1.0.1'}, 'author': 'TheGabDooSan'}
obj = Json.convert_to_obj(data)

print(obj.project.name)    # --> "SimpleJSON"
print(obj.project.version) # --> "1.0.1"
print(obj.author)          # --> "TheGabDooSan"
```