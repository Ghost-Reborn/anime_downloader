#
# Anime Downloader Reborn
#
# Downloads full anime episodes, movies, OVA etc in
# chronological order
#

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

# Get anime title
anime_scraper_base_url = "https://www.animechrono.com"
anime_scraper_search_url = anime_scraper_base_url + "/search?q="
anime_name = input("Enter anime: ")
anime_combined_url = anime_scraper_search_url + quote(anime_name)

# Connect to URL
anime_html = urlopen(anime_combined_url).read()
soup = BeautifulSoup(anime_html, "html.parser")
anime_search_result = soup.select("#wrapper > div.max-width._100px.w-container > div > div > a")[0]

print(anime_scraper_base_url + anime_search_result['href'])