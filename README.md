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
Json.write(data, path)
```

## JSON data to class objects
### Exemple of conversion
```python
data = {'project': {'name': 'SimpleJSON', 'version': '1.0.1'}, 'author': 'TheGabDooSan'}
obj = Json.to_obj(data)

print(obj.project.name)    # --> "SimpleJSON"
print(obj.project.version) # --> "1.0.1"
print(obj.author)          # --> "TheGabDooSan"
```

## Doc
```python
class simplejson.Json()
```
* `@classmethod read(path, cls = None, object_hook = None, parse_float = None, parse_int = None, parse_constant = None, object_pairs_hook = None, **kwds)`
* `@classmethod write(data, path, skipkey = False, ensure_ascii = True, check_circular = True, allow_nan = True, cls = None, indent = None, separators = None, default = None, sort_keys = False **kwds)`