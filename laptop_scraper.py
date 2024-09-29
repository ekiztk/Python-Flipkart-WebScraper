import time
from selenium import webdriver 
from bs4 import BeautifulSoup
import os
from classes.WebDriverThread import WebDriverThread

from classes.laptop import Laptop
from helper_functions.get_laptop_reviews import get_laptop_reviews, get_reviews_on_a_page
from helper_functions.write_laptop_array_to_json import write_laptop_array_to_json
import constants.laptop_constants as constants

LAPTOP_COUNT = 1
CURR_PAGE_NUMBER = 1 

driver = webdriver.Chrome()
driver.implicitly_wait(5)

all_laptop_urls = []

# Getting All Laptop Urls
while len(all_laptop_urls) < LAPTOP_COUNT:
    driver.get(f"https://www.flipkart.com/laptops/pr?sid=6bo,b5g&sort=popularity&page={CURR_PAGE_NUMBER}")
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
file_to_save_laptop_details = "data/laptop/laptop_details.json"
if os.path.exists(file_to_save_laptop_details):
  os.remove(file_to_save_laptop_details)

f = open(file_to_save_laptop_details, "x")

def get_laptop_specifications(tbody, spec_keys):
    specs = {}
    rows = tbody.find_all('tr', class_='WJdYP6 row')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            key = cells[0].get_text(strip=True)
            if key in spec_keys:
                value = cells[1].get_text(strip=True)
                specs[key] = value
                if len(specs) == len(spec_keys):
                    break
    return specs

# Laptops that will be being scrapped
for url in all_laptop_urls:
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Get name
    name = soup.find('span', attrs={'class': constants.NAME_SPAN}).string.split('-')[0].rstrip()

    processor_memory_features_tbody = soup.find('div', attrs={'class': constants.SPECIFICATIONS_PARENT_DIV}).contents[1].contents[1].contents[0]
    spec_keys = ['Processor Brand', 'Processor Name', 'RAM', 'Storage Type','SSD Capacity']
    specs = get_laptop_specifications(processor_memory_features_tbody, spec_keys)

    processor_brand = specs.get('Processor Brand',None)
    processor_name = specs.get('Processor Name',None)
    ram_capacity = specs.get('RAM',None)
    storage_type = specs.get('Storage Type',None)
    storage_capacity = specs.get('SSD Capacity',None)

    display_features_tbody = soup.find('div', attrs={'class': constants.SPECIFICATIONS_PARENT_DIV}).contents[4].contents[1].contents[0]
    spec_keys = ['Screen Size']
    specs = get_laptop_specifications(display_features_tbody, spec_keys)

    screen_size = specs.get('Screen Size',None)
    if screen_size:
        screen_size = screen_size.split('(')[1].split(')')[0]
    

    # Get construction information
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._1JDTUN"))).click()
    
    # Get reviews
    reviews = []
    review_div_arr = soup.find_all('div', class_= constants.A_REVIEW_DIV)
    all_reviews_div = soup.find('div', attrs={'class': constants.REVIEW_COUNT_DIV})
    #if review count is greater than three then go to reviews page
    if all_reviews_div:
        reviews_url = "https://www.flipkart.com" + all_reviews_div.parent.get('href')
        reviews_thread = WebDriverThread(target=get_laptop_reviews, args=(reviews_url,1))
        reviews_thread.start()
        reviews = reviews_thread.join()
    #if review count is less than three then get ratings from the current page
    elif review_div_arr:
        get_reviews_on_a_page(url,driver,reviews, constants.A_REVIEW_DIV)

    # Add the laptop to the array (Ending)
    laptop = Laptop(url=url,name=name,processor_brand=processor_brand,
                    processor_name=processor_name,ram_capacity=ram_capacity,
                    storage_type=storage_type,storage_capacity=storage_capacity,
                    screen_size=screen_size)
    
    laptop_array.append(laptop.__dict__)

driver.quit()

print("Started Writing Laptops To File")
write_laptop_array_to_json(laptop_array, file_to_save_laptop_details)
print("Finished Writing Laptops To File")