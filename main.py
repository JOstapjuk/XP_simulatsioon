import random
import datetime

uudiste_andmed = {
    "Tehnoloogia": [
        "Uus tehisintellekti mudel ületab ootusi.",
        "Eestis avati järjekordne andmekeskus.",
        "Nutitelefonide müük kasvas rekordtasemele."
    ],
    "Spordiuudised": [
        "Eesti jalgpallikoondis võitis sõpruskohtumise.",
        "Kergejõustiku EM-il püstitati uus rekord.",
        "Korvpalliliiga finaal pakkus põnevust lõpuni."
    ],
    "Majandus": [
        "Inflatsioon langes oodatust kiiremini.",
        "Uus idufirma kogus miljon eurot investeeringuid.",
        "Töötuse määr püsib madalana."
    ]
}

def juhuslik_kuupaev():
    tana = datetime.date.today()
    paevad_tagasi = random.randint(0, 6)
    return tana - datetime.timedelta(days=paevad_tagasi)

def genereeri_uudised(kategooria):
    uudised = random.sample(uudiste_andmed[kategooria], k=2)
    return [(uudis, juhuslik_kuupaev()) for uudis in uudised]

def vali_kategooria():
    print("\nVali kategooria:")
    valikud = list(uudiste_andmed.keys())
    for i, kategooria in enumerate(valikud, 1):
        print(f"{i}. {kategooria}")
    valik = int(input("Sisesta valiku number: "))
    return valikud[valik - 1]

def lisa_uudis(kategooria):
    uus_uudis = input("Sisesta uus uudis: ")
    uudiste_andmed[kategooria].append(uus_uudis)
    print("Uudis lisatud.")

def pea_programm():
    while True:
        kategooria = vali_kategooria()
        uudised = genereeri_uudised(kategooria)

        print(f"\nGenereeritud uudised kategooriast '{kategooria}':")
        for uudis, kuup in uudised:
            print(f"{kuup} - {uudis}")

        lisa = input("\nKas soovid lisada uue uudise? (jah/ei): ").lower()
        if lisa == "jah":
            lisa_uudis(kategooria)

        uuesti = input("\nKas soovid uudised uuesti genereerida? (jah/ei): ").lower()
        if uuesti != "jah":
            print("Aitäh kasutamast uudistegeneraatorit!")
            break

pea_programm()
