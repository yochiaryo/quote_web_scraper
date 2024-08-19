import requests
from bs4 import BeautifulSoup
import csv

url = 'https://quotes.toscrape.com'

response = requests.get(url)

with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Quote", "Author", "Tags"])

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        quote_blocks = soup.select("div.quote")
        for quote in quote_blocks:
            title = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = ", ".join([tag.text for tag in quote.find_all("a", class_="tag")])

            writer.writerow([title, author, tags])

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
