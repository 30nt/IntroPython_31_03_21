# FILE_NAME = "Homework9_files/authors.txt"
#
#
# def take_data_date(filename=FILE_NAME):
#     with open(filename, "r") as txt_file:
#         data = txt_file.readlines()
#     return data
#
# take_data_date("tmt.txt")

# months = ("Jan", "Feb", "Mar")
# numb = ["01", "02", "03", "04"]
# # new = [1,2,3]
#
# res = dict(zip(months, numb))
# print(res)
import requests

# import time

url = "http://api.forismatic.com/api/1.0/"

for number in range(10):
    # time.sleep(2)
    params = {"method": "getQuote",
              "format": "json",
              "key": number}
    r = requests.get(url, params=params)
    data = r.json()
    quote = data["quoteText"]
    author = data["quoteAuthor"]
    print(author)
    print(quote)
