import json


class JsonObject:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._read_file()

    def _read_file(self):
        with open(self.filename, "r") as json_file:
            data = json.load(json_file)
        return data

    def get_sort_data(self):
        raise NotImplementedError


class ListJsonObject(JsonObject):
    def get_sort_data(self):
        return sorted(self.data)


class DictJsonObject(JsonObject):
    def get_sort_data(self):
        keys = self.data.keys()
        new_dict = {key: self.data[key] for key in sorted(keys, key=len)}
        return new_dict


my_list_obj = ListJsonObject("tmp_2/list.json")
my_list = my_list_obj.get_sort_data()
print(my_list)

my_dict_obj = DictJsonObject("tmp_2/dict.json")
my_dict = my_dict_obj.get_sort_data()
print(my_dict)
