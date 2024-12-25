import xml.etree.ElementTree as ET

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_xml(self):
        try:
            tree = ET.parse(self.file_path)  
            self.data = tree.getroot()      
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except ET.ParseError:
            print("Failed to parse XML file. Please check its structure.")

    def display_data(self):
        if self.data:
            for product in self.data.findall('product'):  
                name = product.find('name').text
                price = product.find('price').text
                quantity = product.find('quantity').text
                print(f"Product: {name}, Price: {price}, Quantity: {quantity}")
        else:
            print("No data to display. Make sure XML file was read successfully.")

# Sử dụng lớp XMLReader
path = 'D:/17A2DHKL/Lab 1/DATA/products.xml'  
reader = XMLReader(path)
reader.read_xml()
reader.display_data()
