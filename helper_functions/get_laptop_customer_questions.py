from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By

def get_laptop_customer_questions(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
    driver.implicitly_wait(5)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    
    all_questions_a = soup.find('div', attrs={'class':'_2KpZ6l dVBe_p'}) 
    customer_questions = []
    # check if questions are less than three
    if all_questions_a is None:
        questions_div_arr = soup.find_all('div', attrs={'class':'_1RWRBu'})
        for parent in questions_div_arr:
            customer_questions.append(get_a_question_and_answers(parent,driver,url)) 

    return customer_questions


def get_a_question_and_answers(parent_div, webDriver=None, url=None):
    multiple_answers_a = parent_div.find('a', attrs={'class':'nC1FHF'})
    print(multiple_answers_a)
    if multiple_answers_a is not None:
        #hata burda, soruya özel cevapler penceresini nasıl açarız?
        print(multiple_answers_a)
        multiple_answers_a = webDriver.find_element(By.CLASS_NAME, "selected_answers_by_scraper")
        multiple_answers_a.click()

        sleep(10)

        updatedSoup = BeautifulSoup(webDriver.page_source, "html.parser")
        question = updatedSoup.find('a', attrs={'class':'_1xR0kG _3cziW5 Xj9vSS _1N3Db8'}).text
        answers_div_arr =  updatedSoup.find_all('div', attrs={'class':'_1RWRBu rR7Fqx'}) 

        answers = []
        for parent in answers_div_arr:
            content = parent.contents[0].contents[0].contents[1].text
            numberOfLikes = parent_div.contents[0].contents[1].contents[1].contents[0].contents[1].text
            numberOfDislikes = parent_div.contents[0].contents[1].contents[1].contents[1].contents[1].text
            answers.append({ "content": content, "numberOfLikes":numberOfLikes, "numberOfDislikes":numberOfDislikes}) 
                
        close_btn = updatedSoup.find('button', attrs={'class':'_2KpZ6l _1KAjNd'})
        close_btn.click()
        multiple_answers_a['class'] = "nC1FHF"

        return { "question": question, "answers": answers}
    else:
        question = parent_div.contents[0].contents[0].contents[1].text
        content = parent_div.contents[0].contents[1].contents[0].contents[1].text
        numberOfLikes = parent_div.contents[0].contents[1].contents[1].contents[0].contents[1].text
        numberOfDislikes = parent_div.contents[0].contents[1].contents[1].contents[1].contents[1].text

        return { "question": question, "answers": [{ "content": content, "numberOfLikes":numberOfLikes, "numberOfDislikes":numberOfDislikes}]}