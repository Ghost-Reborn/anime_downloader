#
# Anime Downloader Reborn
#
# Downloads full anime episodes, movies, OVA etc in
# chronological order
#

from re import sub
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

# Get anime title from user input
anime_scraper_base_url = "https://www.animechrono.com"
anime_scraper_search_url = anime_scraper_base_url + "/search?q="
anime_name = input("Enter anime: ")
anime_combined_url = anime_scraper_search_url + quote(anime_name)

# Connect and scrape GUIDE url
# TODO get full search result, and show as selectable for the user
anime_html = urlopen(anime_combined_url).read()
soup = BeautifulSoup(anime_html, "html.parser")
anime_search_result = soup.select("#wrapper > div.max-width._100px.w-container > div > div > a")[0]
anime_guide_url = anime_scraper_base_url + anime_search_result['href']

# Connect to anime GUIDE url
anime_html = urlopen(anime_guide_url).read()
soup = BeautifulSoup(anime_html, "html.parser")

# Guide div(s) doesn't have class attribute
saga_main_divs = soup.select("#wrapper > div:nth-child(2) > div > div.div-block-18 > div")
for divs in saga_main_divs:
    if "class" in divs.attrs:
        continue
    print(str(divs.h2.text))
    saga_sub_divs = divs.select("div")
    for sub_divs in saga_sub_divs:
        if(sub_divs.has_attr("class")):
            if(sub_divs.get("class")[0] == "list-item"):
                print(sub_divs.select("div:nth-child(3)")[0].text)
