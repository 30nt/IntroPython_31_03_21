class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def __repr__(self):
        return f"({self.name}, {self.age})"


class Ranger(Person):
    def __init__(self, name, age, job, atribut):
        super().__init__(name, age, job)  # init родителя
        self.atr = atribut

    def __str__(self):
        ranger_str = super().__str__() + f", atr: {self.atr}"
        return ranger_str

person_1 = Person("John", 23, "programmer")
print(person_1)

chuck_norris = Ranger("Chuck", 1000, "ranger", "star")
print(chuck_norris)