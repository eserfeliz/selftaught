import os


def print_file():
    private_key = os.path.join('C:\\', 'Users', 'me', '.ssh', 'id_rsa')

    with open(private_key, "r") as f:
        print(f.read())


def question():
    response_store = os.path.join('C:\\', 'Users', 'me', 'response.txt')

    response = input('Where do you find enlightenment?\n')

    with open(response_store, "w") as f:
        f.write(response)


# question()

def create_csv(list_of_lists):
    import csv

    csv_location = os.path.join('C:\\', 'Users', 'me', 'shows.csv')

    with open(csv_location, "w", newline='') as c:
        w = csv.writer(c, delimiter=',')
        for row in list_of_lists:
            w.writerow(row)
    print("Done. file: {}".format(csv_location))


# create_csv([["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"],
#             ["Training Day", "Man on Fire", "Flight"]])
