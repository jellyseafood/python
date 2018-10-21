import random
import sys

# pie00
# pie01
# pie02
# pie03

print("USE EXISTING DATA? Y/N")

truope = 0

while truope == 0:
    prev = input()

    if prev == "Y":
        pie00 = open("hero01name.tt", "r")
        pie01 = open("hero01kill.tt", "r")
        pie02 = open("hero01pots.tt", "r")
        pie03 = open("hero01hp.tt", "r")
        truope = 1

    if prev == "N":

        pie00 = open("hero01name.tt", "w+")
        pie01 = open("hero01kill.tt", "w+")
        pie02 = open("hero01pots.tt", "w+")
        pie03 = open("hero01hp.tt", "w+")
        truope = 1

    if prev != "Y" and prev != "N":
        print("INVALID INPUT, TRY AGAIN")






class Hero:
    def __init__(self, hp, pots, kills, name):
        self.hp = hp
        self.pots = pots
        self.kills = kills
        self.name = name

        pie00.write(name)
        pie01.write(str(kills))
        pie02.write(str(pots))
        pie03.write(str(hp))

        pie00.close()
        pie01.close()
        pie02.close()
        pie03.close()

    def finalwrite(self, hp01, pots01, kills01, name01):

        pie00 = open("hero01name.tt", "w+")
        pie01 = open("hero01kill.tt", "w+")
        pie02 = open("hero01pots.tt", "w+")
        pie03 = open("hero01hp.tt", "w+")

        pie00.write(name01)
        pie01.write(str(kills01))
        pie02.write(str(pots01))
        pie03.write(str(hp01))

    def finalread(self):
        pie00 = open("hero01name.tt", "r")
        pie01 = open("hero01kill.tt", "r")
        pie02 = open("hero01pots.tt", "r")
        pie03 = open("hero01hp.tt", "r")

        print("NAME: ")
        print(pie00.read())
        print("KILLS: ")
        print(pie01.read())
        print("POTS: ")
        print(pie02.read())
        print("HP: ")
        print(pie03.read())


    # def confirmkill(self, killdc):
    #
    #     self.kills += 1





def hero_attack(boiz):
    if cdict01[boiz] > 0:
        cdict01[boiz] -= 1
    else:
        hero01.kills += 1
        cdict01.pop(boiz)
        boiz -= 1
        cdict01[boiz] -= 1
    return boiz
    # if cdict01[0] == 0:
    #     wine = 1
    #     return wine
    #     combat01 = 1
    print(cdict01)

def hero_heal(pots):
    if pots - 1 >= 0:
        hero01.hp += 3
        hero01.pots -= 1
    else:
        print("YOU HAVE NOTHING")
    while hero01.hp > hp_max:
        hero01.hp -= 1

def hero_run():
    combat01 = 1
    print("YOU RAN AWAY! YOU COWARD! YOU FOOL!")

def enem_attack():
    hero01.hp -= random.randint(0,2)

if prev == "N":
    print("INPUT NAME")
    nam = input()
    hero01 = Hero(15, 7, 0, nam)

if prev == "Y":
    pie00 = open("hero01name.tt", "r")
    pie01 = open("hero01kill.tt", "r")
    pie02 = open("hero01pots.tt", "r")
    pie03 = open("hero01hp.tt", "r")

    oldname01 = pie00.read()
    oldkills01 = int(pie01.read())
    oldpots01 = int(pie02.read())
    oldhp01 = int(pie03.read())

    pie00.close()
    pie01.close()
    pie02.close()
    pie03.close()

    pie00 = open("hero01name.tt", "w+")
    pie01 = open("hero01kill.tt", "w+")
    pie02 = open("hero01pots.tt", "w+")
    pie03 = open("hero01hp.tt", "w+")



    hero01 = Hero(oldhp01, oldpots01, oldkills01, oldname01)

hero01.finalread()

cdict01 = {}
b = 0
print("INPUT NUMBER OF ENEMIES:")
while True:
    try:
        a = int(input())
        break
    except ValueError:
        print("INVALID NUMBER, TRY AGAIN.")

while b < a:
    cdict01[b] = 2
    b += 1



print(cdict01)
hp_max = hero01.hp
pots = hero01.pots
combat01 = 0
wine = combat01

bg = b - 1
# print(bg)

if a == 0:
    combat01 = 2

while combat01 == 0 and hero01.hp > 0:
    print("1 to attack, 2 to use a potion, 3 to flee")

    while True:
        try:
            optio = int(input())
            break
        except ValueError:
            print("INVALID ACTION, TRY AGAIN")
    if optio == 1:
        bg = hero_attack(bg)
    if optio == 2:
        hero_heal(hero01.pots)
    if optio == 3:
        hero_run()

    if cdict01[0] == 0:
        combat01 = 1
        break
    if hero01.hp == 0:
        print("YOU DIED")
        break

    for x in cdict01:
        enem_attack()
    print("YOUR HP")
    print(hero01.hp)
    print("ENEMY HP")
    print(cdict01)


if combat01 == 1:
    hero01.kills += 1
    print("YOU WON!")

if combat01 == 2:
    print("YOU WON WITHOUT EVEN FIGHTING! SUN TZU WOULD BE PROUD!")

hero01.finalwrite(hero01.hp, hero01.pots, hero01.kills, hero01.name)
hero01.finalread()


