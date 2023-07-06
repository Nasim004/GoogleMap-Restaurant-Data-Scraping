import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
no_of_restaurants_details_needed = int(input("Enter limit of restaurants : "))
ChromeDriverManager().install()
driver=webdriver.Chrome()
driver.get(f'https://www.google.com/maps/search/restaurants+in+usa+/@39.4855508,-115.7980212,4z/data=!4m2!2m1!6e5?entry=ttu')
driver.maximize_window()
time.sleep(3)
restaurants = []
while len(restaurants) <= no_of_restaurants_details_needed:
    driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]').send_keys(Keys.END)
    time.sleep(10)
    new_restaurants = driver.find_elements(By.XPATH, '//div[@role="article"]')
    restaurants.extend(new_restaurants)
restaurant_data = []
for restaurant in restaurants:
    restaurant_dict = {}
    try:
        restaurant.click()
    except:
        pass
    time.sleep(3)
    restaurant_name = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h1')
    time.sleep(0.5)
    try:
        restaurant_rating = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]').text
    except:
        restaurant_rating = "Not Given"
    try:
        thumbnail = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[1]/div[1]/button/img')
        restaurant_image = thumbnail.get_attribute("src")
    except:
        restaurant_image="Not Image"
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    restaurant_dict["Restaurant Name"] = restaurant_name.text
    restaurant_dict["Star Rating"] = restaurant_rating
    restaurant_dict["Thumbnail Image"] = restaurant_image
    restaurant_data.append(restaurant_dict)
with open("Restaurant Data.json","w") as outfile:
    json.dump(restaurant_data,outfile)
driver.quit()



