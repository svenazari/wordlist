#WORDLIST.py
#by: SvenAzari
#potrebni programi: python3

#datoteka iz koje radi popis riječi mora imati naziv "input.txt" i mora se nalaziti u istoj mapi kao i skripta
#popis riječi će biti spremljen u datoteku naziva "wordlist.txt"

#imports

#funkcija
def wordlist (): #definiranje fukcije

  odlomci = [] #lista po podlomcima (nakon "splitlines")
  bez = [] #pomoćna lista za bezinterpunkcije
  bezinterpunkcije = [] #razdvajanje po interpunkciji
  bezraz = [] #pomoćna lista za bezrazmak
  bezrazmak = [] #micanje razmaka
  abecedno = [] #riječi po abecednom redu
  bezduplih = [] #bez dublih unosa
  bezbrojeva = [] #lista sa izbačenim brojevima
  final = [] #finalna lista
  
  try:
    with open("input.txt") as file: #otvori input.txt
      odlomci = file.read().splitlines() #razdvoji na mjestima gdje je pritisnut enter (po odlomcima)

    print("Molim pričekati.")

    cpog = len(odlomci) #broj članova u listi poglavalja
    for x in range (0, cpog): #micanje interpunkcijskih i ostalih znakova
      a = odlomci[x]
      b = a.replace('/', ', ').replace('.', ', ').replace(',', ', ').replace('. ', ', ').replace('? ', ', ').replace('?', ', ').replace('! ', ', ').replace('!', ', ').replace('; ', ', ').replace(': ', ', ').replace('- ', ', ').replace(':', ', ').replace('(', ', ').replace(')', ', ').replace('"', ', ').replace('-', ', ').replace('–', ', ').replace('[', ', ').replace(']', ', ').replace('\ufeff', ', ').replace('*', ', ').replace('“', ', ').replace('„', ', ').replace("”", ", ").replace("—", ", ").replace("|", ", ").replace("”", ", ") #zamijeni sve što se treba izbaciti sa ", "
      bez = b.split(', ') #izbaci ", "
      bezinterpunkcije.extend(bez) #dodaj u listu bezinterpunkcije

    cbi = len(bezinterpunkcije) #broj članova u listi bezinterpunkcije
    for x in range (0, cbi): #razdvajanje po razmacija
      a = bezinterpunkcije[x]
      bezraz = a.split (" ") #razdvoji unose u listi na razmacima
      bezrazmak.extend(bezraz) #dodaj u listu bezrazmak

    abecedno = sorted(bezrazmak)
    while("" in abecedno): #očisti poglavalja od praznih redova
      abecedno.remove("")
 
    bezduplih = list(dict.fromkeys(abecedno)) #micanje duplih unosa

    bezbrojeva = [x for x in bezduplih if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())] #micanje brojeva

    final = map(lambda x:x.lower(), bezbrojeva) #sve riječi napisane malim slovima (jer ako neka počinje sa velikim slovima, Ž bude ispred a - probati naći rješenje)
    
    brojrijeci = len(bezbrojeva)

    with open("wordlist.txt", "w+") as wl: #otvori wordlist.txt datoteku
      for item in final:
        wl.write(item)
        wl.write('\n')

    print ("\033[A                             \033[A") #izbriši zadnji red teksta
    print ("ZAVRŠENO!" + '\n' + "Ukupno izdvojeno " + str(brojrijeci) + " različitih riječi." + '\n' + "Popis riječi je spremljen u datoteku wordlist.txt") #obavijesti da je proces završen i koliko je različitih riječi izdvojeno

    #print (final) #ispis

  except FileNotFoundError: #u slučaju da nedostaje datoteka input.txt
    print ("GREŠKA: Nedostaje datoteka input.txt!" + '\n' + "Stvorite datoteku input.txt u nju kopirajte tekst iz kojeg želite napraviti popis riječi")

wordlist () #pozovi funkciju
