from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import csv
import re

#create/open csv
with open('train_reviews.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(["course", "review", "rate"])

# courses
web_courses=["https://www.udemy.com/course/programa-completo-de-data-science-todo-para-los-datos/",
              "https://www.udemy.com/course/python-ciencia-de-datos/", 
              "https://www.udemy.com/course/machinelearningpython/",
              "https://www.udemy.com/course/master-dashboards-interactivos-con-python-dash-plotly/",
              "https://www.udemy.com/course/curso-de-deep-learning-con-kerastensorflow-en-python/",
              "https://www.udemy.com/course/machinelearning-es/",
              "https://www.udemy.com/course/aprende-ciencia-de-datos-con-python/",
              "https://www.udemy.com/course/ciencia-de-datos-para-todos-los-publicos/",
              "https://www.udemy.com/course/estadistica-para-ciencia-de-datos/",
              "https://www.udemy.com/course/python-para-ciencia-de-datos/",
              "https://www.udemy.com/course/ciencia-de-datos-con-python-en-qgis34/",
              "https://www.udemy.com/course/r-developer-big-data-con-r/",
              ]
#selenium setting


for num_course in web_courses:
    options = Options()
    options.add_argument("--disable-notifications")
    PATH= "D:/Ivonne/Downloads/chromedriver_win32/chromedriver.exe"
    driver=webdriver.Chrome(executable_path=PATH, options=options) 
    driver.get(num_course)
    
    # print(driver.title)
    driver.execute_script("window.scrollTo(0, 7100)")

    #closing pop up
    popup=WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH,'//button[@data-purpose="dismiss"]')))
    popup.click()

    # titulo
    course_element= driver.find_element_by_xpath('//h1[@data-purpose="lead-title"]')
    course=course_element.text
    # press see more review button
    try:
        for i in list(range(80)):
            # driver.implicitly_wait(10) 
            element = WebDriverWait(driver, 40).until( 
                EC.element_to_be_clickable((By.XPATH,'//button[@data-purpose="show-more-review-button"]' )))
            element.click()
    except:
        print(course+":    "+str(i)+" fin de reviews")

    # gel all visible reviews
    reviews_texts=driver.find_elements_by_xpath('//div[@data-purpose="review-comment-content"]')
    reviews_rates=driver.find_elements_by_xpath('//div[@data-purpose="individual-review"]//div[2]//div[2]//span[@class="udlite-sr-only"]')
    
    num=len(reviews_texts) if len(reviews_texts)<len(reviews_rates) else len(reviews_rates) 

    #write dataset
    with open('train_reviews.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        for item in range(num):
            review=re.sub("[,;]"," ",reviews_texts[item].text)
            rate=re.sub("[,;]"," ",reviews_rates[item].text)
            writer.writerow([course, review, rate])

    print(course +':    '+str(num))
    print("_______"*10)    
    
    driver.quit()
# for reviews_block in reviews_blocks:

# reviews_rate=driver.find_element_by_xpath()



# except: 
#     print('yiyi') 
# #     else quit 
#    driver.quit() 

# a=driver.find_elements_by_class_name('udlite-btn udlite-btn-medium udlite-btn-secondary udlite-heading-sm')

# for item in a:
#     print (item.text)

#driver.quit(