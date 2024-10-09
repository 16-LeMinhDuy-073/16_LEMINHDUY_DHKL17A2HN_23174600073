import json

# Đối tượng Python (ví dụ dictionary)
python_obj = {
    "name": "Minh Duy",
    "age": 19,
    "city": "Bắc Giang"
}

# Chuyển đối tượng Python thành chuỗi JSON
json_string = json.dumps(python_obj)

# In chuỗi JSON
print("Chuỗi JSON:")
print(json_string)

# In tất cả các giá trị trong đối tượng Python
print("Giá trị của từng khóa:")
for key, value in python_obj.items():
    print(f"{key}: {value}")
