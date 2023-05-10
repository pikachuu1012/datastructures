"""Functions to parse a file containing villager data."""

#opens, splits according to | 
##############################
        # f = open("villagers.csv")
        # for line in f:
        #     villager_entry = line.split("|")
        #     print(villager_entry)
        #     print()

        # f.close()
#############################




def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    f = open(filename)
    species_list = []

    for line in f:
        entry = line.split("|")
        species_list.append(entry[1])

    species = set(species_list)
    f.close()

    # TODO: replace this with your code
    print(species)
    return species
#all_species("villagers.csv")


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    f = open(filename)
   
    for line in f: 
        villager_entry = line.split("|")
        if search_string == villager_entry[1]:
            villagers.append(villager_entry[0])
    print(sorted(villagers))
    return sorted(villagers)

#get_villagers_by_species("villagers.csv", "Cat")

#       ?????? ****** IS THIS WHAT THEY MEAN ???? ####
def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    f = open(filename)
    listoflists = []
    for entry in f:
        villager = entry.split("|")
        listoflists.append(villager)
    

    listoflists.sort(key = lambda listoflists: listoflists[3]) #sorts by hobby
    for l in listoflists:
        print(l)

    f.close()
    return []
all_names_by_hobby("villagers.csv")

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    f = open(filename)
    for line in f:
        entry = line.split("|")
        #name, species, personality, hobby, catchphrase
        mytuple = (entry[0], entry[1], entry[2], entry[3], entry[4])
        
        all_data.append(mytuple)
    f.close()
    print(all_data)
    return all_data
all_data("villagers.csv")

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    f = open(filename)
    for line in f:
        villager_entry = line.split("|")
        name = villager_entry[0]
        if name == villager_name:
            print(villager_entry[-1])
            return villager_entry[-1]
    f.close()
    print("No villager with name: ", villager_name)
    return None
find_motto("villagers.csv", "Tangy")
find_motto("villagers.csv", "Tagy")
find_motto("villagers.csv", "Marshal")

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    

    f = open(filename)
    personality = "blank"
    myset = {1,}
    for line in f:
        entry = line.split("|")
        name = entry[0]
        if name == villager_name:
            personality = entry[2]
            break
        
    print("personality to look for: ", personality)
    for line in f: 
        
        entry = line.split("|")

        if personality == entry[2]:
            myset.add(entry[0])

    myset.remove(1)
    print(myset)
    return myset


find_likeminded_villagers("villagers.csv", "Tangy")
