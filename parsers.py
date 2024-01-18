from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import datetime


def get_data(group:str = "6", course: str = "1" , program: str = "RDBI0"):
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)
    driver.get("https://nodarbibas.rtu.lv/?lang=en")

    select = Select(driver.find_element(By.ID, "program-id"))
    for opt in select.options:
        if program in opt.text:
            opt.click()

    select = Select(driver.find_element(By.ID, "course-id"))
    for opt in select.options:
        if course == opt.text:
            opt.click()
    time.sleep(1)

    select = Select(driver.find_element(By.ID, "group-id"))
    for opt in select.options:
        if group == opt.text:
            opt.click()
    time.sleep(1)


    date = datetime.datetime.utcnow()
    day = str(date.year)
    if date.month < 10:
        day += "-0" + str(date.month)
    else:
        day += "-" + str(date.month)
    if date.day < 10:
        day += "-0" + str(date.day)
    else:
        day += "-" + str(date.day)


    timels = driver.find_elements(By.XPATH, f"//td[@data-date='{day}']/div/div[@class='fc-daygrid-day-events']/div/a/div[@class='fc-event-time']")
    title = driver.find_elements(By.XPATH, f"//td[@data-date='{day}']/div/div[@class='fc-daygrid-day-events']/div/a/div[@class='fc-event-title']")

    times = []
    titels = []
    for i in range(len(timels)):
        times.append( timels[i].text)
        titels.append( title[i].text.encode("utf-8"))
        
        
    return times, titels


# times , titels = get_data()
# print(times)
# print(titels)