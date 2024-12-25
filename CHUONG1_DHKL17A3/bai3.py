class PS:
    def __init__(self, tso=0, mso=1):
        self.tso = tso
        self.mso = mso

    def kiemtra(self):
        return self.tso > 0 and self.mso > 0

    def nhap(self):
        self.tso = int(input("Nhập tử số: "))
        self.mso = int(input("Nhập mẫu số: "))

    def in_fraction(self):
        print(f"{self.tso} / {self.mso}")

# Example usage
ps = PS()
ps.nhap()
if ps.kiemtra():
    ps.in_fraction()
else:
    print("Tử số và mẫu số phải lớn hơn 0.")
