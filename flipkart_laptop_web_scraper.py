import json
import time
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd
import os
from classes.WebDriverThread import WebDriverThread

from classes.laptop import Laptop
from helper_functions.get_laptop_customer_questions import get_laptop_customer_questions
from helper_functions.get_laptop_ratings import get_laptop_ratings
from helper_functions.get_laptop_reviews import get_laptop_reviews, get_reviews_on_a_page
from helper_functions.write_laptop_array_to_json import write_laptop_array_to_json
import constants.laptop_constants as constants

LAPTOP_COUNT = 10 
CURR_PAGE_NUMBER = 1 

driver = webdriver.Chrome()
driver.implicitly_wait(5)

all_laptop_urls = []

# Getting All Laptop Urls
while len(all_laptop_urls) < LAPTOP_COUNT:
    driver.get(f"https://www.flipkart.com/laptops/pr?sid=6bo,b5g&page={CURR_PAGE_NUMBER}")
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    all_laptop_a = soup.findAll('a', href=True, attrs={'class': constants.ALL_LAPTOPS_A}, limit=(LAPTOP_COUNT - len(all_laptop_urls)))

    # Linkleri listeye ekleme
    for a in all_laptop_a:
        all_laptop_urls.append("https://www.flipkart.com" + a['href'])
    
    if len(all_laptop_urls) >= LAPTOP_COUNT:
        break

    CURR_PAGE_NUMBER += 1
    time.sleep(2) 

# Getting Each Laptop Detail

# Get the file ready
laptop_array = []
file_to_save_laptop_details = "data/laptops/laptop_details.json"
if os.path.exists(file_to_save_laptop_details):
  os.remove(file_to_save_laptop_details)

f = open(file_to_save_laptop_details, "x")

# Laptops that will be being scrapped
for url in all_laptop_urls:
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Get name and highlights
    name = soup.find('span', attrs={'class': constants.NAME_SPAN}).string
    highlights_li_arr = soup.find_all('li', attrs={'class': constants.HIGHLIGHTS_LI})
    highlights = []
    for li in highlights_li_arr:
        highlights.append(li.string)

    # Get description
    description_div = soup.find('div', attrs={'class': constants.DESCRIPTION_DIV})
    description = ""
    if description_div:
        description = description_div.contents[0].contents[0].text

    # Get features (optional)
    features_div_arr =  soup.find_all('div', attrs={'class': constants.FEATURE_TITLE_DIV})
    features= []
    if features_div_arr:
        for div in features_div_arr:
            parent = div.parent
            f = dict(title = parent.contents[0].string, description = parent.contents[1].contents[0].string)
            features.append(f)

    # Get specifications
    specifications_parent_div = soup.find('div', attrs={'class': constants.SPECIFICATIONS_PARENT_DIV})
    specifications = []
    for specification_div in specifications_parent_div.contents:
        category = specification_div.contents[0].string
        properties = []
        table = specification_div.contents[1].contents[0] #tbody

        for tr in table:
            properties.append({"name":tr.contents[0].string, "content": tr.contents[1].string})
        
        specifications.append(dict(category = category, properties = properties))

    # Get construction information
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._1JDTUN"))).click()
    
    # Get ratings
    ratings = []
    all_reviews_div = soup.find('div', attrs={'class': constants.REVIEW_COUNT_DIV})
    ratings_div = soup.find('div', class_= constants.RATINGS_DIV)
    #if review count is greater than three then go to reviews page
    if all_reviews_div:
        rating_url = "https://www.flipkart.com" + all_reviews_div.parent.get('href')
        ratings_thread = WebDriverThread(target=get_laptop_ratings, args=(rating_url,))
        ratings_thread.start()
        ratings = ratings_thread.join()
    #if review count is less than three then get ratings from the current page
    elif ratings_div:
        overall_rating = ratings_div.contents[0].contents[0].contents[0].contents[0].contents[0].contents[0].text
        ratings.append({"Overall": overall_rating})

    # Get reviews
    reviews = []
    review_div_arr = soup.find_all('div', class_= constants.A_REVIEW_DIV)
    #if review count is greater than three then go to reviews page
    if all_reviews_div:
        reviews_thread = WebDriverThread(target=get_laptop_reviews, args=(rating_url,1))
        reviews_thread.start()
        reviews = reviews_thread.join()
    #if review count is less than three then get ratings from the current page
    elif review_div_arr:
        get_reviews_on_a_page(url,driver,reviews, constants.A_REVIEW_DIV)

    # Get customer questions
    customer_questions = []
    questions_answers_title_div = soup.find('div', attrs={'class': constants.QUESTIONS_ANSWERS_TITLE_DIV})
    # check if Questions and Answers exits
    if questions_answers_title_div:
        questions_thread = WebDriverThread(target=get_laptop_customer_questions, args=(url,1))
        questions_thread.start()
        customer_questions = questions_thread.join()

    # Add the laptop to the array (Ending)
    laptop = Laptop(url=url,name=name,highlights=highlights,description = description,features=features,
                    specifications=specifications,ratings=ratings,
                    reviews=reviews,customer_questions=customer_questions)
    
    laptop_array.append(laptop.__dict__)

driver.quit()

print("Started Writing Laptops To File")
write_laptop_array_to_json(laptop_array, file_to_save_laptop_details)
print("Finished Writing Laptops To File")