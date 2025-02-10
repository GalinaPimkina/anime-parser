from bs4 import BeautifulSoup
import requests
import lxml
from fake_useragent import UserAgent
import json


ua = UserAgent()

headers = {
    "Accept": "*/*",
    "User-Agent": ua.random
}

#сохраняю первую страницу списка в отдельный файл, чтобы не засыпать сайт своими запросами лишний раз

# req = requests.get(url="https://shikimori.one/animes/page/1", headers=headers)
# src = req.text
#
# with open("shiki.html", "w", encoding="utf-8") as file:
#     file.write(src)
#

#из полученного файла считываю данные. хочу составить словарь - название аниме: ссылка

# with open("shiki.html", "r", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# anime_list = soup.find_all("a", class_="cover")
#
# anime_dict = {}
#
# for item in anime_list:
#     title = item.find("span", class_="name-ru").text
#     anime_href = item.get("href")
#
#     anime_dict[title] = anime_href
#

# записываю полученный словарь в json-файл

# with open("shiki.json", "w", encoding="utf-8") as file:
#     json.dump(anime_dict, file, indent=4, ensure_ascii=False)


# из полученного json-файла беру название аниме, привожу к общему виду, убирая лишние символы.

# with open("shiki.json", "r", encoding="utf-8") as file:
#     all_anime = json.load(file)
#
#     for anime_title, anime_href in all_anime.items():
#         lst = [")", "("]
#         for symbol in anime_title:
#             if symbol not in lst and not symbol.isalnum():
#                 anime_title = anime_title.replace(symbol, "_")
#
#         if "__" in anime_title:
#             anime_title = anime_title.replace("__", "_")
#
#         #буду проходиться по каждой ссылке на конкретное аниме, сохраняю страницу на каждое аниме, чтобы не было нагрузки на сайт
#
#         req = requests.get(url=anime_href, headers=headers)
#         src = req.text
#
#         with open(f"animes/{anime_title}.html", "w", encoding="utf-8") as file:
#             file.write(src)


