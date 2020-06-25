class Animal:
    total_weight = 0
    heaviest_animal = None

    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice
        Animal.total_weight = 0
        Animal.heaviest_animal = None

    def feed(self):
        print(f"{self.name}")

    def voice(self):
        print(f"{self.name}, говорит {self.voice}")

    def product(self):
        pass

class Bird(Animal):
    def egg(self):
        print(f"яйца от птицы по имени {self.name}")

    def product(self):
        self.egg()

class Chicken(Bird):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

class Goose(Bird):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

class Duck(Bird):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

class Milk(Animal):
    def milk(self):
        print(f"молоко от животного по имени {self.name}")

    def product(self):
        self.milk()

class Cow(Milk):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

class Goat(Milk):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

class Sheep(Animal):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def wool(self):
        print(f"шерсть от овцы по имени {self.name}")

    def product(self):
        self.wool()

cow = Cow("Манька", "450", "муууу")
sheep1 = Sheep("Барашек", "100", "бэээээ")
sheep2 = Sheep("Кудрявая", "80", "бэээээ")
goat1 = Goat("Рога", "50", "меееее")
goat2 = Goat("Копыта", "55", "меееее")
goose1 = Goose("Серый", "3", "ээге-гей!")
goose2 = Goose("Белый", "4", "ээге-гей!")
chicken1 = Chicken("Ko-Ko", "2", "ко-ко-ко")
chicken2 = Chicken("Кукареку", "2", "ко-ко-ко")
duck = Duck("Кряква", "3", "кря-кря")

animals = [cow, sheep1, sheep2, goat1, goat2, goose1, goose2, chicken1, chicken2, duck]

print("Животные которых нужно кормить:")
for animal in animals:
    animal.feed()

print("Продукты от животных:")
for animal in animals:
    animal.product()

print("Голоса животных:")
for animal in animals:
    print(f"{animal.name} говорит {animal.voice}")

for animal in animals:
    if Animal.heaviest_animal is None:
        Animal.heaviest_animal = animal
        print(f"Самое тяжелое животное {animal.name}, весит {animal.weight} кг.")
