"""
We are going to have you automate some features on Yummly.com:
    - Test_A: will have you open yummly.co and verify the page loaded
    - Test_B: search for "chicken" and retrieve the titles of the first 5 recipes
    - Test_C: From the homepage, open a recipe and print the Ingredients of that recipe
    NOTE: You do not need to be logged in for this, so do not worry about creating any accounts.
          This should all be done in a logged out state.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#TestA
driver = webdriver.Firefox()
driver.get("http://yummly.co")
assert "Yummly" in driver.title
time.sleep(5)

#TestB
elem = driver.find_element_by_name("searchBoxInput")
elem.clear()
elem.send_keys("chicken")
elem.send_keys(Keys.RETURN)
time.sleep(5)
titles = []
for title in driver.find_elements_by_class_name("card-title"):
    titles.append(title.text)
for i in range(0, 5):
    print(titles[i])

#TestC
driver.get("http://yummly.co")
assert "Yummly" in driver.title
driver.find_element_by_class_name("recipe-card").click()
time.sleep(5)
ingredients = driver.find_elements_by_class_name("ingredient")
for ingredient in ingredients:
    print(ingredient.text)
