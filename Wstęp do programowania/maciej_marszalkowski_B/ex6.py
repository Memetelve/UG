
database = [{'name': 'ania', 'position': 2, 'speed': 2}, {'name': 'jan', 'position': 1, 'speed': 9.81}]

# {'name': 'jan', 'position': 1, 'speed': 9.81}

def create(name, position, speed, base):
    for i, person in enumerate(database):
        if person['name'].lower() < name.lower():
            pass
        else:
            base.insert(i, {'name': name, 'position': position, 'speed': speed})
            return base

        if i == len(base)-1:
            base.append({'name': name, 'position': position, 'speed': speed})
            return base

database = create('zygmunt', 3, 3, database)
print(database)

def search(name, base):

    name = name.lower()

    start = 0
    end = len(base) - 1

    while start <= end:
        mid = (start + end) // 2


        current_name = base[mid]['name'].lower()

        if current_name == name:
            return mid
        elif name < current_name:
            end = mid - 1
        else:
            start = mid + 1

    return -1

index = search('kasztan', database)
print(index)

def delete(name, base: list):

    index = search(name, base)

    # binary search niekoniecznie znajduje pierwsze wystąpienie
    while True:
        if base[index-1]['name'].lower() == name.lower():
            index = index-1
        else:
            break
    
    base.pop(index)

    return base

database = delete('zygmunt', database)
print(database)



