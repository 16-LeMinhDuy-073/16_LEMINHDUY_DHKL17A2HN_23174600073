class TS:
 def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
  self.ho_ten = ho_ten
  self.diem_toan = diem_toan
  self.diem_ly = diem_ly
  self.diem_hoa = diem_hoa

 def tinh_tong_diem(self):
  return self.diem_toan + self.diem_ly + self.diem_hoa

 def in_thong_tin(self):
  print(f"Ho ten: {self.ho_ten}")
  print(f"Diem Toan: {self.diem_toan}")
  print(f"Diem Ly: {self.diem_ly}")
  print(f"Diem Hoa: {self.diem_hoa}")
danh_sach_ts = []
while True:
 ho_ten = input("Nhap ho ten thi sinh: ")
 diem_toan = float(input("Nhap diem Toan: "))
 diem_ly = float(input("Nhap diem Ly: "))
 diem_hoa = float(input("Nhap diem Hoa: "))
 ts = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
 danh_sach_ts.append(ts)
 print("Danh sach thi sinh:")
 for ts in danh_sach_ts:
  ts.in_thong_tin()
 if ts.tinh_tong_diem() >= 500:
  print("Thi sinh trúng tuyen")
 else:
  print("Thi sinh khong trúng tuyen")