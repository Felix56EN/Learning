class Animal:
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        return "Гав!"

class Cat(Animal):
    def voice(self):
        return "Мяу!"

class Cow(Animal):
    def voice(self):
        return "Муууу!"

polkan = Dog()
murka = Cat()
burenka = Cow()

print("Собака Полкан говорит:", polkan.voice())
print("Кошка Мурка говорит:", murka.voice())
print("Корова Буренка говорит:", burenka.voice())