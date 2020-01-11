
import statistics

#słowniki do przechowywania danych
slownikZPodzialemNaKlasy = {}
slownikAtrybuty = {}

#wczytanie danych z plikow txt
plikDiabetes = open("diabetes.txt", "r")
plikDiabetesType = open("diabetes-type.txt", "r")

indeksyZSlownikAtrybuty = []


for liniaZplikuTxt in plikDiabetesType:
    wczytaniaLiniaDoZapisaniaWSlowniku = liniaZplikuTxt
    wczytaniaLiniaDoZapisaniaWSlowniku = wczytaniaLiniaDoZapisaniaWSlowniku.strip()
    wczytaniaLiniaDoZapisaniaWSlowniku = wczytaniaLiniaDoZapisaniaWSlowniku.split(" ")
    slownikAtrybuty[wczytaniaLiniaDoZapisaniaWSlowniku[0]] = wczytaniaLiniaDoZapisaniaWSlowniku[1]

licz = 0
diabetesType1 = "n"

for kluczZeSlownika in slownikAtrybuty:
    if slownikAtrybuty[kluczZeSlownika] == diabetesType1:
        indeksyZSlownikAtrybuty.append(licz)
    licz = licz + 1

for liniaZPlikuTxt in plikDiabetes:
    wczytaniaLiniaDoZapisaniaWSlowniku = liniaZPlikuTxt
    wczytaniaLiniaDoZapisaniaWSlowniku = wczytaniaLiniaDoZapisaniaWSlowniku.strip()
    wczytaniaLiniaDoZapisaniaWSlowniku = wczytaniaLiniaDoZapisaniaWSlowniku.split(" ")

    listaKopiujLinie = []
    tmp = 0
    for item in wczytaniaLiniaDoZapisaniaWSlowniku:
        if tmp in indeksyZSlownikAtrybuty:
            listaKopiujLinie.append(float(item))
        else:
            listaKopiujLinie.append(item)
        tmp += 1
    wczytaniaLiniaDoZapisaniaWSlowniku = listaKopiujLinie

    if wczytaniaLiniaDoZapisaniaWSlowniku[-1] in slownikZPodzialemNaKlasy:
        slownikZPodzialemNaKlasy[wczytaniaLiniaDoZapisaniaWSlowniku[-1]] = slownikZPodzialemNaKlasy.get(wczytaniaLiniaDoZapisaniaWSlowniku[-1]) + [wczytaniaLiniaDoZapisaniaWSlowniku]
    else:
        slownikZPodzialemNaKlasy[wczytaniaLiniaDoZapisaniaWSlowniku[-1]] = [wczytaniaLiniaDoZapisaniaWSlowniku]


print(" Istniejące w systemie klasy decyzyjne:")

for kluczZeSlownikaZPodzialemNaKlasy in slownikZPodzialemNaKlasy:
    print("{}".format(kluczZeSlownikaZPodzialemNaKlasy))

print(" ----------------------------------------")

for kluczZeSlownikaZPodzialemNaKlasy in slownikZPodzialemNaKlasy:
    print("Klasa decyzyjna - {} - liczba obiektów w klasie: {}".format(kluczZeSlownikaZPodzialemNaKlasy, len(slownikZPodzialemNaKlasy[kluczZeSlownikaZPodzialemNaKlasy])))

print(" ----------------------------------------")


def unikalny(atrybut, lista):
    listaUnikalna = []
    for i in lista:
        if i not in listaUnikalna:
            listaUnikalna.append(i)
    print("Atrybut {} ma : {} unikalnych wartości ".format(atrybut, len(listaUnikalna)))
    print("Lista unikalnych wartości atrybutu {}".format(atrybut))

    print(listaUnikalna)
    
for index in indeksyZSlownikAtrybuty:
    listaAtrybutow = []
    listaAtrybutowPoKluczach = {}

    for kluczSlownikZPodzialem in slownikZPodzialemNaKlasy:
        listPom = []
        for wartosc in slownikZPodzialemNaKlasy[kluczSlownikZPodzialem]:
            listaAtrybutow.append(wartosc[index])
            listPom.append(wartosc[index])

        listaAtrybutowPoKluczach[kluczSlownikZPodzialem] = listPom

        print("{}".format("a{}".format(str(index + 1))))
        print("Max listy - {}".format(max(listaAtrybutow)))
        print("Min listy - {}".format(min(listaAtrybutow)))

        unikalny("a{}".format(index + 1), listaAtrybutow)
        print("Odchylenie standardowe atrybutu {}, wynosi: {}".format(index + 1, statistics.stdev(listaAtrybutow)))
        for kluczWListaPoKluczach in listaAtrybutowPoKluczach:
           print("Odchylenie standardowe atrybutu {} w klasie decyzyjnej {}, wynosi: {}".format(index + 1, kluczWListaPoKluczach,statistics.stdev(listaAtrybutowPoKluczach[kluczWListaPoKluczach])))
