class Employee:
 def __init__(self, ht, ngay_sinh, ngay_vao_cong_ty):
  self.ht = ht
  self.ngay_sinh = ngay_sinh
  self.ngay_vao_cong_ty = ngay_vao_cong_ty

 def print_info(self):
  print(f"Họ tên: {self.ht}")
  print(f"Ngày sinh: {self.ngay_sinh}")
  print(f"Ngày vào công ty: {self.ngay_vao_cong_ty}")

employee_list = []


employee_1 = Employee("Nguyễn Văn A", "1990-10-10", "2010-1-1")
employee_2 = Employee("Trần Thị B", "1985-5-5", "2005-1-1")
employee_3 = Employee("Phạm Văn C", "1995-2-2", "2015-1-1")

employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(employee_3)

for employee in employee_list:
 employee.print_info()