class Date:
 def __init__(self, day, month, year):
  self.day = day
  self.month = month
  self.year = year

 def display(self):
   print(self.day, self.month, self.year)

 def next(self):
  self.day += 1
  if self.day > 31:
   self.day = 1
  self.month += 1
  if self.month > 12:
   self.month = 1
  self.year += 1
  if self.year > 9999:
   self.year = 0

date = Date(1, 1, 2023)
date.display()
date.next()
date.display()