class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def __repr__(self):
        return f"({self.name}, {self.age})"


person_1 = Person("John", 23, "programmer")
print(person_1)

person_2 = Person("Jane", 36)
print(person_2)

persons = [person_1, person_2]
print(persons)
