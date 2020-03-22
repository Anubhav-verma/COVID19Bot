from selenium import webdriver
from robot.api import logger
# from BeautifulSoup4 import BeautifulSoup4
# import pandas as pd

#driver = webdriver.Chrome("C:\\bin\\chromedriver.exe")



def get_total_cases_count():
    logger.console("Hi there")
    driver = webdriver.Chrome("C:\\bin\\chromedriver.exe")
    driver.get("https://www.mohfw.gov.in/")
    logger.console("Hi there")
    total_cases = driver.find_element_by_xpath("""//div[contains(text(),'Active COVID 2019 cases *')]/preceding-sibling::span[@class="icount"]""").text
    logger.console(total_cases)
    driver.close()
    return total_cases

get_total_cases_count()

#driver.close()