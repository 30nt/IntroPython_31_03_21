import random
from tools import read_dict_csv, write_dict_csv

print("<<<<<<<<<<<", __name__)

filename = "persons.csv"
data = read_dict_csv(filename=filename)
for row in data:
    row["Education"] = random.choice([0,1])

write_dict_csv("persons_2.csv", data)
print(data)