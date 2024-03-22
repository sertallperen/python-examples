class Girls:    
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color

    def Bilgi(self, g_1, g_2, g_3, g_4):
        a = (g_1.name, g_1.age, g_1.hair_color,
             g_2.name, g_2.age, g_2.hair_color,
             g_3.name, g_3.age, g_3.hair_color,
             g_4.name, g_4.age, g_4.hair_color)
        print(a)
    
g_1 = Girls('Ecem', 19, 'Black')
g_2 = Girls('Kinga', 24, 'Yellow')
g_3 = Girls('Alexis', 22, 'Brown')
g_4 = Girls('Valentine', 20, 'Red')

g_1.Bilgi(g_1, g_2, g_3, g_4)



