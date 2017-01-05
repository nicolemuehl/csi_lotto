# -*- coding: utf-8 -*-

haare = {"schwarz":"CCAGCAATCGC", "braun":"GCCAGTGCCG", "blond":"TTAGCTATCGC"}
gesicht = {"eckig":"GCCACGG", "rund":"ACCACAA", "oval":"AGGCCTCA"}
augen = {"blau":"TTGTGGTGGC", "grün":"GGGAGGTGGC", "braun":"AAGTAGTGAC"}
geschlecht = {"weiblich":"TGAAGGACCTTC", "männlich":"TGCAGGAACTTC"}
haut = {"weiß":"AAAACCTCA", "schwarz":"CGACTACAG", "asiatisch":"CGCGGGCCG"}

eva = {"haare":"blond", "gesicht":"oval", "augen":"blau", "geschlecht":"weiblich", "haut":"weiß"}
larisa = {"haare":"braun", "gesicht":"oval", "augen":"braun", "geschlecht":"weiblich", "haut":"weiß"}
matej = {"haare":"schwarz", "gesicht":"oval", "augen":"blau", "geschlecht":"männlich", "haut":"weiß"}
miha = {"haare":"braun", "gesicht":"eckig", "augen":"grün", "geschlecht":"männlich", "haut":"weiß"}

print "Das ganze Eis wurde aufgegessen!!! \n...alles weg... \n...wie schrecklich... \n\n!!!Ruft die CSI(Crime on Stolen Icecreams)!!!"
antwort = raw_input("\nSollen wir die CSI rufen? j/n\n")

if antwort == "j":
    dna = open("csi_dna.txt").read()
    print "\nDie CSI hat ermittelt und folgende DNA gefunden:\n" + dna + "\n\nAuf Grundlage dieser DNA hat der/die Verdächtige folgende Merkmale:"

    merkmale = {}

    if geschlecht["weiblich"] in dna:
        print "- Geschlecht: Weiblich -"
        merkmale["geschlecht"] = "weiblich"
    elif geschlecht["männlich"] in dna:
        print "- Geschlecht: Männlich -"
        merkmale["geschlecht"] = "männlich"

    if haut["weiß"] in dna:
        print "- Hautfarbe: Weiß -"
        merkmale["haut"] = "weiß"
    elif haut["schwarz"] in dna:
        print "- Hautfarbe: Schwarz -"
        merkmale["haut"] = "schwarz"
    elif haut["asiatisch"] in dna:
        print "- Hautfarbe: Asiatisch -"
        merkmale["haut"] = "asiatisch"

    if augen["blau"] in dna:
        print "- Augenfarbe: Blau -"
        merkmale["augen"] = "blau"
    elif augen["grün"] in dna:
        print "- Augenfarbe: Grün -"
        merkmale["augen"] = "grün"
    elif augen["braun"] in dna:
        print "- Augenfarbe: Braun -"
        merkmale["augen"] = "braun"

    if haare["schwarz"] in dna:
        print "- Haarfarbe: Schwarz -"
        merkmale["haare"] = "schwarz"
    elif haare["braun"] in dna:
        print "- Haarfarbe: Braun -"
        merkmale["haare"] = "braun"
    elif haare["blond"] in dna:
        print "- Haarfarbe: Blond -"
        merkmale["haare"] = "blond"

    if gesicht["eckig"] in dna:
        print "- Gesichtsform: Eckig -"
        merkmale["gesicht"] = "eckig"
    elif gesicht["rund"] in dna:
        print "- Gesichtsform: Rund -"
        merkmale["gesicht"] = "rund"
    elif gesicht["oval"] in dna:
        print "- Gesichtsform: Oval -"
        merkmale["gesicht"] = "oval"

#ich war irgendwie zu blöd, das ganze obige verkürzt in eine funktionierende for schleife zu bringen

    print "\nDas Eis wurde auf grausame Weise verspeist von:"

    if merkmale == eva:
        print "...Eva..."
    elif merkmale == larisa:
        print "...Larisa..."
    elif merkmale == matej:
        print "...Matej..."
    elif merkmale == miha:
        print "...Miha..."

    print "\nJetzt können wieder alle ruhig schlafen. Die Frage ist, wie lange..."

elif antwort == "n":
    print "\nNa gut, wenn du es nicht wissen willst... \nDann wird auch dein Eis bald gegessen werden... \nSüße Träume!!!"

else:
    print "\n!!!Falsche Entscheidung!!! \nDa du die Suche nach dem/der Verdächtigen nicht ernst nimmst, kann dein Eis auch niemand retten..."


