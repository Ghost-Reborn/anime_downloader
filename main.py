#
# Anime Downloader Reborn
#
# Downloads full anime episodes, movies, OVA etc in
# chronological order
#

# Get anime title
anime_scraper_base_url = "https://www.animechrono.com/search?q="
anime_name = input("Enter anime: ")
anime_combined_url = anime_scraper_base_url + anime_name