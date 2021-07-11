import random

with open("20kWords", "r") as file:
    words = file.read().split("\n")

    middle_index = len(words) // 2
    first_half = words[:middle_index]
    second_half = words[middle_index:]

    def random_common() -> str:
        return random.choice(first_half).capitalize()

    def random_rare() -> str:
        return random.choice(second_half).capitalize()


    def get_good_password() -> str:
        picked_words = [random_rare()]
        password = "".join(picked_words)
        while len(password) < 20:
            picked_words.append(random_common())
            random.shuffle(picked_words)
            password = "".join(picked_words)
        return password


    inpt = ""
    while input != "Y":
        print(get_good_password())
        inpt = input()
