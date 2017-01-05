# -*- coding: utf-8 -*-

import random

print "Willkommen beim Nummerngenerator der Alpenländischen Lotterien!"

def main():
    lotteriezahlen = []
    eingabe = int(raw_input("\nWieviele Zahlen(von 1 bis 10) soll die Lotterie denn ausgeben?\n"))

    if eingabe < 1 or eingabe > 10:
        print "Keine Augen oder was? Welchen Teil von 1-10 hast du nicht verstanden?"
    elif eingabe > 1 and eingabe < 10:
        for zahl in range(0, eingabe):
            zufall = random.randint(1, 101)
            lotteriezahlen.append(zufall)
            lotteriezahlen.sort()
        print "\nDeine Lottozahlen sind:\n%s" % str(lotteriezahlen)[1:-1] + "\nViel Glück damit!"

if __name__ == "__main__":
    main()
