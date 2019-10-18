def pozdrav(ime, priimek):
    print("Pozdravljeni, " + ime + " " + priimek)

pozdrav("Miha", "Novak")
pozdrav("Mojca", "Kovač")
pozdrav("Janko", "Novak")


def obseg_kroga(polmer):
    pi = 3.1415926535
    obseg = 2 * pi * polmer
    return obseg

obseg5 = obseg_kroga(5)
print("Obseg kroga s polmerom 5 je " + str(obseg5))
