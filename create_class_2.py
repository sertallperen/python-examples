class Cars: 
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color 

    def bilgi(self, c_1, c_2, c_3):
        a = (c_1.brand, c_1.year, c_1.color,
               c_2.brand, c_2.year, c_2.color,
               c_3.brand, c_3.year, c_3.color)
        print(a)

c_1 = Cars('BMW', 2015, 'Gold')
c_2 = Cars('MERCEDES', 2019, 'Black')
c_3 = Cars('AUDI', 2023, 'Purple')

c_1.bilgi = (c_1, c_2, c_3)
