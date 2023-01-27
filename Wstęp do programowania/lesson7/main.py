
# template = {'nazwa': '', 'gęstość': 0}
database = [{'nazwa': 'Mars', 'gęstość': 5.427}, {'nazwa': 'Ziemia', 'gęstość': 5.513}]

def add_planet(name, density, base):
    planet = {'nazwa': name, 'gęstość': density}
    for x, item in enumerate(base):
        if item['gęstość'] < planet['gęstość']:
            base.insert(x, planet)
            break
    else:
        base.append(planet)

    return base


print(database)
print(add_planet('Wenus', 5.204, database))

def read_planet(name, base):  # sourcery skip: use-next, useless-else-on-loop
    for item in base:
        if item['nazwa'] == name:
            return (item["nazwa"], item["gęstość"])
    else:
        return None


print(read_planet('Ziemia', database))

def updatePlanet(name, density, base):
    for item in base:
        if item['nazwa'] == name:
            item['gęstość'] = density
            break
    else:
        return None

    return base

print(updatePlanet('Wenus', 1.0, database))

def deletePlanet(density, base):
    for item in base:
        if item['gęstość'] < density:
            base.remove(item)

    return base

print(deletePlanet(1, database))

def searchPlanet(name, base):
    for index, item in enumerate(base):
        if item['nazwa'] == name:
            return index

    return -1

print(searchPlanet('Mars', database))

