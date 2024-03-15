import math
import datetime


def physical_wave(days: int) -> float:
    return 1.0 * math.sin(2 * math.pi * days / 23)


def emotional_wave(days: int) -> float:
    return 1.0 * math.sin(2 * math.pi * days / 28)


def intellectual_wave(days: int) -> float:
    return 1.0 * math.sin(2 * math.pi * days / 33)


def main():
    name = input("Enter your name: ")
    yob = int(input("Enter your year of birth: "))
    mob = int(input("Enter your month of birth: "))
    dob = int(input("Enter your day of birth: "))

    day_of_life = datetime.date.today() - datetime.date(yob, mob, dob)

    wave_names = ["physical", "emotional", "intellectual"]
    wave_functions = [physical_wave, emotional_wave, intellectual_wave]

    wave_values = [wave_function(day_of_life.days) for wave_function in wave_functions]

    print(f"Hello {name}! You are {day_of_life.days} days old.")
    print(f"Your physical wave is {wave_values[0]:.2f}")
    print(f"Your emotional wave is {wave_values[1]:.2f}")
    print(f"Your intellectual wave is {wave_values[2]:.2f}")

    for i, value in enumerate(wave_values):
        if value > 0.5:
            print(f"Your {wave_names[i]} is good today, good job!")
        elif value < -0.5:
            additional_msg = (
                ""
                if value > wave_functions[i](day_of_life.days + 1)
                else " But tomorrow will be better!"
            )
            print(f"Your {wave_names[i]} is bad today, be careful!" + additional_msg)


if __name__ == "__main__":
    main()
