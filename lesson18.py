# my_addition_skills = {1: "fire", 2: "water"}
#
# user_choice = 1
#
# type_weapon = my_addition_skills[user_choice]

class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self._health = 100
        self._strength = 1
        self._agility = 1
        self._intelligence = 1
        self._base_skill = 1

    def increase_base_skill(self):
        if self._base_skill <= 10:
            self._base_skill += 1

    @property
    def agility(self):
        return self._agility

    @property
    def strength(self):
        return self._strength


class Archer(Unit):
    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon

    @property
    def agility(self):
        self._agility = self._base_skill
        return self._agility


class Sniper(Unit):
    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon

    @property
    def agility(self):
        self._agility = self._base_skill
        return self._agility

legolas = Archer("Legolas", "Elfs", "Bow")
print(legolas.agility)
print(legolas.strength)
legolas.increase_base_skill()
legolas.increase_base_skill()
legolas.increase_base_skill()
print(">>", legolas.strength)
print(legolas.agility)