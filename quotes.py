import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")


def create_data():
    data_list = []
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    tags_divs = soup.find_all("div", class_="tags")
    for quote, author, tags_div in zip(quotes, authors, tags_divs):
        tags = [tag.text for tag in tags_div.find_all("a", class_="tag")]
        dict_of_data = {
            "quote": quote.text,
            "author": author.text,
            "tags": tags
        }
        if dict_of_data not in data_list:
            data_list.append(dict_of_data)
    return data_list

def create_tags_file(data_list):
    file_path = "quotes.json"
    with open(file_path, "w") as file:
        json.dump(data_list, file, indent=4)


if __name__ == "__main__":
    data_list = create_data()
    create_tags_file(data_list)
