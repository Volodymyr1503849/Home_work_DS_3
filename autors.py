import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://quotes.toscrape.com"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


def list_of_link():
    link = soup.select("[href^='/author']")
    pattern = r'"(.*?)"'
    list_of_url = [url + re.findall(pattern, str(i))[0] for i in link]
    return list_of_url


def data_creator(list_of_url):
    data_list = []
    for url in list_of_url:
        dict_of_data = {}
        page_auth = requests.get(url)
        soup_auth = BeautifulSoup(page_auth.text, "lxml")
        dict_of_data["fullname"] = soup_auth.find_all("h3", class_="author-title")[
            0
        ].text
        dict_of_data["born_date"] = soup_auth.find_all(
            "span", class_="author-born-date"
        )[0].text
        dict_of_data["born_location"] = soup_auth.find_all(
            "span", class_="author-born-location"
        )[0].text
        dict_of_data["description"] = soup_auth.find_all(
            "div", class_="author-description"
        )[0].text
        if dict_of_data not in data_list:
            data_list.append(dict_of_data)
    return data_list


def create_authors_file(data_list):
    file_path = "authors.json"
    with open(file_path, "w") as file:
        json.dump(data_list, file, indent=4)


if __name__ == "__main__":
    list_of_url = list_of_link()
    data_list = data_creator(list_of_url)
    create_authors_file(data_list)
