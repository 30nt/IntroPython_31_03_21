import csv


def read_csv(filename) -> list:
    with open(filename, 'r', encoding="utf-8") as f:
        data = []
        reader = csv.reader(f)  # , delimiter=";")
        for row in reader:
            data.append(row)
    return data


def read_dict_csv(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = []
        reader = csv.DictReader(f)  # , delimiter=";")
        for row in reader:
            data.append(dict(row))
    return data


def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def write_dict_csv(filename, data):
    with open(filename, 'w') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


print(">>>>>>>>>>>>>", __name__)
if __name__ == "__main__":
    print('TOOLS')
    data = read_csv("test.csv")
    print(data)
    assert data != []
