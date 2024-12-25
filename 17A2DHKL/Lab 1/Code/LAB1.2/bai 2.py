import json

class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_json(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in {self.file_path}.")
    
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, Address: {user['address']}")
        else:
            print("No data to display.")

# Sử dụng lớp JSONReader
path = 'D:/17A2DHKL/Lab 1/DATA/users.json'
reader = JSONReader(path)
reader.read_json()
reader.display_data()
