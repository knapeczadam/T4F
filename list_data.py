import csv


class ListData:

    def list_data():
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

        for key in dicta:
            print("\n%s" % key, end=" ")
            for element in dicta[key]:
                if element == dicta[key][0]\
                        or element == dicta[key][2]\
                        or element == dicta[key][3]\
                        or element == dicta[key][9]:
                    print(element)
