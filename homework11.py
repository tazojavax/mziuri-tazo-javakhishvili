with open("number.txt", "r") as numbers_file, open("squere.txt", "w") as squere_file:
    numbers = numbers_file.readlines()

    for i in numbers:
        num = int(i.strip())
        squere_file.write(str(num ** 2) + "\n")