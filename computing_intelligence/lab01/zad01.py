import math
from datetime import datetime


name = input("What is your name")
year_of_birth = input("What is your year of birth")
month_of_birth = input("What is your month of birth")
day_of_birth = input("What is your day of birth")

year_of_birth = int(year_of_birth)
month_of_birth = int(month_of_birth)
day_of_birth = int(day_of_birth)

birth_date = datetime(year_of_birth, month_of_birth, day_of_birth)
current_date = datetime.now()

age_days = (current_date - birth_date).days

print(f"Hello {name}, you are {age_days} days old")


def physical_wave(age_days):
    return math.sin(2 * math.pi * age_days / 23)


def emotional_wave(age_days):
    return math.sin(2 * math.pi * age_days / 28)


def intellectual_wave(age_days):
    return math.sin(2 * math.pi * age_days / 33)


Physical_result = physical_wave(age_days)
Emotional_result = emotional_wave(age_days)
Intellectual_result = intellectual_wave(age_days)

phys_message = ""
if Physical_result > 0.5:
    phys_message = "You are in a physical high today"
elif Physical_result < -0.5:
    phys_message = "You are in a physical low today"


emot_message = ""
if Emotional_result > 0.5:
    emot_message = "You are in a emotional high today"
elif Emotional_result < -0.5:
    emot_message = "You are in a emotional low today"

intel_message = ""
if Intellectual_result > 0.5:
    intel_message = "You are in a intellectual high today"
elif Intellectual_result < -0.5:
    intel_message = "You are in a intellectual low today"


phys_better_tommorow = Physical_result < physical_wave(age_days + 1)
emot_better_tommorow = Emotional_result < emotional_wave(age_days + 1)
intel_better_tommorow = Intellectual_result < intellectual_wave(age_days + 1)

if phys_better_tommorow:
    print("You will feel better physically tomorrow")
if emot_better_tommorow:
    print("You will feel better emotionally tomorrow")
if intel_better_tommorow:
    print("You will feel better intellectually tomorrow")

print(phys_message)
print(emot_message)
print(intel_message)
