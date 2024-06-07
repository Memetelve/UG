import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = [(random.randint(0, 200), random.randint(0, 200)) for _ in range(10)]


def random_coord():
    r = random.randint(0, len(COORDS))
    return r


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

colony = AntColony(
    COORDS,
    ant_count=100,
    alpha=0.5,
    beta=1.2,
    pheromone_evaporation_rate=0.4,
    pheromone_constant=500.0,
    iterations=100,
)

optimal_nodes = colony.get_path()

for i in range(len(optimal_nodes) - 1):
    plt.plot(
        (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
        (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
    )


plt.savefig("./png/ex2.png")


# zwiększenie liczby wierzchołków zwieksza czas obliczeń
# zwiększenie liczby mrówek zwiększa czas obliczeń
# zmiana parowania nie powoduje znaczących zmian
# zmiana stałej feromonowej powoduje zmiany w wynikach niezależnie od tego czy zwiekszamy czy zmniejszamy

# if większa alpha to większe znaczenie ma feromon
# if większa beta to większe znaczenie ma odległość (długość fragmentu trasy)
