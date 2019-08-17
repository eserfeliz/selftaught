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

def guess_a_number(list_of_nums):
    n = 0
    prompt = ''
    while prompt != 'q':
        print(list_of_nums)
        prompt = input('Which number in the above list am I thinking of? (enter "q" to quit) ')
        if prompt == 'q':
            break
        else:
            try:
                prompt = int(prompt)
            except ValueError:
                print('Entry must be an integer or the letter "q"')
                break
        if list_of_nums[n % len(list_of_nums)] == prompt:
            print('You guessed it!')
            break
        else:
            print("Nope, try again...")
        n += 1


# guess_a_number([1, 4, 5, 19, 81])

def multiply_numbers():
    list1 = [8, 19, 148, 4]
    list2 = [9, 1, 33, 83]
    list3 = []

    for i, values in enumerate(list1):
        list3.append(int(list1[i]) * int(list2[i]))
    print(list3)


# multiply_numbers()
