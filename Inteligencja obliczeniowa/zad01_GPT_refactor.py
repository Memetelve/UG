import math
import datetime


def physical_wave(days: int) -> float:
    """Calculate the physical wave value."""
    return 1.0 * math.sin(2 * math.pi * days / 23)


def emotional_wave(days: int) -> float:
    """Calculate the emotional wave value."""
    return 1.0 * math.sin(2 * math.pi * days / 28)


def intellectual_wave(days: int) -> float:
    """Calculate the intellectual wave value."""
    return 1.0 * math.sin(2 * math.pi * days / 33)


def main():
    name = input("Enter your name: ")
    yob = int(input("Enter your year of birth: "))
    mob = int(input("Enter your month of birth: "))
    dob = int(input("Enter your day of birth: "))

    birth_date = datetime.date(yob, mob, dob)
    days_alive = (datetime.date.today() - birth_date).days

    wave_functions = [physical_wave, emotional_wave, intellectual_wave]
    wave_names = ["physical", "emotional", "intellectual"]

    # Calculate wave values
    wave_values = [wave_func(days_alive) for wave_func in wave_functions]

    print(f"Hello {name}! You are {days_alive} days old.")

    # Display wave values
    for name, value in zip(wave_names, wave_values):
        print(f"Your {name} wave is {value:.2f}")

    # Check wave statuses
    for name, value, wave_func in zip(wave_names, wave_values, wave_functions):
        if value > 0.5:
            print(f"Your {name} wave is good today, good job!")
        elif value < -0.5:
            # Check if tomorrow's wave is better
            if value < wave_func(days_alive + 1):
                print(
                    f"Your {name} wave is bad today, be careful! But tomorrow will be better!"
                )
            else:
                print(f"Your {name} wave is bad today, be careful!")


if __name__ == "__main__":
    main()
