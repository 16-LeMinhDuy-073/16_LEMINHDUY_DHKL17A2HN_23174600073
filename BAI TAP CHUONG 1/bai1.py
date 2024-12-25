class HinhChuNhat:
 def __init__(self, chiều_dài, chiều_rộng):
  self.chiều_dài = chiều_dài
  self.chiều_rộng = chiều_rộng

 def nhap_dung_lieu(self):
  self.chiều_dài = float(input("Nhập chiều dài của hình chữ nhật: "))
  self.chiều_rộng = float(input("Nhập chiều rộng của hình chữ nhật: "))

 def tinh_chu_vi(self):
  return 2 * (self.chiều_dài + self.chiều_rộng)

 def tinh_dien_tich(self):
  return self.chiều_dài * self.chiều_rộng

 def in_thong_tin(self):
  print("Chiều dài: ", self.chiều_dài)
  print("Chiều rộng: ", self.chiều_rộng)
  print("Chu vi: ", self.tinh_chu_vi())
  print("Diện tích: ", self.tinh_dien_tich())
hinh_chu_nhat = HinhChuNhat(10, 5)
hinh_chu_nhat.nhap_dung_lieu()
hinh_chu_nhat.in_thong_tin()