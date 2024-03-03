from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd
import os
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from classes.WebDriverThread import WebDriverThread
from helper_functions.get_laptop_ratings import get_laptop_ratings
from helper_functions.get_laptop_reviews import get_laptop_reviews, get_reviews_on_a_page
from helper_functions.write_array_to_json import write_array_to_json
from classes.laptop import Laptop


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.implicitly_wait(5)

driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART&otracker=product_breadCrumbs_Laptops")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

# Getting URLS (sadece bir sayfayı alıyor)
print("Started Getting All Laptop Urls")
all_laptop_a = soup.findAll('a', href=True, attrs={'class':'_1fQZEK'},limit=1)
all_laptop_urls = []

for a in all_laptop_a:
    all_laptop_urls.append("https://www.flipkart.com" + a['href'])

df = pd.DataFrame({'Product Url': all_laptop_urls}) 
df.to_csv('laptop_urls.csv', index=False, encoding='utf-8')
print("Finished Getting All Laptop Urls")


# Getting Each Laptop Detail

# Get the file ready
laptop_array = []
file_to_save_laptop_details = "laptop_details.json"
if os.path.exists(file_to_save_laptop_details):
  os.remove(file_to_save_laptop_details)

f = open(file_to_save_laptop_details, "x")

#burda urlleri dosyadan alacak
for url in ["https://www.flipkart.com/lenovo-ideapad-slim-5-oled-intel-core-ultra-125h-16-gb-1-tb-ssd-windows-11-home-14imh9-laptop/p/itmd68c19b8eeeba?pid=COMGXAU9B7GGGZH4&lid=LSTCOMGXAU9B7GGGZH4QBWTKF&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_11&otracker=product_breadCrumbs_Laptops&fm=organic&iid=28056f02-b13b-4a72-9a5a-e870bd123003.COMGXAU9B7GGGZH4.SEARCH&ppt=browse&ppn=browse"]:
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    # Get name and highlights
    name = soup.find('span', attrs={'class':'B_NuCI'}).string
    highlights_li_arr = soup.find_all('li', attrs={'class':'_21Ahn-'})
    highlights = []
    for li in highlights_li_arr:
        highlights.append(li.string)

    # Get features (optional)
    features_div_arr =  soup.find_all('div', attrs={'class':'_3qWObK'})
    features= []
    if features_div_arr:
        for div in features_div_arr:
            parent = div.parent
            f = dict(title = parent.contents[0].string, description = parent.contents[1].contents[0].string)
            features.append(f)

    # Get specifications
    specifications_parent_div = soup.find('div', attrs={'class':'_1UhVsV'})
    specifications = []
    for specification_div in specifications_parent_div.contents:
        category = specification_div.contents[0].string
        properties = []
        table = specification_div.contents[1].contents[0] #tbody

        for tr in table:
            properties.append({"name":tr.contents[0].string, "content": tr.contents[1].string})
        
        specifications.append(dict(category = category, properties = properties))
    
    # Get ratings
    ratings = []
    all_reviews_div = soup.find('div', attrs={'class':'_3UAT2v _16PBlm'})
    ratings_div = soup.find('div', class_='_2e3Uck')
    #if review count is greater than three then go to reviews page
    if all_reviews_div:
        rating_url = "https://www.flipkart.com" + all_reviews_div.parent.get('href')
        # ratings_thread = WebDriverThread(target=get_laptop_ratings, args=(rating_url,))
        # ratings_thread.start()
        # ratings = ratings_thread.join()
    #if review count is less than three then get ratings from the current page
    elif ratings_div:
        overall_rating = ratings_div.contents[0].contents[0].contents[0].contents[0].contents[0].contents[0].text
        ratings.append({"Overall": overall_rating})

    # Get reviews
    reviews = []
    review_div_arr = soup.find_all('div', class_='col _2wzgFH')
    #if review count is greater than three then go to reviews page
    if all_reviews_div:
        reviews_thread = WebDriverThread(target=get_laptop_reviews, args=(rating_url,))
        reviews_thread.start()
        reviews = reviews_thread.join()
    #if review count is less than three then get ratings from the current page
    elif review_div_arr:
        get_reviews_on_a_page(url,driver,reviews,"col _2wzgFH")

    # Get manufacturer
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._1JDTUN"))).click()


    # Add the laptop to the array (Ending)
    laptop = Laptop(url=url,name=name,highlights=highlights,features=features,
                    specifications=specifications,ratings=ratings,reviews=reviews)
    
    laptop_array.append(laptop.__dict__)




driver.quit()

print("Started Writing Laptops To File")
write_array_to_json(laptop_array, file_to_save_laptop_details)
print("Finished Writing Laptops To File")