import json

# Ví dụ về dữ liệu JSON để chuyển đổi sang python
json_data = '{"name": "Duy", "age": 19, "city": "Bắc Giang"}'

# Chuyển đổi dữ liệu JSON thành đối tượng python 
python_object = json.loads(json_data)

# In đối tượng Python
print(python_object)
