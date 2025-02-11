class Animals:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

    def eat(self):
        return f"{self.name} is eating"

class Dog(Animals):
# pass -> let the class be without anything

    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed
    
    def bark(self):
        return f"{self.name} barks loudly"

class Cat(Animals):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def meow(self):
        return f"{self.name} meows"