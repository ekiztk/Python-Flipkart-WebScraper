from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

import constants.laptop_constants as constants

rating_categories = ["Performance", "Battery", "Design", "Display", "Value for Money"]

def get_laptop_ratings(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
    driver.implicitly_wait(5)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    ratings = {}
    ratings["Overall"] = soup.find('div', attrs={'class': constants.RATINGS_OVERALL_DIV}).string

    rating_urls_parent_div = soup.find('div', attrs={'class': constants.RATING_URLS_PARENT_DIV}).contents[0]

    for index, a in enumerate(rating_urls_parent_div.contents[1:]):
        driver.get("https://www.flipkart.com" + a['href'])
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        ratings[rating_categories[index]] = soup.find('text', attrs={'class': constants.RATING_SCORE_TEXT}).string
    
    driver.quit()
    return ratings