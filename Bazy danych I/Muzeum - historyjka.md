### Odbiorca:

**Muzeum - jego zarząd**

### Założenia:

- Muzeum jest w jednym budynku
- Budynek jest podzielony na piętra 
- Piętra są podzielone na obszary (kategorie)
- W muzeum pracują pracownicy
- Pracownicy mają przypisane dane, takie jak adres
- Pracownicy są przypisani do stanowiska
- Pracownicy posiadający niektóre stanowiska są przypisani do konkretnej częsci muzeum (np. ochroniarz lub osoba specjalizująca się w danej dziedzinie malarstwa)
- Dodatkowo jedno piętro jest zarezerwowane na wystawy czasowe, które zmieniają się co jakiś czas
- Na piętrach (i w obszarach) powieszone są obrazy
- Każdy obraz ma autora, wymiar, technikę wykonania, datę wykonania, datę dotarcia do muzeum, kolorystykę i nurt
- pod jednym adresem może mieszkać wielu pracowników (np. mąż i żona)
- Obrazy nie są wypożyczane, więc jeśli obraz należy do muzeum (obszaru) to nie należy do wystywy (nie może też należeć do 2 wystaw)

### Detale: 

- Obraz może mieć nieznanego autora, dlatego imie i nazwisko jest "nullable", lecz połączenie z autorem musi istnieć (możemy np. wiedzieć, że 2 obrazy są namalowane przez jednego autora, ale nie znamy jego tożsamości)
- Identyczna sytuacja z datą
- jesli ktos mieszka w domu nie ma numeru mieszkania
- wystawa zajmuje jedno całe piętro (tak powiedział dyrektor muzeum)
- wiele wystaw moze mieć bilet o takiej samej cenie
- obraz należy albo do wystawy albo do obszaru, dlatego "O" w relacjach 
- obszar może nie mieć obrazów w przypadku gdy jest np. modernizowany (obszar nie ob)
- może nie być w tym muzeum obrazu o danym nurcie (wszystkie nurty są w bazie danych, na tyle na ile to możliwe {przynajmniej te popularne})
- każdy rozmiar jest przypisany do jakiegoś obrazu (dany rozmiar tworzymy dopiero gdy muzem posiada obraz o takim rozmiarze)
- kolorystykę również tworzymy dopiero gdy istnieje obraz z daną kolorystyką
- nie ma pustych wystaw (nie jest to wówczas wystawa)
- wysokosc i szerokosc w mm, dlatego int a nie float (prostota)
- stanowisko może być "puste" gdy np. ktoś się zwolnił i jeszcze nie znaleziono zastępstwa
- każdy atrybut obrazu (data wykonania, autor itp. jest jeden do wielu ponieważ jeden autor mógł namalować więcej niż jeden obraz...)
- więcej niż jeden pracownik może pracować na danym stanowisku (np. 15 ochoroniarzy)
- wystawa może być w muzem np. dwa razy do roku, dlatego wiele terminow dla jednej wystawy
- tylko jedna wystawa mieści się w muzeum, nie może być 2-ch w tym samym czasie
- pusty obszar nie musi miec przypisanego pracownika

### Detale techniczne:
- date -> datetime
- bit -> bool

### Opis niektórych (mniej jasnych) kolumn:

- data_otrzymania_data_ot: data od której muzeum jest w posiadaniu danego obrazu
- kolorystyka_typ: typ kolorow (np. pastele)
- kolorystyka_nastoj: (np. jasne lub zimne)
- bilet_potrzebny: czy obowiązuje dodatkowa opłata za zobaczenie wystawy
- technika_nazwa: np. oleje na płótnie
- obraz_stan: % stan obrazu (czy się rozpada czy nie) (według mnie nie ma sensu tworzyć osobnej encji na to)
- obraz_opis: krótka notatka o tym co znajduje się na obrazie (np. "dostojnie ubrany mężczyzna spoglądający z urwiska skalnego na mgłę znajdującą się pod nim" -> Wanderer above the Sea of Fog)