def print_items_in_list(list_of_items):
    for item in list_of_items:
        print(item)


# print_items_in_list(["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"])

def print_nums_25_to_50():
    for x in range(24, 50):
        print(x + 1)


# print_nums_25_to_50()

def print_items_and_indices(list_of_items):
    for x, item in enumerate(list_of_items):
        print("{} is index {}.".format(item, x))


# print_items_and_indices(["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"])
