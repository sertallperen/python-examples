class Dog:
    def __init__(self, color, age, origin, name):
        self.color = color 
        self.age = age
        self.origin = origin
        self.name = name

    def bark_voice_of_dog(self):
        print('Hav')

    def one_more_year(self):
        self.age += 1

first_dog = Dog('White',5, 'Turkey', 'Ates')
second_dog = Dog('Black',2, 'Holland', 'Daesy')
third_dog = Dog('Brown',11, 'Germany', 'Mark')

first_dog.bark_voice_of_dog()


