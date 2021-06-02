import requests
from requests_oauthlib import OAuth1
import os


class IconSaver:
    def __init__(self):
        self._auth = OAuth1(os.getenv("KEY"), os.getenv("SECRET"))
        self._endpoint = "http://api.thenounproject.com/icon/"

    def get_icon_by_id(self, id, save=False):
        response = requests.get(self._endpoint + f"{id}", auth=self._auth)
        res = response.json()
        icon_url = res["icon"]["icon_url"]
        icon_res = requests.get(icon_url)
        if save:
            self._save_icon(id, icon_res)
        return icon_res.content

    def _save_icon(self, id, icon_res):
        with open(f"tmp/{id}.svg", "wb") as file:
            file.write(icon_res.content)


icon_saver = IconSaver()
icon = icon_saver.get_icon_by_id(17)
print(icon)
