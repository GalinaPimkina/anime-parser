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


with open("shiki.json", "r", encoding="utf-8") as file:
    all_anime = json.load(file)

    for anime_title, anime_href in all_anime.items():
        lst = [")", "("]
        for symbol in anime_title:
            if symbol not in lst and not symbol.isalnum():
                anime_title = anime_title.replace(symbol, "_")

        if "__" in anime_title:
            anime_title = anime_title.replace("__", "_")

        #буду проходиться по каждой ссылке на конкретное аниме, сохраняю страницу на каждое аниме, чтобы не было нагрузки на сайт

        req = requests.get(url=anime_href, headers=headers)
        src = req.text

        with open(f"animes/{anime_title}.html", "w", encoding="utf-8") as file:
            file.write(src)

        with open(f"animes/{anime_title}.html", "r", encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        ru_en_title = soup.find("h1").text
        ru_title = ru_en_title[:ru_en_title.find("/")].rstrip()
        en_title = ru_en_title[ru_en_title.find("/")+1:].lstrip()
        image_href = soup.find("div", class_="b-db_entry-poster").get("data-href")

        # print(ru_title)
        # print(en_title)
        # print(image_href)

        format_type = soup.find("div", class_="b-entry-info").find(class_="line-container")
        format_type_key = format_type.find(class_="key").text[:-1]
        format_type_value = format_type.find(class_="value").text
        # print(format_type_key, " - ", format_type_value)

        # отсюда поиск пойдет двумя разными путями, т.к. в описании каких-то аниме отсутствует пункт "Эпизоды", если он там 1
        # ЭПИЗОДЫ
        episodes = format_type.find_next(class_="line-container")
        # если есть пункт "Эпизоды":
        if episodes.find(class_="key").text[:-1] == "Эпизоды":
            episodes_key = episodes.find(class_="key").text[:-1]
            episodes_value = episodes.find(class_="value").text
            print(episodes_key, "-", episodes_value)

            # ДЛИТЕЛЬНОСТЬ ЭПИЗОДА
            len_episodes = episodes.find_next(class_="line-container")
            len_episodes_key = len_episodes.find(class_="key").text[:-1]
            len_episodes_value = len_episodes.find(class_="value").text
            print(len_episodes_key, "  ---  ", len_episodes_value)

            # СТАТУС ВЫХОДА
            status = len_episodes.find_next(class_="line-container")
            status_key = status.find(class_="key").text[:-1]
            status_value = status.find(class_="value")
            # статус-вышло, выходит и тд.
            status_value_tag = status_value.find(class_="b-anime_status_tag").get("data-text")
            # даты выхода
            status_value_date = status.find(class_="value").text
            print(status_key, status_value_tag, status_value_date)
            print(ru_title)
            print("----"*10)


        else:
            # ЭПИЗОДЫ / если в графе пусто, значит эпизод 1, искусственно добавляем
            episodes_key = "Эпизоды"
            episodes_value = "1"
            print(episodes_key, "-", episodes_value)

            # ДЛИТЕЛЬНОСТЬ ЭПИЗОДА
            len_episodes = format_type.find_next(class_="line-container")
            # дублирование кода -----
            len_episodes_key = len_episodes.find(class_="key").text[:-1]
            len_episodes_value = len_episodes.find(class_="value").text
            print(len_episodes_key, "  ---  ", len_episodes_value)

            # СТАТУС ВЫХОДА
            status = len_episodes.find_next(class_="line-container")
            status_key = status.find(class_="key").text[:-1]
            status_value = status.find(class_="value")
            # статус-вышло, выходит и тд.
            status_value_tag = status_value.find(class_="b-anime_status_tag").get("data-text")
            # даты выхода
            status_value_date = status.find(class_="value").text
            print(status_key, status_value_tag, status_value_date)
            print(ru_title)
            print("----" * 10)












