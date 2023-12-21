class Circus:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def get_name(self):
        return self.name

    def get_animals(self):
        return self.animals

    def add_animal(self, animal):
        self.animals.append(animal)
    
    def let_animals_make_sound(self):
        for animal in self.animals:
            print(animal.get_name(), 'makes', animal.make_sound())

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        return self.name
    
    def make_sound(self):
        return self.sound

class Bear(Animal):
    def __init__(self, name):
        super().__init__(name, 'roar')

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name, 'yiyiyiyiyiyiyi')

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, 'pawoo')

if __name__ == '__main__':
    circus = Circus('Big Apple Circus')
    animals = [Bear('Pooh'), Monkey('Kong'), Elephant('Jumbo')]
    for animal in animals:
        circus.add_animal(animal)
    circus.let_animals_make_sound()