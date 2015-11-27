import csv


def delete_donor_data_from_file():

    data = []

    with open("Data\donors.csv") as csvfile_read:
        csvreader = csv.reader(csvfile_read, delimiter=",")
        for row in csvreader:
            if row:
                data.append(row)
    csvfile_read.close()

    dicta = {}
    x = 1
    for elements in data:
        dicta[x] = elements
        x += 1
    for h in dicta:
        print(h, end="")
        print(dicta[h])
    find_id = 0
    delete = input("Enter an ID what u want to delete: ")
    if delete:
            for key in dicta:
                for element in dicta[key]:
                    if element == delete:
                        find_id += key
    dicta.pop(find_id)

    print(dicta)
    with (open("Data\donors.csv", 'w')) as writer:
        csvwriter = csv.writer(writer, delimiter=",")
        for word in dicta:
            csvwriter.writerow(dicta[word])
    """
    z = input("Do you want to clear the donors data file? (Y/N)")
    if z.lower() == "y":
        open("Data\donors.csv", 'w').close()
        print("The donors data file has been cleared!")"""
