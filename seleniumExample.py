
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() #tam ekran acılmasını saglar
driver.get("https://www.google.com/")
sleep(5)
input = driver.find_element(By.NAME, "q") ##google da arama yapma
input.send_keys("kodlama.io") #aramaya yazı yazabilme
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click() ##butona tıklama
sleep(2)
firstResult = driver.find_element(By.XPATH, "//[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")
# sleep(10)
# input() webbrowser ın kapanmamasını sağlar.
while True:
   continue

# HTML LOCATORS 
# web scraping
# data scraping 