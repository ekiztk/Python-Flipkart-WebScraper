from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd
import os
from helper_functions.write_array_to_json import write_array_to_json
from laptop import Laptop

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.implicitly_wait(5)

driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART&otracker=product_breadCrumbs_Laptops")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")

# Getting URLS (sadece bir sayfayı alıyor)
print("Started Getting All Laptop Urls")
all_laptop_a = soup.findAll('a', href=True, attrs={'class':'_1fQZEK'},limit=5)
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

for url in all_laptop_urls:
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
    

    # Get manufacturer
    

    # Add the laptop to the array (Ending)
    laptop = Laptop(url=url,name=name,highlights=highlights,features=features,specifications=specifications)
    laptop_array.append(laptop.__dict__)




driver.quit()

print("Started Writing Laptops To File")
write_array_to_json(laptop_array, file_to_save_laptop_details)
print("Finished Writing Laptops To File")