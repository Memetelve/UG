DROP TABLE IF EXISTS obraz;
DROP TABLE IF EXISTS pracownik;
DROP TABLE IF EXISTS obszar;
DROP TABLE IF EXISTS termin;
DROP TABLE IF EXISTS wystawa;
DROP TABLE IF EXISTS pietro;
DROP TABLE IF EXISTS adres;
DROP TABLE IF EXISTS stanowisko;
DROP TABLE IF EXISTS autor;
DROP TABLE IF EXISTS kolorystyka;
DROP TABLE IF EXISTS technika;
DROP TABLE IF EXISTS nurt;
DROP TABLE IF EXISTS wymiar;


CREATE TABLE wymiar (
    id_wymiar INT PRIMARY KEY IDENTITY,
    szerokosc INT CHECK (szerokosc > 0),
    wysokosc INT CHECK (wysokosc > 0),
);

CREATE TABLE nurt (
    id_nurt INT PRIMARY KEY IDENTITY,
    nazwa_nurt VARCHAR(100) NOT NULL,
);

CREATE TABLE technika (
    id_technika INT PRIMARY KEY IDENTITY,
    nazwa_technika VARCHAR(100) NOT NULL,
);

CREATE TABLE kolorystyka (
    id_kolorystyka INT PRIMARY KEY IDENTITY,
    typ VARCHAR(255) NOT NULL,
    nastoj VARCHAR(255) NOT NULL,
);

CREATE TABLE autor (
    id_autor INT PRIMARY KEY IDENTITY,
    imie VARCHAR(255),
    nazwisko VARCHAR(255),
    data_urodzenia DATE,
    data_smierci DATE,
);

CREATE TABLE stanowisko (
    id_stanowisko INT PRIMARY KEY IDENTITY,
    nazwa_stanowisko VARCHAR(50) NOT NULL,
);

CREATE TABLE adres (
    id_adres INT PRIMARY KEY IDENTITY,
    miasto VARCHAR(100) NOT NULL CHECK (LEN(miasto) > 2),
    wojewodztwo VARCHAR(50) NOT NULL CHECK (LEN(wojewodztwo) > 5),
    ulica VARCHAR(255) NOT NULL CHECK (ulica <> ''),
    budynek VARCHAR(10) NOT NULL,
    mieszkanie INT CHECK (mieszkanie > 0),
);

CREATE TABLE pietro (
    id_pietro INT PRIMARY KEY IDENTITY,
    pietro_liczba INT NOT NULL,
);

CREATE TABLE wystawa (
    id_wystawa INT PRIMARY KEY IDENTITY,
    nazwa_wystawa VARCHAR(255) NOT NULL CHECK (nazwa_wystawa <> ''),
    opis_wystawa VARCHAR(1000) NOT NULL CHECK (opis_wystawa <> ''),
    id_pietro INT FOREIGN KEY REFERENCES pietro(id_pietro),
);

CREATE TABLE termin (
    id_termin INT PRIMARY KEY IDENTITY,
    data_rozpoczecia DATETIME NOT NULL,
    data_zakonczenia DATETIME NOT NULL,
    id_wystawa INT FOREIGN KEY REFERENCES wystawa(id_wystawa),
);

CREATE TABLE obszar (
    id_obszar INT PRIMARY KEY IDENTITY,
    nazwa_obszar VARCHAR(50) NOT NULL CHECK (nazwa_obszar <> ''),
    opis_obszar VARCHAR(255) NOT NULL CHECK (opis_obszar <> ''),
    id_piętro INT FOREIGN KEY REFERENCES pietro(id_pietro),
);

CREATE TABLE pracownik (
    id_pracownik INT PRIMARY KEY IDENTITY,
    imie VARCHAR(25) NOT NULL,
    nazwisko VARCHAR(50) NOT NULL,
    pesel VARCHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    nr_tel VARCHAR(12) NOT NULL UNIQUE,
    pensja DECIMAL(10,2) DEFAULT 0.00,
    id_stanowisko INT FOREIGN KEY REFERENCES stanowisko(id_stanowisko),
    id_obszar INT FOREIGN KEY REFERENCES obszar(id_obszar),
    id_adres INT FOREIGN KEY REFERENCES adres(id_adres),
);

CREATE TABLE obraz (
    id_obraz INT PRIMARY KEY IDENTITY,
    nazwa VARCHAR(255) NOT NULL,
    stan INT NOT NULL CHECK (stan > 0),
    data_wykonania DATE,
    data_otrzymania DATE NOT NULL,
    id_wymiar INT FOREIGN KEY REFERENCES wymiar(id_wymiar),
    id_nurt INT FOREIGN KEY REFERENCES nurt(id_nurt),
    id_technika INT FOREIGN KEY REFERENCES technika(id_technika),
    id_kolorystyka INT FOREIGN KEY REFERENCES kolorystyka(id_kolorystyka),
    id_autor INT FOREIGN KEY REFERENCES autor(id_autor),
    id_wystawa INT FOREIGN KEY REFERENCES wystawa(id_wystawa),
    id_obszar INT FOREIGN KEY REFERENCES obszar(id_obszar),
);

-- Tabela wymiar
INSERT INTO wymiar (szerokosc, wysokosc) VALUES (100, 200);
INSERT INTO wymiar (szerokosc, wysokosc) VALUES (300, 400);
INSERT INTO wymiar (szerokosc, wysokosc) VALUES (500, 600);
INSERT INTO wymiar (szerokosc, wysokosc) VALUES (700, 800);
INSERT INTO wymiar (szerokosc, wysokosc) VALUES (900, 1000);

-- Tabela nurt
INSERT INTO nurt (nazwa_nurt) VALUES ('abstrakcja');
INSERT INTO nurt (nazwa_nurt) VALUES ('realizm');
INSERT INTO nurt (nazwa_nurt) VALUES ('impresjonizm');
INSERT INTO nurt (nazwa_nurt) VALUES ('ekspresjonizm');
INSERT INTO nurt (nazwa_nurt) VALUES ('surrealizm');

-- Tabela technika
INSERT INTO technika (nazwa_technika) VALUES ('olej');
INSERT INTO technika (nazwa_technika) VALUES ('akryl');
INSERT INTO technika (nazwa_technika) VALUES ('węgiel');
INSERT INTO technika (nazwa_technika) VALUES ('akwarela');
INSERT INTO technika (nazwa_technika) VALUES ('gwasz');

-- Tabela kolorystyka
INSERT INTO kolorystyka (typ, nastoj) VALUES ('monochromatyczna', 'spokojna');
INSERT INTO kolorystyka (typ, nastoj) VALUES ('kontrastowa', 'dynamiczna');
INSERT INTO kolorystyka (typ, nastoj) VALUES ('chromatyczna', 'energetyczna');
INSERT INTO kolorystyka (typ, nastoj) VALUES ('tonalna', 'nastrojowa');
INSERT INTO kolorystyka (typ, nastoj) VALUES ('kolorowa', 'radosna');

-- Tabela autor
INSERT INTO autor (imie, nazwisko, data_urodzenia, data_smierci) VALUES (NULL, NULL, NULL, NULL);
INSERT INTO autor (imie, nazwisko, data_urodzenia, data_smierci) VALUES ('Anna', 'Nowak', '1985-01-01', '2025-01-01');
INSERT INTO autor (imie, nazwisko, data_urodzenia, data_smierci) VALUES ('Tomasz', 'Wiśniewski', '1990-01-01', '2030-01-01');
INSERT INTO autor (imie, nazwisko, data_urodzenia, data_smierci) VALUES ('Katarzyna', 'Wójcik', '1995-01-01', '2035-01-01');
INSERT INTO autor (imie, nazwisko, data_urodzenia, data_smierci) VALUES ('Piotr', 'Kowalczyk', '2000-01-01', '2040-01-01');

-- Tabela stanowisko
INSERT INTO stanowisko (nazwa_stanowisko) VALUES ('dyrektor');
INSERT INTO stanowisko (nazwa_stanowisko) VALUES ('kurator');
INSERT INTO stanowisko (nazwa_stanowisko) VALUES ('konserwator');
INSERT INTO stanowisko (nazwa_stanowisko) VALUES ('pracownik techniczny');
INSERT INTO stanowisko (nazwa_stanowisko) VALUES ('ochroniarz');

-- Tabela adres
INSERT INTO adres (miasto, wojewodztwo, ulica, budynek, mieszkanie) VALUES ('Warszawa', 'Mazowieckie', 'Nowowiejska', '4b', '34');
INSERT INTO adres (miasto, wojewodztwo, ulica, budynek, mieszkanie) VALUES ('Kraków', 'Małopolskie', 'Krakowska', '8a', '31');
INSERT INTO adres (miasto, wojewodztwo, ulica, budynek, mieszkanie) VALUES ('Łódź', 'Łódzkie', 'Piotrkowska', 7, '54');
INSERT INTO adres (miasto, wojewodztwo, ulica, budynek, mieszkanie) VALUES ('Wrocław', 'Dolnośląskie', 'Oławska', 4, '11');
INSERT INTO adres (miasto, wojewodztwo, ulica, budynek, mieszkanie) VALUES ('Poznań', 'Wielkopolskie', 'Poznańska', 5, '12');

-- Tabela piętro
INSERT INTO pietro (pietro_liczba) VALUES (0);
INSERT INTO pietro (pietro_liczba) VALUES (1);
INSERT INTO pietro (pietro_liczba) VALUES (2);
INSERT INTO pietro (pietro_liczba) VALUES (3);
INSERT INTO pietro (pietro_liczba) VALUES (4);

-- Tabela wystawa
INSERT INTO wystawa (nazwa_wystawa, opis_wystawa, id_pietro) VALUES ('Wystawa Romantyczna', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ', 5);
INSERT INTO wystawa (nazwa_wystawa, opis_wystawa, id_pietro) VALUES ('Wystawa Neoromantyczna', 'Nulla vel urna eu orci condimentum consectetur sed eu nisl', 5);
INSERT INTO wystawa (nazwa_wystawa, opis_wystawa, id_pietro) VALUES ('Wystawa Abstrakcyjna', 'Phasellus commodo diam vel tempus dignissim.', 5);
INSERT INTO wystawa (nazwa_wystawa, opis_wystawa, id_pietro) VALUES ('Wystawa sztuki współczesnej', 'Morbi sit amet magna id sapien molestie faucibus.', 5);
INSERT INTO wystawa (nazwa_wystawa, opis_wystawa, id_pietro) VALUES ('Wystawa Ekspresjonistyczna', 'Curabitur malesuada mi ut pellentesque pellentesque.', 5);

-- Tabela termin
INSERT INTO termin (data_rozpoczecia, data_zakonczenia, id_wystawa) VALUES ('2022-01-01', '2022-01-31', 1);
INSERT INTO termin (data_rozpoczecia, data_zakonczenia, id_wystawa) VALUES ('2022-02-01', '2022-02-28', 2);
INSERT INTO termin (data_rozpoczecia, data_zakonczenia, id_wystawa) VALUES ('2022-03-01', '2022-03-31', 3);
INSERT INTO termin (data_rozpoczecia, data_zakonczenia, id_wystawa) VALUES ('2022-04-01', '2022-04-30', 4);
INSERT INTO termin (data_rozpoczecia, data_zakonczenia, id_wystawa) VALUES ('2022-05-01', '2022-05-31', 5);

-- Tabela obszar
INSERT INTO obszar (nazwa_obszar, opis_obszar, id_piętro) VALUES ('Obszar 1', 'Pierwszy obszar wystawowy', 1);
INSERT INTO obszar (nazwa_obszar, opis_obszar, id_piętro) VALUES ('Obszar 2', 'Drugi obszar wystawowy', 2);
INSERT INTO obszar (nazwa_obszar, opis_obszar, id_piętro) VALUES ('Obszar 3', 'Trzeci obszar wystawowy', 3);
INSERT INTO obszar (nazwa_obszar, opis_obszar, id_piętro) VALUES ('Obszar 4', 'Czwarty obszar wystawowy', 4);
INSERT INTO obszar (nazwa_obszar, opis_obszar, id_piętro) VALUES ('Obszar 5', 'Piąty obszar wystawowy', 5);

-- Tabela pracownik
INSERT INTO pracownik (id_adres, id_stanowisko, id_obszar, imie, nazwisko, pensja, pesel, email, nr_tel) VALUES (1, 1, 1, 'Jan', 'Kowalski', 5000.0, 123456789, 'a@a.pl', '+48124456789');
INSERT INTO pracownik (id_adres, id_stanowisko, id_obszar, imie, nazwisko, pensja, pesel, email, nr_tel) VALUES (2, 2, 2, 'Anna', 'Nowak', 4000.0, 987654321, 'b@b.pl', '+48123556789');
INSERT INTO pracownik (id_adres, id_stanowisko, id_obszar, imie, nazwisko, pensja, pesel, email, nr_tel) VALUES (3, 3, NULL, 'Jan', 'Nowak', 3000.0, 123435479, 'c@c.pl', '+48123656789');
INSERT INTO pracownik (id_adres, id_stanowisko, id_obszar, imie, nazwisko, pensja, pesel, email, nr_tel) VALUES (4, 4, NULL, 'Marian', 'Kowalski', 2000.0, 987235321, 'd@d.pl', '+48123756789');
INSERT INTO pracownik (id_adres, id_stanowisko, id_obszar, imie, nazwisko, pensja, pesel, email, nr_tel) VALUES (5, 5, 5, 'Marszałkowski', 'Maciej', 1000.0, 126666789, 'e@e.pl', '+48123856789');
-- Tabela obraz
INSERT INTO obraz (nazwa, stan, data_wykonania, data_otrzymania, id_wymiar, id_nurt, id_technika, id_kolorystyka, id_autor, id_wystawa, id_obszar) VALUES ('Obraz 1', 99.0, '2021-01-12', '2021-01-01', 1, 1, 1, 1, 1, 1, 1);
INSERT INTO obraz (nazwa, stan, data_wykonania, data_otrzymania, id_wymiar, id_nurt, id_technika, id_kolorystyka, id_autor, id_wystawa, id_obszar) VALUES ('Obraz 1', 99.0, '2023-01-01', '2021-01-01', 2, 2, 2, 2, 1, 2, 2);
INSERT INTO obraz (nazwa, stan, data_wykonania, data_otrzymania, id_wymiar, id_nurt, id_technika, id_kolorystyka, id_autor, id_wystawa, id_obszar) VALUES ('Obraz 1', 99.0, '2021-01-01', '2021-01-01', 3, 3, 3, 3, 3, 3, 3);
INSERT INTO obraz (nazwa, stan, data_wykonania, data_otrzymania, id_wymiar, id_nurt, id_technika, id_kolorystyka, id_autor, id_wystawa, id_obszar) VALUES ('Obraz 1', 99.0, '0001-01-01', '2021-01-01', 4, 4, 4, 4, 4, 4, 4);
INSERT INTO obraz (nazwa, stan, data_wykonania, data_otrzymania, id_wymiar, id_nurt, id_technika, id_kolorystyka, id_autor, id_wystawa, id_obszar) VALUES ('Obraz 1', 99.0, '1732-01-01', '2021-01-01', 5, 5, 5, 5, 5, 5, 5);

-- SELECT * FROM autor;
-- SELECT * FROM adres;
-- SELECT * FROM wymiar;
-- SELECT * FROM nurt;
-- SELECT * FROM technika;
-- SELECT * FROM kolorystyka;
-- SELECT * FROM wystawa;
-- SELECT * FROM termin;
-- SELECT * FROM obszar;
-- SELECT * FROM pracownik;
-- SELECT * FROM obraz;
-- SELECT * FROM pietro;
-- SELECT * FROM stanowisko;

-- znajdz autorów którzy mają więcej niż 1 obraz
SELECT autor.imie, autor.nazwisko, count(obraz.id_obraz) as paintings
FROM autor
JOIN obraz ON autor.id_autor = obraz.id_autor
GROUP BY autor.id_autor, autor.imie, autor.nazwisko
HAVING count(obraz.id_obraz) > 1;

-- znajdz obszary bez pracowników
SELECT obszar.*
FROM obszar
LEFT JOIN pracownik ON pracownik.id_obszar = obszar.id_obszar
WHERE pracownik.id_pracownik IS NULL;

-- znajdz wystawy które moją co najmniej jeden obraz namalowany w 2021 roku
SELECT wystawa.nazwa_wystawa, obraz.nazwa
FROM wystawa
JOIN termin ON wystawa.id_wystawa = termin.id_wystawa
JOIN obraz ON termin.id_termin = obraz.id_wystawa
WHERE obraz.data_wykonania LIKE '2021%';

-- znajdz pracowników którzy mają pensję większą niż średnia pensja pracowników
SELECT pracownik.imie, pracownik.nazwisko, pracownik.pensja
FROM pracownik
WHERE pracownik.pensja > (SELECT AVG(pracownik.pensja) FROM pracownik);

-- znajdz obszar z największą średnią pensją
SELECT TOP 1 obszar.nazwa_obszar, AVG(pracownik.pensja) AS srednia_pensja
FROM obszar
INNER JOIN pracownik ON pracownik.id_obszar = obszar.id_obszar
GROUP BY obszar.nazwa_obszar
ORDER BY srednia_pensja DESC;


