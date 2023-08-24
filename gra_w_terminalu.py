from random import randint
class Player:
    def __init__(self, name, age , str, per, endurance, charisma, intel, luck, magic, skills):
        self.name = name
        self.age = age
        self.strength = str
        self.perception = per
        self.endurance = endurance
        self.charisma = charisma
        self.inteligence = intel
        self.luck = luck
        self.magic_talent = magic
        self.health = 20+1*endurance
        self.skills=skills
    def __repr__(self):
        return "{} is {} old. Has {} strength, {} perception, {} endurance. {} charisma, {} inteligence, {} luck, {} magic and {} health".format(self.name, self.age, self.strength, self.perception, self.endurance, self.charisma, self.inteligence, self.luck, self.magic_talent, self.health)




print("Hello in game")
num_players = input("How many people will play?(insert number like 2)")
while num_players.isdigit() == False:
    num_players = input("Wrong! Please insert number")
gracze = []
def losowanie_postaci(imie):
    return Player(imie, randint(18, 70), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#print(losowanie_postaci("Elrich"))
for x in range(int(num_players)):
    z = input("What will be name of your character player {}".format(x+1))
    gracze.append(losowanie_postaci(z))
for x in range(int(num_players)):
    print("Player {} will play {}".format(x+1, gracze[x].name))
    print(gracze[x])

