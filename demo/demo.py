import json

data = {"name": "John", "age": 30, "city": "New York"}
json_str = json.dumps(data, indent=None)

print(json_str) # 输出：{"name": "John", "age": 30, "city": "New York"}

decoded_data = json.loads(json_str)

print(decoded_data) # 输出：{'name': 'John', 'age': 30, 'city': 'New York'}