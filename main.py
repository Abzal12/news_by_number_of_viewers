from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_value_of_list = max(article_upvotes)
max_index = article_upvotes.index(max_value_of_list)
print(article_texts[max_index])
print(article_links[max_index])
print(max_value_of_list)
# with open("website.html", "r") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText(), tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section = soup.find(class_="heading")
# print(section.name)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select_one(".heading")
# print(headings)
