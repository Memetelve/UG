from datetime import datetime, timedelta


def calculate_biorhythms(birth_date, current_date):
    physical = 50 * (1 - ((current_date - birth_date).days % 23) / 23)
    emotional = 50 * (1 - ((current_date - birth_date).days % 28) / 28)
    intellectual = 50 * (1 - ((current_date - birth_date).days % 33) / 33)
    return physical, emotional, intellectual


def get_birthday():
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia: "))
    month = int(input("Podaj miesiąc urodzenia: "))
    day = int(input("Podaj dzień urodzenia: "))
    return name, datetime(year, month, day)


def print_biorhythms(physical, emotional, intellectual):
    print("\nTwoje wyniki biorytmów:")
    print(f"Fizyczne: {physical}")
    print(f"Emocjonalne: {emotional}")
    print(f"Intelektualne: {intellectual}")


def main():
    name, birth_date = get_birthday()
    today = datetime.now()
    days_alive = (today - birth_date).days
    print(f"\nWitaj, {name}! Dzisiaj jest {today.strftime('%d/%m/%Y')}.")
    print(f"Jesteś już {days_alive} dni na świecie.")

    physical, emotional, intellectual = calculate_biorhythms(birth_date, today)
    print_biorhythms(physical, emotional, intellectual)

    if physical > 50:
        print("Twoje wyniki fizyczne są wysokie. Gratulacje!")
    elif physical < 50:
        print("Twoje wyniki fizyczne są niskie. Pociesz się, jutro będzie lepiej!")

    if emotional > 50:
        print("Twoje wyniki emocjonalne są wysokie. Gratulacje!")
    elif emotional < 50:
        print("Twoje wyniki emocjonalne są niskie. Pociesz się, jutro będzie lepiej!")

    if intellectual > 50:
        print("Twoje wyniki intelektualne są wysokie. Gratulacje!")
    elif intellectual < 50:
        print("Twoje wyniki intelektualne są niskie. Pociesz się, jutro będzie lepiej!")


if __name__ == "__main__":
    main()
