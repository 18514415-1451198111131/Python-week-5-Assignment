# Defining the base class
class Superhero:
    def __init__(self, name):
        self.name = name

    def power(self):
        print(f"{self.name} has unique superhero powers.")

# Subclass 1: Superman
class Superman(Superhero):
    def power(self):
        print(f"{self.name} uses super strength and can fly!")

# Subclass 2: Batman
class Batman(Superhero):
    def power(self):
        print(f"{self.name} uses intelligence, gadgets, and martial arts!")

# Polymorphic function
def show_power(hero):
    hero.power()

# Creating superhero objects
superman = Superman("Superman")
batman = Batman("Batman")

# Displaying their powers using polymorphism
show_power(superman)
show_power(batman)
