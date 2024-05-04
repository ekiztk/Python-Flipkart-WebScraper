from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.by import By
import constants.laptop_constants as constants

def get_laptop_customer_questions(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
    driver.implicitly_wait(5)
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    
    all_questions_a = soup.find('a', attrs={'class': constants.ALL_QUESTIONS_A}) 
    customer_questions = []
    # check if questions are less than three
    if all_questions_a is None:
        questions_div_arr = soup.find_all('div', attrs={'class': constants.A_QUESTION_DIV})
        for parent in questions_div_arr:
            customer_question = get_a_question_and_answers(parent)
            customer_questions.append(customer_question) 
    else:
        driver.get("https://www.flipkart.com" + all_questions_a['href'])
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        try:
            load_more_a = driver.find_element(By.CLASS_NAME, constants.LOAD_MORE_A)
            while load_more_a is not None:
                load_more_a.click()
                sleep(1)
                load_more_a = driver.find_element(By.CLASS_NAME, constants.LOAD_MORE_A)
        except:
            pass

        updatedSoup = BeautifulSoup(driver.page_source, "html.parser")
        questions_div_arr = updatedSoup.find_all('div', attrs={'class': constants.A_QUESTION_DIV})
        for parent in questions_div_arr:
            customer_question = get_a_question_and_answers(parent)
            customer_questions.append(customer_question)

    return customer_questions


def get_a_question_and_answers(parent_div):
    question = parent_div.contents[0].contents[0].contents[1].text
    content = parent_div.contents[0].contents[1].contents[0].contents[1].text
    answeredBy = parent_div.contents[0].contents[1].contents[1].contents[0].contents[0].contents[0].text
    answererRole = parent_div.contents[0].contents[1].contents[1].contents[0].contents[1].text
    numberOfLikes = parent_div.contents[0].contents[1].contents[1].contents[1].contents[0].text
    numberOfDislikes = parent_div.contents[0].contents[1].contents[1].contents[1].contents[1].text

    return { "question": question, 
            "answers": [{ "content": content, "answeredBy":answeredBy,"answererRole": answererRole, 
                        "numberOfLikes":numberOfLikes, "numberOfDislikes":numberOfDislikes}]}