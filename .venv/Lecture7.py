class Animal:
    count = 0
    def voice(self):
        pass
    def __init__(self):
        Animal.count = Animal.count + 1
    def inst_count():
        print(Animal.count)
    inst_count = staticmethod(inst_count)


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
Animal.inst_count()
