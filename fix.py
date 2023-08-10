class Animal:
    def __init__(self, species):
        self.species = species
    def set_species(self, species):
        self.species = species
    def get_species(self):
        return self.species

turtle1 = Animal("turtle")
turtle2 = Animal("turtle")
unknown = Animal("")
hare = Animal("hare")
animals = [turtle1, turtle2, unknown, hare]
for animal in animals:
    print(animal.get_species(), end="; ")
    unknown.set_species("beaver")

class Pet(Animal):
    def __init__(self, name, age, species):
        super().__init__(species)
        self.name = name
        self.age = age
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def get_name(self):
        return (self.name)
    def get_age(self):
        return(self.age)
    def isYounger(self, pet):
        if self.age < pet.get_age():
            return True
        else:
            return False

cat = Pet("Fluffy", 3, "cat")
dog = Pet("Tobby", 5, "dog")
if cat.isYounger(dog):
    print(cat.get_name() + " is younger than " + dog.get_name())
else:
    print(f"{dog.get_name()} is younger than {cat.get_name()}")
for animal in animals:
    print(animal.get_species(), end = "; ")
    

class ZooAnimal(Pet):
    aged = 7                                                       
mountainlion = ZooAnimal("Rocky", 5, "leopard")
snowleopard = ZooAnimal("Snowy", 3, "leopard")
tiger = ZooAnimal("Sunny", 8, "tiger")
cats = [mountainlion, snowleopard, tiger]
for animal in cats:
    if animal.get_age() < ZooAnimal.aged:     
        print(animal.get_name() + " is a young cat.")
    else:
        print(animal.get_name() + " is an old cat.")
tiger.set_name("Honey")
print(tiger.get_name())
class ZooAnimal(Pet):
    def aged(self):
        species = self.get_species()
        if (species == "tiger"):
            aged = 7.0
        elif (species == "lion"):
            aged = 6.0
        else:
            aged = 8.0
        return aged

class Tiger(ZooAnimal):
    def aged(self):
        return 7.5

 

class Lion(ZooAnimal):
    def aged(self):
        return 6.5

 

leopard = ZooAnimal("Snowy", 3.0, "leopard")
tiger = Tiger("Sunny", 8.0, "tiger")
lion = Lion("Rocky", 4.0, "lion")
cats = [lion, leopard, tiger]
for animal in cats:
    if animal.get_age() < animal.aged():
        print(f"{animal.get_name()} is a young cat because it is less than {animal.aged()} years old.")
    else:
        print(f"{animal.get_name()} is an old cat because it is more than {animal.aged()} years old.")