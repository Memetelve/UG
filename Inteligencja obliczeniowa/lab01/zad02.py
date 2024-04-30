import math
import random
import matplotlib.pyplot as plt


def calculate_distance(velocity, degree, height):
    degree = math.radians(degree)
    distance = (
        velocity * math.sin(degree)
        + math.sqrt(velocity**2 * math.sin(degree) ** 2 + 2 * 9.81 * height)
    ) * (velocity * math.cos(degree) / 9.81)

    return distance


def calculate_position(velocity, degree, height, time):
    time = time / 100
    degree = math.radians(degree)
    y = velocity * time * math.sin(degree) - 0.5 * 9.81 * time**2 + height

    if y < 0:
        y = None

    return y


def main():
    obstacle_distance = random.randint(50, 340)
    error_margin = 5
    velocity = 50
    height = 100

    print(f"Distance to the obstacle: {obstacle_distance} m")

    degree = input("Enter the angle of the cannon (in degrees): ")
    degree = float(degree)

    while (
        abs(calculate_distance(velocity, degree, height) - obstacle_distance)
        > error_margin
    ):
        if calculate_distance(velocity, degree, height) > obstacle_distance:
            print("Too far!")
        else:
            print("Too close!")
        degree = input("Enter the angle of the cannon (in degrees): ")
        degree = float(degree)

    print("You hit the obstacle!")

    # Plot the trajectory
    x = [i for i in range(0, 340 * 100)]
    y = [calculate_position(velocity, degree, height, i) for i in x]

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
