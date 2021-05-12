# csv
import random
import tools

data = tools.read_csv("persons.csv")
for row in data[1:]:
    row[1] = int(row[1]) + 1

data[0].append("Education")
for row in data[1:]:
    row.append(random.choice([0,1]))
tools.write_csv("test_2.csv", data)

# header = data.pop(0)
# for row in data:
#     print(row[1])
# data = [header] + data

filename = "persons.csv"
data = tools.read_dict_csv(filename=filename)
for row in data:
    row["Education"] = random.choice([0,1])

tools.write_dict_csv("persons_2.csv", data)
print(data)